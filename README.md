## URL Shortener/Redirect Flask App

This is a simple Flask app that allows users to create short/dynamic URLs that redirect to a specified URL.

### Features

-   Create short URLs that redirect to a long URL
-   In case you want to hardcode a URL somewhere, you can use this and change it dynamically from `redirects`. 

### Setup

To run locally:
1.  Install Flask: `pip install flask`
2.  Clone this repository: `git clone https://github.com/swatishchoudhury/urlredirect`
3.  Run the app: `python urlredirect.py`

### Usage

To create a short or dynamic URL, edit the `redirects` file and add a new line in the format `short_url long_url`.


##
This project was inspired by [cass.run](https://github.com/cassidoo/cass.run) by Cassidy Williams. 
