import os
import requests

from dotenv import load_dotenv

load_dotenv()

VAPI_BASE_URL = os.environ.get("VAPI_BASE_URL", "https://api.vapi.ai")
VAPI_API_KEY= os.environ.get("VAPI_API_KEY", "")

def get_call_data(call_ID: str) -> dict:
    """
    Get call data using call_ID
    """
    response = requests.get(
        f"{VAPI_BASE_URL}/call/{call_ID}",
        headers={
            "Authorization": f"Bearer {VAPI_API_KEY}"
        }
    )
    log_api_response(response)
    return response.json()


def create_assistant(deserialized_assistant: dict) -> dict:
    """
    Create an assistant using VAPI API
    """
    response = requests.post(
        f"{VAPI_BASE_URL}/assistant",
        headers={
            "Authorization": f"Bearer {VAPI_API_KEY}",
            "Content-Type": "application/json"
        },
        json=deserialized_assistant
    )

    log_api_response(response)
    return response.json()
    
def make_outbound_call(phone_number_ID: str, 
                       deserialized_assistant: dict, 
                       phone_number_to_call: str) -> dict:
    """
    Make an outbound call using VAPI API to the phone_number_to_call using the assistant object and phone number ID
    """
    try:
        response = requests.post(
            f"{VAPI_BASE_URL}/call",
            headers={
                "Authorization": f"Bearer {VAPI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "assistant": deserialized_assistant,
                "phoneNumberId": phone_number_ID,
                "customer": {
                    "number": phone_number_to_call
                }
            },
        )
        log_api_response(response)
        return response.json()
    
    except Exception as error:
        return {
            "message": "Failed to place outbound call",
            "error": str(error)
        }

def log_api_response(response: dict) -> None:
    """
    Log the response from the VAPI API
    """
    print(f"Response status code: {response.status_code}")
    print(f"Response headers: {response.headers}")
    print(f"Response body: {response.text}")
    