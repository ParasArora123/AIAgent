import time
from typing import List
from api_functions.vapi_api_functions import make_outbound_call, get_call_data
from scripts.deserializer import to_filtered_dict
from models import Assistant

def make_concurrent_outbound_calls(phone_number_ID: str, 
                                   assistants: List[Assistant], 
                                   phone_number_to_call: str) -> dict:
    """
    Make concurrent outbound calls using VAPI API. The number of calls made is equal to the number of assistants.
    VAPI accepts up to 10 concurrent calls and we must include a 1 second delay between calls.
    """
    # We could consider using threads here, but synchronous calls work fine for now with the 3 second delay, since 
    # the max calls we can make "concurrently" is 10 anyways, so the tests would happen in 30 seconds.
    call_data = []
    for assistant in assistants:
        print(f"Making outbound call with assistant: {assistant.name} from phone number ID: {phone_number_ID} to phone number: {phone_number_to_call}")

        deserialized_assistant = to_filtered_dict(assistant)
        response = make_outbound_call(
            phone_number_ID=phone_number_ID, 
            deserialized_assistant=deserialized_assistant,
            phone_number_to_call=phone_number_to_call
        )

        call_data.append(get_call_data(response.get("callId")))
        time.sleep(3)

    return call_data
