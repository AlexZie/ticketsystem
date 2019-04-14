# Aufgabenverwaltung besser machen! 
[![Build Status](https://travis-ci.org/AlexZie/ticketsystem.svg?branch=master)](https://travis-ci.org/AlexZie/ticketsystem)
[![Coverage Status](https://coveralls.io/repos/github/AlexZie/ticketsystem/badge.svg?branch=master)](https://coveralls.io/github/AlexZie/ticketsystem?branch=master)
# Installation

Um den Server zu starten, innerhalb des /mysite Ordners folgenden Befehl ausführen:
```
python3 manage.py runserver
```

Um die Datenbank zu aktualisieren folgenden zwei Befehl ausführen:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Um eine App zustarten folgenden Befehl ausführen (ohne Anführungszeichen):
```
python3 manage.py startapp "appname"
```

# Testing

```
 coverage run --source='.' manage.py test
 coverage html
  
```
# Install Selenium 

https://christopher.su/2015/selenium-chromedriver-ubuntu/

```
