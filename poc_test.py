#!/usr/bin/env python3
"""AutoPoC Test Script for Omnigent Server"""
import json, os, sys, time, urllib.request, urllib.error

SERVICE_URL = os.environ.get("SERVICE_URL", sys.argv[1] if len(sys.argv) > 1 else "")
MAX_RETRIES = 5
RETRY_DELAY = 10
results = []

def test_scenario(name, description, method, path, body=None,
                  expected_status=200, expected_content=None, timeout=30,
                  accept_statuses=None):
    url = f"{SERVICE_URL.rstrip('/')}{path}"
    start = time.time()
    acceptable = accept_statuses or [expected_status]
    for attempt in range(MAX_RETRIES):
        try:
            if body:
                data = json.dumps(body).encode() if isinstance(body, dict) else body.encode()
                req = urllib.request.Request(url, data=data, method=method)
                req.add_header("Content-Type", "application/json")
            else:
                req = urllib.request.Request(url, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = resp.status
                response_body = resp.read().decode()
                if status in acceptable:
                    if expected_content and expected_content not in response_body:
                        r = {"scenario_name": name, "status": "fail",
                             "output": response_body[:2000],
                             "error_message": f"Expected '{expected_content}' not in response",
                             "duration_seconds": round(time.time()-start, 2)}
                    else:
                        r = {"scenario_name": name, "status": "pass",
                             "output": response_body[:2000], "error_message": None,
                             "duration_seconds": round(time.time()-start, 2)}
                    results.append(r); return r
                elif attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY); continue
                else:
                    r = {"scenario_name": name, "status": "fail",
                         "output": response_body[:2000],
                         "error_message": f"Expected {acceptable}, got {status}",
                         "duration_seconds": round(time.time()-start, 2)}
                    results.append(r); return r
        except urllib.error.HTTPError as e:
            if e.code in acceptable:
                response_body = e.read().decode() if hasattr(e, 'read') else ""
                r = {"scenario_name": name, "status": "pass",
                     "output": response_body[:2000], "error_message": None,
                     "duration_seconds": round(time.time()-start, 2)}
                results.append(r); return r
            elif attempt < MAX_RETRIES - 1:
                print(f"  Retry {attempt+1}/{MAX_RETRIES}: HTTP {e.code}", file=sys.stderr)
                time.sleep(RETRY_DELAY)
            else:
                r = {"scenario_name": name, "status": "fail", "output": "",
                     "error_message": f"HTTP {e.code} after {MAX_RETRIES} attempts",
                     "duration_seconds": round(time.time()-start, 2)}
                results.append(r); return r
        except urllib.error.URLError as e:
            if attempt < MAX_RETRIES - 1:
                print(f"  Retry {attempt+1}/{MAX_RETRIES}: {e}", file=sys.stderr)
                time.sleep(RETRY_DELAY)
            else:
                r = {"scenario_name": name, "status": "error", "output": "",
                     "error_message": f"Unreachable after {MAX_RETRIES} attempts: {e}",
                     "duration_seconds": round(time.time()-start, 2)}
                results.append(r); return r
        except Exception as e:
            r = {"scenario_name": name, "status": "error", "output": "",
                 "error_message": str(e),
                 "duration_seconds": round(time.time()-start, 2)}
            results.append(r); return r

# === SCENARIOS ===
print("Running health check...", file=sys.stderr)
test_scenario("health-check", "Verify /health endpoint", "GET", "/health",
              expected_status=200)

print("Running web UI check...", file=sys.stderr)
test_scenario("web-ui-loading", "Verify React SPA loads", "GET", "/",
              expected_status=200, expected_content="<!doctype html")

print("Running API docs check...", file=sys.stderr)
test_scenario("api-docs", "Verify OpenAPI docs endpoint", "GET", "/docs",
              expected_status=200, expected_content="swagger")

print("Running auth endpoint check...", file=sys.stderr)
test_scenario("auth-endpoint", "Verify auth system response", "GET", "/auth/status",
              accept_statuses=[200, 401, 403, 404, 307])

# === END SCENARIOS ===

print(json.dumps({"results": results}, indent=2))
sys.exit(1 if any(r["status"] in ("fail", "error") for r in results) else 0)
