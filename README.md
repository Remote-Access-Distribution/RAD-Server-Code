# RAD-Code
Only Windows installion guide is available for now, however this can be ran on other operating systems, but commands will differ.

Mac/Linux guides coming soon.
## Installation
Download and Extract this repository. It would be recommended to extract the files to your desktop

### Automatic install (Recommended)
#### Windows
Run `Setup.bat`.

Run through the python install ensuring you check add to path box and disable path length.
You will be prompted to create a superuser account, create a username and password. The email address field is optional.

### Manual Install
Firstly you will need to install python and mosquitto. Files have been provided for ease. Ensure when installing python you check add to path and disable path length.

Once both are installed open command prompt and run the following commands
#### Windows
``` bash
cd desktop/<folder>
python -m venv myenv
myenv\Scripts\activate.bat
pip install -r requirements.txt
```

In order to gain access the the \admin to edit and delete data you will need to create a superuser account. From the admin site you will be able to add additional users
``` bash
python manage.py createsuperuser
```

Now everything is installed to run the web server

## Start up
#### Windows:
`Startup.bat` will start the necessary components for the product to run.

## Shut down
### Windows:
Close the three Command Prompts that are open.

## Usage
Ensure you are connected to RAD-1 access point, password is 'testing123'
Open up a web browser e.g. Google Chrome
Navigate to 192.168.4.2:8000

In order to see a distro to control, you will need to navigate to the distros page using the navigation bar and add a new distro and define its location if required, once the server starts recieving data from the ESP32 then you will be able to control using the buttons.

## Future Development
Allow socket name to be named rather than just displaying 'Socket 1'
