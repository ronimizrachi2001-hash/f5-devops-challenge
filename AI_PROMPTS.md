# Generative AI Disclosure

Using AI tools for this challenge is allowed. Be honest here — an accurate
"I used AI heavily" is worth more to us than an inaccurate "I did not".

**Did you use AI tools?** (yes / no):
    yes

**Which ones?** (e.g. ChatGPT, Claude, Copilot, Cursor):
    Gemini

> If you answered **no**, write "N/A" in sections 1 and 2 and skip to
> section 3. That is a perfectly good answer.

---

## 1. Key prompts

List the main prompts you used. Paraphrasing is fine.

1. `Help me analyze why integration tests are failing with 502 Bad Gateway errors against Nginx and how to fix backend readiness races in Docker Compose.`
2. `How can I implement a retry mechanism in Python's urllib script with loop retries and time delays to handle startup race conditions?`
3. `Why is GitHub Actions throwing permission denied (exit code 126) when running a shell script, and how do I fix it in ci.yml?`
4. `What does Docker build error code 100 mean?`

---

## 2. Where the AI got it wrong

Describe **one concrete case** where the AI's answer was wrong, outdated, or
sub-optimal. Cover: what it suggested, how you noticed it was wrong, and what
you did instead. 3–5 sentences.

> Initially, the AI suggested adding complex 'healthcheck' directives directly into the 'docker-compose.yml' file to handle service dependencies natively. However, this approach introduced unexpected behavior and didn't gracefully solve the integration test race condition out-of-the-box in our local environment. I noticed it was sub-optimal because it over-complicated the orchestration configuration without ensuring reliable execution. Instead, I removed the complex healthchecks and implemented a lightweight, robust retry loop directly inside the Python integration test script ('test_integration.py'), which solved the timing issue cleanly and reliably.

---

## 3. Anything in your submission you could not fully explain?

We would rather know. Write "nothing" if that is the case.

> nothing
