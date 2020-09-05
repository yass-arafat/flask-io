# flask-io

This is a simple flask-restful project with sqlite/postgresql database. This project is created using cookiecutter(https://github.com/karec/cookiecutter-flask-restful) template.

# Branch flask-sqlite
- used uwsgi as wsgi server
- python 3.7
- no celery
- admin username, mail, password : yassir, yassir@admin.com, yassir

### How to run
- Go to root directory and try ```make init``` or ```docker-compose up -d --build```
- Then ```make run```. Check server is running or not ```docker-compose ps``` 
- Then try in browser ```http://localhost:5000/swagger-uihttp://localhost:5000/swagger-ui``` as we have exposed in port 5000, you should see the swagger.
