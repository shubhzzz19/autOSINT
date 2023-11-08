# AutOSINT

# About

## TODO

- api/lookup.py: returning a string, should return json. that json can then be converted to a dictionary to allow for accessing key:value pairs to be displayed in the results window

- check http code in api response, if something gone wrong, write to logfile but dont display in results window

- implement logging with logging package

- add validation: if all fields are empty, show a blocking popup with an error. one or more can be empty, but not all. create a commit with a descriptive message and push. **when any field is empty, don't send a request to the api endpoint**

✅ - protect api keys. moving api keys into hidden files and moving out of repository ✅

- parse api response and display results in the results window in human-readable format(like the text in the image below)

- display results in dedicated results window

- add more apis

- add PPT etc. files to repo so that they are version controlled too

- cosmetic changes-change theme, font, placement of elements

## Installation and Setup

Clone this repository. 

```
$ pip -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
