import os
import json

from scripts.execute_calls import make_concurrent_outbound_calls
from scripts.generate_profiles import generate_assistant_profiles, retrieve_system_prompt, retrieve_voice_agent_type

if __name__ == "__main__":

    VAPI_PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")
    TEST_PHONE_NUMBER = os.getenv("TEST_PHONE_NUMBER")
    
    assistants = generate_assistant_profiles(num_profiles=10, 
                                             voice_agent_system_prompt=retrieve_system_prompt(),
                                             voice_agent_type=retrieve_voice_agent_type())
    
    call_data = make_concurrent_outbound_calls(phone_number_ID=VAPI_PHONE_NUMBER_ID, 
                                               assistants=assistants, 
                                               phone_number_to_call=TEST_PHONE_NUMBER)
    
    for i, call_log in enumerate(call_data, start=1):
        print(f"\nCall {i} Data:")
        print(json.dumps(call_log, indent=4))
