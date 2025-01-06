# road_accidents
A simple Django web app

On terminal enter the command line: python manage.py runserver 127.0.0.1:8080
GET http://127.0.0.1:8080/  -Go to the main page
GET http://127.0.0.1:8080/accidents/ -Go to the page that browse the app and enter new data
POST http://127.0.0.1:8080/accidents/ -Add new data to the page
OPTIONS http://127.0.0.1:8080/accidents/ -Browse the detail of the entered data

Consider the price may occur when using Heroku to deploy the web app, the project is not 
host on the Heroku currently. To deploy the app, follow the instruction using command line below: 
1. On terminal, install the Heroku: brew tap heroku/brew && brew install heroku
2. login to the Heroku account: heroku login
3. Create and deploy the app: heroku create
