# MLS Team Web Scraper

## A web application to view stats for very MLS team. Built with FastAPI, BeautifulSoup, React, and Tailwind.

This was a 2 week long project during my summer semester. This project was inspired by a similar school project where we were asked to web scrape online retail stores, store the product information (price, image, name, reviews) into a database, and display it using html and css.

For this project I wanted to apply what I learn using new languages and frameworks, such as:

* FBREF for data collection.
* Python and Beautiful soup for webscraping the relavent team data.
* Supabase for storage.
* FastAPI to facilitate information retrieval from database.
* React and Tailwind for displaying the information.
* Heroku for hosting.

## Project Demo

## Project Setup

```
|-backend ------------- contains fastapi apis and templates for rendering
|
|-data ---------------- contains txt files with links to data
|   |-teams.txt
|
|-frontend ------------ contains react react project files
|
|-scripts ------------- contains script for downloading team stats daily
```

## How to Install