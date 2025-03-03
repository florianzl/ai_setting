# src/telephony/outbound_call.py

from twilio.rest import Client

account_sid = "ACdc070ee620650696a5dabebc14b94b5c"
auth_token = "61714554b2c025905643f4c7b34e1625"
client = Client(account_sid, auth_token)

call = client.calls.create(
    from_="+12566009667",  # Deine verifizierte Twilio-Nummer
    to="+995599884923",    # Die Zielnummer, die du anrufen willst
    url="https://ab39-185-115-7-111.ngrok-free.app/twilio/outbound",
    method="POST"
)

print("Call SID:", call.sid)
