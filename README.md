# celery_sample

simple flask app with celery

`docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management`


**default management creds:**

username: guest

password: guest

`celery -A celery_worker worker --loglevel=INFO --purge --pool=solo`

**Postgress**

https://hub.docker.com/_/postgres/

`docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

**Migrations**

`alembic init alembic`

`alembic revision -m "first" --autogenerate`

`alembic upgrade head`

**Links**

https://www.psycopg.org/

https://docs.sqlalchemy.org/en/14/core/engines.html

https://stackoverflow.com/questions/43477244/how-to-find-postgresql-uri-for-sqlalchemy-config

https://docs.sqlalchemy.org/en/14/tutorial/engine.html

https://flask.palletsprojects.com/en/2.2.x/patterns/sqlalchemy/

https://alembic.sqlalchemy.org/en/latest/tutorial.html

**Sessions**

https://flask.palletsprojects.com/en/2.2.x/quickstart/#sessions

https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/

https://flask-session.readthedocs.io/en/latest/

https://testdriven.io/blog/flask-sessions/

https://pythonbasics.org/flask-sessions/

https://www.educba.com/flask-session/
