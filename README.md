# celery_sample

simple flask app with celery

`docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management`


**default management creds:**

username: guest

password: guest

`celery -A celery_worker worker --loglevel=INFO --purge --pool=solo`