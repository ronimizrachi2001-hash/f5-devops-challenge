# Root Cause Analysis

Fill this in as you go. Bullet points are fine — be specific, not long.

---

## Defect 1: Proxy image fails to build

### Symptom / error output:
    Docker build failed with error code 100 during the proxy image compilation.

### How I diagnosed it:
    Inspected the build logs where error code 100 appeared, and reviewed the proxy's Dockerfile instruction sequence.

### Root cause:
    Incorrect order of Dockerfile instructions: the COPY command was placed before the dependency installation steps, which caused compilation issues and triggered error code 100.

### Fix:
    Reordered the Dockerfile layers so that dependency definitions and installation steps occur before copying the rest of the source code, resolving the build failure and optimizing layer caching.

---

## Defect 2: Proxy cannot reach the backend

### Symptom / error output:
    Nginx returned '502 Bad Gateway' errors when attempting to proxy requests, because it could not correctly route traffic to the backend service.

### How I diagnosed it:
    Inspected the Nginx configuration file inside the proxy service and checked how upstream routing was defined.

### Root cause:
    The Nginx configuration file used a hardcoded IP address instead of the internal Docker Compose service name (backend), causing routing and resolution failures.

### Fix:
    Updated the Nginx configuration file to point directly to the 'backend' service name instead of a static IP, allowing Docker's internal DNS to resolve the service correctly.

---

## Defect 3: Tests still fail after fixing defect 2

### Symptom / error output:
    Integration tests failed immediately on execution because the test script made a single request before the backend web server was fully ready to accept traffic.

### How I diagnosed it:
    Inspected the execution flow and recognized that a single, non-retrying HTTP request in 'test_integration.py' was racing against the container's startup time.

### Root cause:
    A startup race condition: the test runner script executed and fired its single request before the backend service finished initializing and binding to its port.

### Fix, and why I chose it over the alternatives:
    Implemented a retry and polling mechanism (up to 10 retries with a 1-second delay and exception handling) inside 'test_integration.py'. This approach was chosen because it is self-ained, avoids rigid hardcoded delays, and ensures the test suite executes reliably as soon as the service becomes operational.

---

## Defect 4: CI pipeline fails

### Symptom / error output:
    GitHub Actions workflow failed immediately upon execution with exit code 126 and a permission denied error.

### How I diagnosed it:
    Reviewed the GitHub Actions CI logs and identified that the shell script lacked executable permissions in the fresh runner Linux environment.

### Root cause:
    Git file modes on Unix systems do not always preserve executable bits across checkouts depending on the repository configuration or the runner's environment setup.

### Fix:
    Added an explicit 'chmod +x ./scripts/run-tests.sh' step directly inside the GitHub Actions workflow file (ci.yml) prior to executing the script, guaranteeing correct execution permissions on every pipeline run.

---

## Bonus questions

Optional. Answer only the ones you got to — number them, skip the rest.

>

---

## Anything you would do differently with more time
