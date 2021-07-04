# API Management :: 3rd Party Integration


### Problem statement : To ease out the process of 3rd Party API (webhooks) integration

### Installation
This app requires python 3.6 or later versions.
Clone the app using `git clone https://github.com/242jainabhi/gemini.git`
Root directory is 'gemini'. Create virtual environment and execute `pip install -r requirements.txt` to install all the dependencies.

Install MySQL and create a DB called `geminidb`.

To launch the application on local server (127.0.0.1:5000), execute the command `python manage.py`.
The app is now available on your local server.

# APIs
- /user/<int:user_id> (GET, PUT, DELETE on user resource)
- /user (POST on user resource)
- /users (GET method to fetch all users)
- /workspace
- /workspace/<int:workspace_id>
- /workspaces
- /send_invite
- /accept_invite?uuid=xxxxx

### Technologies used:
- Language: Python
- Web Framework: Flask
- Databse: MySQL
- ORM: SQLALCHEMY
