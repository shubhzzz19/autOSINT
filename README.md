# AutOSINT

# About

## TODO

- align all field text ("host: ", "domain: ", etc.)

- fix main screen description code, use an element that can align a paragraph within given bounds

- put label above textboxes saying that you can leave one or more fields blank

- api/lookup.py: returning a string, should return json. that json can then be converted to a dictionary to allow for accessing key:value pairs to be displayed in the results window

- check http code in api response, if something gone wrong, write to logfile but dont display in results window

- implement logging with logging package

- **check that when any field is empty, its not sending a request to the api endpoint**

- parse api response and display results in the results window in human-readable format(like the text in the image below)

- display results in dedicated results window

- add more apis

- add PPT etc. files to repo so that they are version controlled too

- cosmetic changes-change theme, font, placement of elements

## Installation and Setup

You will need `git` to clone this repository(alternatively download an archive of this repository), `pip` to install required packages, `python venv` for the virtual environment

You can install them on ubuntu linux systems by running

```
$ sudo apt install -y git python3-pip python3-venv python3-tk
```

Clone the repository with

```
$ git clone https://github.com/shubhzzz19/autOSINT.git
```

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run the program with 
```
python3 /path/to/main.py
```
Make sure that the virtual environment is activated.
