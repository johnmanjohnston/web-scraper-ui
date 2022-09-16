# web-scraper-ui

## About
A tool that gets results from the web, matching a query using [Zenserp](https://zenserp.com/).
The results are retrieved, then on a HTML page they are formatted and displayed.
As a framework for the backend code, [Django](https://www.djangoproject.com/) is used.

## Installation
+ Get Python. (no frickin crap sherlock)
+ Clone this repository
+ Install Django (if you have pip, you may use `pip3 install django`)
+ In the `scraper` app directory, create a `.env` file and create a variable `ZENSERP_KEY` and set its value to your Zenserp key
+ Run the server (`python3 manage.py runserver`)

If everything works successfully, you should see something resembling the following at the home route of the application

Now you can explore the internet. Want to know what the internet can do? Listen to [Welcome to the Internet](https://www.youtube.com/watch?v=k1BneeJTDcU) by Bo Burnham to find out!

![image](https://user-images.githubusercontent.com/97091148/187571096-2beeb106-081b-40be-a38a-e774d9485d1e.png)

## Explanation
If it's the home route, then the home page is rendered. The home page has a form which sends a `GET` request to the search page.

When a request to the search route is detected, `search_page()` in `views.py` is called, and a request is sent to Zenserp to get the search results using the query passed along with the request from the home page. If no query is detected, the user is redirected to the home route.
