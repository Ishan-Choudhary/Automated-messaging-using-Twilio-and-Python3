from twilio.rest import Client

ACCOUNT_SID = ('Your Account SID')
AUTH_TOKEN = ('Your Authorisation Token')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(from_='+12513195138',
                        to='+919920062711',
                        body='I have written this through python')
