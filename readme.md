Global Consumer using python kombu

This consumer can accept data in the from of 'json' from rabbitmq queue.
The Producer Consumer is connected using django-bindings

Steps:
1. Install requirements using command pip install -r requirements.txt
2. Go in djangoConsumer folder and run following commands to run migrations
    `python manage.py makemigrations`
    `python manage.py migrate`
3. python manage.py runserver will now start the django server
4. In another terminal from same folder as above run -> `celery -A demoproject.celery worker --loglevel=info --pool=solo` 
    it will start celery 
    mention it in config.py
6. you can run this curl command to add items in database. items with same name cannot be added it will produce 404 error.

curl --location --request POST 'localhost:8000/demoapp/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item": "pen"
}'

7. you can check queue list using `sudo rabbitmqctl list_queues` command 


Process:
1. Initially the item is added in the database with status = pending
2. after running the consumer the task is prossesed using celery. and database entry is updated.
