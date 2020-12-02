# Transcribe
This is a sample Django application with PostgreSQL database running on Docker for transcribing audio files.
User interface is simplified and created on top of django admin forms.
For every audio file user can enter textual transcription which is verified with validation rules. 

Here are the steps for running the project for the first time:

#####1. Build the project: 
```
docker-compose build
```
#####2. Run the migrations:
```
docker-compose run --rm web python manage.py migrate
```
#####3. Load initial data: 
```
docker-compose run --rm web python manage.py loaddata ./myapp/fixtures/init_data.json
```
#####4. Start the project: 
```
docker-compose -up
```
#####5. Open application
Open web browser on http://localhost:8000
and login with username: **root** and password **root**
