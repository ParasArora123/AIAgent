import time
from typing import List
from api_functions.vapi_api_functions import make_outbound_call
from scripts.deserializer import to_filtered_dict
from models import Assistant

def make_concurrent_outbound_calls(phone_number_ID: str, 
                                   assistants: List[Assistant], 
                                   phone_number_to_call: str) -> dict:
    """
    Make concurrent outbound calls using VAPI API. The number of calls made is equal to the number of assistants.
    VAPI accepts up to 10 concurrent calls and we must include a 1 second delay between calls.
    """
    for assistant in assistants:
        print(f"Making outbound call with assistant: {assistant.name} from phone number ID: {phone_number_ID} to phone number: {phone_number_to_call}")

        deserialized_assistant = to_filtered_dict(assistant)
        make_outbound_call(
            phone_number_ID=phone_number_ID, 
            deserialized_assistant=deserialized_assistant,
            phone_number_to_call=phone_number_to_call
        )
        time.sleep(3)
