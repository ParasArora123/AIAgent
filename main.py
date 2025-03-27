import os

from api_functions.vapi_api_functions import *
from models import *
from scripts.execute_calls import make_concurrent_outbound_calls

if __name__ == "__main__":

    VAPI_PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")
    TEST_PHONE_NUMBER = os.getenv("TEST_PHONE_NUMBER")

    assistant = Assistant(
        name="John Doe",
        firstMessage="Hello, how are you?",
        transcriber=Transcriber(provider="openai", 
                                model="gpt-4o-transcribe",
                                language="en"),
        model=Model(provider="openai", 
                    model="gpt-3.5-turbo",
                    messages=[Message(role="system", 
                                        content="You are a helpful assistant")]),
        voice=Voice(provider="11labs", 
                    voiceId="burt"),
    )

    assistant2 = Assistant(
        name="John Does",
        firstMessage="Yo, how are you?",
        transcriber=Transcriber(provider="openai", 
                                model="gpt-4o-transcribe",
                                language="en"),
        model=Model(provider="openai", 
                    model="gpt-3.5-turbo",
                    messages=[Message(role="system", 
                                        content="You are an unhelpful assistant")]),
        voice=Voice(provider="11labs", 
                    voiceId="burt"),
    )

    assistants = [assistant, assistant2]
    make_concurrent_outbound_calls(phone_number_ID=VAPI_PHONE_NUMBER_ID, 
                                   assistants=assistants, 
                                   phone_number_to_call=TEST_PHONE_NUMBER)
