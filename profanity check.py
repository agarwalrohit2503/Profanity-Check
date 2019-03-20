#
#author - Rohit Agarwal
import urllib
from twilio.rest import Client
text=input("Please Enter the message:")
text2=text
text=text.split()
result = False
for word in text:
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+word)
    output=connection.read()
    output=output.decode('utf-8')
    if 'true' in output:
        result=True
        break
if result == False:
    # Your Account SID from twilio.com/console
    account_sid = "------------------"
    # # Your Auth Token from twilio.com/console
    auth_token  = "-------------------"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+9179****************", 
        from_="+***********",
        body=text2)

    print(message.sid)
else:
    print('It contains bad words')