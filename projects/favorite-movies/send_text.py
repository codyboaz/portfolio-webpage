from twilio.rest import TwilioRestClient

account_sid = "AC7d6856e85e7bb75659c9e6d01e65bf6e" # Your Account SID from www.twilio.com/console
auth_token  = "c0ffca2844fb6e6f095961b5d0b6f143"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This message was sent using Twilio",
    to="+18315665190",    # Replace with your phone number
    from_="+18313161706") # Replace with your Twilio number

print(message.sid)
