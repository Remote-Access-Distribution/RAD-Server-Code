
start "" "C:\Program Files\mosquitto\mosquitto.exe" -v -c mosquitto.conf
cd django_app
start ..\myenv\Scripts\python.exe manage.py runserver 0.0.0.0:8000
start ..\myenv\Scripts\python.exe manage.py mqtt_subscribe --broker localhost #