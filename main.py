from twilio.rest import Client
import os
from dotenv import load_dotenv
from concatMSG import concatMSG
from datetime import datetime, time
from zoneinfo import ZoneInfo
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
timeCorrect = False
def is_8am():
    # Write Zone Info string in format Country/City in .env
    melbourne_tz = ZoneInfo(str(os.getenv("TIMEZONE")).strip())
    current_time = datetime.now(melbourne_tz)
    
    target_time = time(8, 0, 0) # 8:00:00 AM
    
    # Check if the current time matches the target time
    if current_time.time() == target_time:
        return True
    else:
        return False
while is_8am()!=True:
    # print("SUP") #Testing to see if the while loop while loops
    is_8am()
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to=os.getenv("RECEIVE_NUMBER"),
    from_=os.getenv("TWILIO_NUMBER"),
    body=concatMSG()
    )

print(f"Message SID: {message.sid}")
