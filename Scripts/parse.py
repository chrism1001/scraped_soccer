import requests
from bs4 import BeautifulSoup
import os


with open("./Data/teams.txt", "r") as file:
    for url in file:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")