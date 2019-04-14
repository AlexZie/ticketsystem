# Make task management better! 
[![Build Status](https://travis-ci.org/AlexZie/ticketsystem.svg?branch=master)](https://travis-ci.org/AlexZie/ticketsystem)
[![Coverage Status](https://coveralls.io/repos/github/AlexZie/ticketsystem/badge.svg?branch=master)](https://coveralls.io/github/AlexZie/ticketsystem?branch=master)
# Installation

Install a virtual environment:
```
sudo pip3 install virtualenv
```

Create a new project directory:
```
mkdir ~/projectname
cd ~/projectname
```

Download the repo and move the project into that directory:
```
cp -r /path_of_downloads /path_of_project_directory
```

Start the virtual environment in the specific directory:
```
virtualenv venv
cd ~/projectname
source venv/bin/activate
```

With the new terminal look (like: (venv)username@hostname:~/projectname) you are ready to install the requirements:
```
cd ticketsystem

pip3 install -r requirements.txt
```

Now all requirements for the project are downloaded and installed.
The database must be updated:
```
python3 manage.py makemigrations
python3 manage.py migrate
```


Create an admin to control the ticketsystem:
```
python3 manage.py createsuperuser
```

# Testing

```
 coverage run --source='.' manage.py test
 coverage html
  
```
# Install Selenium 

https://christopher.su/2015/selenium-chromedriver-ubuntu/

```
