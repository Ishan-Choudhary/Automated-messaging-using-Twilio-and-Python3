from twilio.rest import Client

ACCOUNT_SID = ('Your Account SID')
AUTH_TOKEN = ('Your Authorisation Token')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(from_='number you recieved',
                        to='number to message to',
                        body='I have written this through python')
