cd Installers\
python-3.11.0-amd64.exe
mosquitto-2.0.15-install-windows-x64.exe

cd..
python -m venv myenv
myenv\Scripts\python.exe -m pip install --upgrade pip
myenv\Scripts\pip.exe install -r requirements.txt

cd django_app\
..\myenv\Scripts\python.exe manage.py createsuperuser