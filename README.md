# Python TCP

###Features

- Validate users
- Add user
- Run migrations
- Reset and create schemas

###Requirements

Python 3.x


##Server

####Run server

`$ python3 server.py`


####Menu options

#####1. Validate users
Have you already created the database and the loaded users? then you are ready to validate users.

Run the following command:

`$ python3 server.py`

Then, select the option 1 and the server will be ready to listen to messages on host 127.0.0.1 and port 65432:

`$ -- Mode: Validate users - App listen on: 127.0.0.1:65432 ---`

#####2. Add user
You have already created the database but you need to load a new user? then you are in the correct option.

Run the following command:

`$ python3 server.py`

Then, select the option 2 and follow the steps:

1. Enter the name of the user to add:

`$ Please, enter the first name:`

2. Enter the last name of the user to add:

`$ Now enter the last name:`

3. When you are ready, press any key to start the server and send the card id:

`$ Finally, prepare the card. Are you ready? Enter any key when you're ready.`

4. The server is waiting the card id

`$ -- Mode: Add users - App listen on: 127.0.0.1:65432 ---`

5. Done!

#####3. Run migrations
You have already created the database but you need to load several users in batch? OK, let's start!

1. Edit the migrations.py file adding other users like:

```python
def insert_users():
  orm.insert_user(
    name='John',
    last_name='Doe',
    card_id='ASF1235',
  )
  orm.insert_user(
    name='John',
    last_name='Doe',
    card_id='ASF1235',
  )

```

2. Then, run:

`$ python3 server.py`

3. Select the option 3

3. Finally press "Y" (yes)

#####4. Reset and create schemas
You have not created the database and the tables yet?  What are you waiting for?

1. Run the following command:

`$ python3 server.py`

3. Select the option 4

3. Finally press "Y" (yes)


##Client

####Run client test
> Remember to have the server running in another tab.

1. Run the following command:

`$ python3 client.py`
