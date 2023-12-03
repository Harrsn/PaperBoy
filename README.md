# PaperBoy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   <img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with Python"> <a href='https://github.com/harrsn' target='_blank'><img src='https://img.shields.io/github/followers/harrsn.svg?label=Follow&style=social'>
</a>

PaperBoy is a powerful content aggregator designed to efficiently collect content from various sources, organize it, and present it in one convenient location.

## Getting Started
Follow these step-by-step instructions to set up the project on your local machine for both development and testing purposes.

### Prerequisites

Ensure that you have [ **Python (> Python 3.10)**](https://www.python.org/) installed on your system.

### Getting the project.
Clone the repository using the following command:
```sh
$ git clone https://github.com/Harrsn/PaperBoy.git
```
Alternatively, you can download and extract the zip file.
### Setting up Virtual Environemt
Setting up a virtual environment is recommended for both development and normal execution purposes. Navigate to the project directory and run the following commands:
```sh
$ cd content_master
$ python -m virtualenv env
$ source env/bin/activate    #Linux/Unix
 or (Windows)
$ .\env\Scripts\activate
```
### Installing Dependencies
Install the project dependencies by running:
```sh
$ pip install -r dependencies.txt 
```
## Starting the Server
To start the Flask server, run the following command:
```sh
$ python server.py
```
A Flask development server will be initialized at http://127.0.0.1:5000/

### Warnings 

**WARNING: Do not use the development server in a production environment.**

This warning is displayed because currently a Flask Development Server is running, but the default environment of Flask is set to "Production". To remove this warning, change the FLASK_ENV environment variable.
<br>***Setting environment to development automatically sets the debugger on.**
```sh
$ export FLASK_ENV=development    #Linux/Unix
or (Windows)
$ set FLASK_ENV=development
```

## Errors and Debugging options
The server, by default, does not start in debugger mode. To enable debugger mode, modify the last line of the '[server.py](https://github.com/harrsn/paperboy/blob/main/server.py)' file:
```python
app.run() -> app.run(debug=True)
```
Most errors will be logged to the console and can be referenced later for debugging.
## Packages Used
- **[Requests](https://2.python-requests.org/en/master/)** : For fetching the source websites.
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** : For scraping the source websites.
- **[Flask](http://flask.pocoo.org/)** : For hosting the web interface.
