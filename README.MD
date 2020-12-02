# Transcribe
This is a sample application Django application with PostgreSQL database for transcribing audio files.

Here are the steps for running the project for the first time:

#####1. Build the project: 
```
docker-compose build
```
#####2. Create the migrations: 
```
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py makemigrations myapp
```
#####3. Run the migrations:
```
docker-compose run --rm web python manage.py migrate
```
#####4. Create superuser: 
```
docker-compose run --rm web python manage.py createsuperuser
```
#####5. Start the project: 
```
docker-compose -up
```
