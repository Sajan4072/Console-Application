# Console-Application

## Setting up the project
1-Clone the repo \
2-Change directory \
`cd Console-Application`\
3-Create a virtualenv\
`virtualenv env`\
-OR
-Download python 3.8.2 and Create a virtualenv with it \
`py -m virtualenv -p=<your_python_executable> <virtual_environment_directory>`\
`for eg,virtualenv -p C:\Users\lenovo\AppData\Local\Programs\Python\Python37\python.exe env`

4-Activate your environtment\
`env\Sripts\activate` 

5-Install dependencies\
`pip install -requirements.txt`

6-Create a .env file (take refrence from .env.sample.txt)\
-Inside .env\
`SENDER_MAIL="your email address" and SENDER_PASSWORD="your 16 character password i.e your 2 step authentication gmail password"`

****-Note on how to obtain 16 character password\
-goto or search myaccount.google.com\
-goto security\
-scroll down and click on 2 step verification\
-click on get started\
-enter you phone number and click on next\
-enter your code and click on next\
-clickon turn on\
-goto or search myaccount.google.com/apppasswords\
-enter you gmail credentials and go inside\
-slect dropdown option of other custom name\
-enter any name you want and click on generate\
-copy your 16 character password and paste in on .env file

7-Now you can run the main console app \
`python main_console.py `\
OR\
`py main_console.py `

8-Run test cases\
`python -m unittest tests.py`


