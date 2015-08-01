# identity-toolkit-django
Demonstrates how to access the Identity Toolkit API with Django

## Command Line Tool
The script `gitkit_command_tool.py` is a useful CLI for interacting with 
Identity Toolkit while debugging your application.  You can easily get 
information on registered users and delete users so that you can test
onboarding flows repeatedly.

## Setup

### Dependencies
First, install the python dependencies by running:

    pip install -r requirements.txt

### Credentials

1) Follow the [Google Identity Toolkit](https://developers.google.com/identity/toolkit/web/v2/devconsole) instructions to generate credentials and download the necessary files from identity toolkit console.  

2) Next, you will need to download a p12 key for your service account by clicking
the **Generate new P12 key** in the Developers Console.  Once downloaded,
move it to this folder and rename it `private-key.p12`.

3) Next, the following fields from the downloaded `gitkit-server-config.json` should already be configured:

  * `clientId` - the client ID for your web application.
  * `serviceAccountEmail` - the email address listed for your service account.
  If your project does not have a service account, you will need to create one.
  * `serviceAccountPrivateKeyFile` - Supply `private-key.p12` or the name of the *.p12 file you downloaded from the Developers Console.  
  _Note: Running `gitkit_command_tool.py` may warn you to convert `private-key.p12` to `private-key.pem`._
  * `widgetUrl` - Should be the full path url (including host:port) mapped to `identity/widget` in this project. 

4) Finally create `identity/widget_config.json` with the following:
  ```json
  {
    "apiKey": "AIza..."
  }
  ```
  
  `apiKey` - Should match the apiKey found from the `gitkit-widget.html` file downloaded from the Google Identity Toolkit Developers Console.

## gitkit_command_tool.py Usage
Run the script by invoking `python gitkit_command_tool.py`:

    usage: gitkit_command_tool.py [-h] [--id [ID]] [--email [EMAIL]] command

    positional arguments:
      command          one of: get, list, insert, delete

    optional arguments:
      -h, --help       show this help message and exit
      --id [ID]        id of the user
      --email [EMAIL]  email of the user

## Run

  ./gitkit_command_tool.py insert

  ./manage.py runserver

  Open [http://localhost:8000/](http://localhost:8000/)