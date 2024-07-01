from twilio.rest import Client

account_sid = '***********'
auth_token = '************'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19033548003',
  body='this is testing message from twilio \n\n       -Anjesh',
  to='+91********71'
)

print(message.sid)