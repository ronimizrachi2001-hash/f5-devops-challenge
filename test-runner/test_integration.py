import json
import os
import sys
import time
import urllib.request

PROXY_URL = os.environ.get("PROXY_URL", "http://proxy:80")

def run_tests():
    print(f"Starting integration tests against {PROXY_URL}...")

    # Test 1: Verify Proxy health endpoint
    print("Testing /nginx-health...")
    req = urllib.request.Request(f"{PROXY_URL}/nginx-health")
    with urllib.request.urlopen(req, timeout=3) as res:
        if res.status != 200:
            print(f"FAILED: /nginx-health returned status {res.status}")
            sys.exit(1)
        data = json.loads(res.read().decode())
        if data.get("proxy") != "ok":
            print(f"FAILED: Unexpected payload from /nginx-health: {data}")
            sys.exit(1)
        print("PASSED: /nginx-health")

    # Test 2: Verify Proxied backend endpoint with retries for startup race condition
    print("Testing proxied backend /api/info...")
    max_retries = 10
    delay = 1
    response_data = None

    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(f"{PROXY_URL}/api/info")
            with urllib.request.urlopen(req, timeout=3) as res:
                if res.status == 200:
                    response_data = res.read().decode()
                    break
        except Exception:
            pass
        
        print(f"Backend not ready yet, retrying in {delay}s (attempt {attempt}/{max_retries})...")
        time.sleep(delay)

    if response_data is None:
        print("FAILED: /api/info failed to respond after multiple retries")
        sys.exit(1)

    data = json.loads(response_data)
    if data.get("status") != "operational":
        print(f"FAILED: Unexpected backend payload: {data}")
        sys.exit(1)
    print("PASSED: /api/info proxied successfully!")

    print("ALL TESTS PASSED!")

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"TEST RUNNER CRASHED: {e}")
        sys.exit(1)
