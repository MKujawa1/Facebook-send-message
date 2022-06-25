import facebook_bot as fbb 

email = 'email' ### email to facebook account
password = 'password' ### password to facebook account
people = ['Name1 Surname1', 'Name2 Surname2'] ### people to send message. If person -> ['Name1 Surname1']
messages = ['message1','message2'] ### messages to send. If message -> ['message1']
### Get configured driver
driver = fbb.conf()
### Login to facebook
driver = fbb.login(driver,email,password)
### Send messages
for person in people:
    for message in messages:
        fbb.send_message(driver,person,message)