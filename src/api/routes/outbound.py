from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
test_number = os.getenv("TEST_NUMBER")
ngrok_url = os.getenv("NGROK_URL")

client = Client(account_sid, auth_token)

call = client.calls.create(
    from_=twilio_number,
    to=test_number,
    url=f"{ngrok_url}/twilio/outbound",
    method="POST"
)

print("Call SID:", call.sid)