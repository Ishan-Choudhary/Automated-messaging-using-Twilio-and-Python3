from twilio.rest import Client

ACCOUNT_SID = ('AC54903fd3e716820edaef9885350d5f1c')
AUTH_TOKEN = ('8e732e74430934c068b1772dac2ffb68')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(from_='+12513195138',
                        to='+919920062711',
                        body='I have written this through python')
