from twilio.rest import Client

# your account SID and Auth Token from twilio.com/user/account
account_sid = "ACd5751f3068d5e314ad8a61f016664900"
client = client (account_sid, auth_token)

message = client.sms.messages.create(
        body="Body of the text"
        to="+16504683456"
        from_="+14158141829")
print message.sid
