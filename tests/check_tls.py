"""Probe Requests' default CA bundle without running the gift checker.

Run manually with ``python tests/check_tls.py``. Only the incident's official
test hosts and example.com are contacted. No environment proxies or credentials
are loaded. DNS failures and timeouts are failures, not proof of distrust.
"""

import requests


def main():
    with requests.Session() as session:
        session.trust_env = False
        for host in (
            "dv-g3b-emudhra.we-have-a-problem.com",
            "dv-g3b-aaa-emudhra.we-have-a-problem.com",
        ):
            try:
                session.get("https://" + host + "/", timeout=15)
            except requests.exceptions.SSLError as error:
                if "CERTIFICATE_VERIFY_FAILED" not in str(error):
                    raise
                print(host + ": certificate rejected")
            else:
                raise AssertionError(host + ": compromised chain accepted")

        response = session.get("https://example.com/", timeout=15)
        response.raise_for_status()
        print("example.com: HTTPS succeeded")


if __name__ == "__main__":
    main()
