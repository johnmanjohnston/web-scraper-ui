# web-scraper-ui

## About
A tool that gets results from the web, matching a query using [Zenserp](https://zenserp.com/).
The results are retrieved, then on a HTML page they are formatted and displayed.
As a framework for the backend code, [Django](https://www.djangoproject.com/) is used.

## Use Instructions
+ Get Python. (ns)
+ Clone this repository
+ Install Django (`pip3 install django`)
+ In the `scraper` app directory, create a `.env` file and create a variable `ZENSERP_KEY` and set its value to your Zenserp key
+ Run the server (`python3 manage.py runserver`)
