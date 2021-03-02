import requests
from auth_dnac import get_auth_token


def get_network_devices():
    """
    Send a GET request to the DNAC always on sandbox to fetch the list of network devices.
    """
    DNAC_URL = "https://sandboxdnac.cisco.com/"
    token = get_auth_token()
    headers = {"X-Auth-Token": token}

    get_response= requests.get(f"{DNAC_URL}dna/intent/api/v1/network-device", headers=headers)
    
    for device in get_response.json()["response"]:
        print(f"ID: {device['id']}   hostname: {device['hostname']}")

if __name__ == "__main__":
    get_network_devices()