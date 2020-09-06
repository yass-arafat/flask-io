# flask-io

This is a simple flask-restful project with sqlite/postgresql database. This project is created using cookiecutter(https://github.com/karec/cookiecutter-flask-restful) template.


# Branch flask-postgresql
- used uwsgi as wsgi server
- python 3.7
- no celery
- admin username, mail, password : yarafat, yarafat@admin.com, yarafat
- admin dashboard added with ```pip install flask-admin``` because flask have no default admin panel like Django

### How to run
- Go to root directory and try ```make init``` or ```docker-compose up -d --build```
  If you face any problem running ``make init`` and got error like this `ERROR [root] Error: Can't locate revision identified by 'faf3ebfbe667'` then
  just delete the table `alembic_versions` and run `make init` again
- Then ```make run```. Check server is running or not ```docker-compose ps``` 
- Then try in browser ```http://localhost:5000/swagger-ui``` as we have exposed in port 5000, you should see the swagger.
- Admin url ```http://localhost:5000/admin/user/```
