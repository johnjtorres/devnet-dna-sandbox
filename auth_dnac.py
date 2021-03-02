import requests


def get_auth_token():
    """
    Send a POST request to fetch an auth token to the DNAC always on sandbox environment.
    """

    DNAC_URL = "https://sandboxdnac.cisco.com/"
    DNAC_USER = "devnetuser"
    DNAC_PASSWORD = "Cisco123!"

    headers = {"Content-Type": "application/json"}

    auth_resp = requests.post(f"{DNAC_URL}dna/system/api/v1/auth/token", auth=(DNAC_USER, DNAC_PASSWORD), headers=headers)
    
    return auth_resp.json()["Token"]


if __name__ == "__main__":
    get_auth_token()
