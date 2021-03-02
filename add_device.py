import requests
from auth_dnac import get_auth_token


def add_device():
    """
    Send a POST request to the DNAC always on sandbox to add a network devices.
    """

    DNAC_URL = "https://sandboxdnac.cisco.com/"
    token = get_auth_token()
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    new_device_dict = {
        "type" : "NETWORK_DEVICE",
        "computeDevice" : False,
        "snmpVersion" : "V3",
        "snmpUserName" : "superman",
        "snmpMode" : "RW",
        "snmpAuthProtocol" : "SHA",
        "snmpAuthPassphrase" : "cisco",
        "snmpPrivProtocol" : "AES128",
        "snmpPrivPassphrase" : "cisco",
        "snmpRetry" : "3",
        "snmpTimeout" : "5",
        "cliTransport" : "SSH",
        "userName" : "admin123",
        "password" : "cisco123",
        "enablePassword" : "cisco123",
    }

    post_response= requests.post(f"{DNAC_URL}dna/intent/api/v1/network-device", json=new_device_dict, headers=headers)

    if post_response.ok:
        print(f"Request accepted: status code {post_response.status_code}")
    else:
        print(f"Request failed: status code {post_response.status_code}")

if __name__ == "__main__":
    add_device()