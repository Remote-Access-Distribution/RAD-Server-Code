# RAD-Code
Only Windows installion guide is available for now, however this can be ran on other operating systems, but commands will differ.

Mac/Linux guides coming soon.
## Installation
Download and Extract this repository. It would be recommended to extract the files to your desktop

### Automatic install (Recommended)
#### Windows
Run `Setup.bat`.

Run through the python install ensuring you check add to path box and disable path length.

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
Now everything is installed to run the web server

## Start up
In order to start the server, there is a specific order to run everything otherwise there will be errors

#### Windows:
Firstly you will need to run the Mosquitto MQTT broker, this can be done by running `Start_Mosquitto.bat` as administrator.

After that you can run `Startup.bat` which will start the necessary components for the product to run.

## Shut down
### Windows:
Close the two Command Prompts open.