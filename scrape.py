#This file contains the functions associated with gathering data from designated movie sites


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def get_url():
    mov_title = str(input())

def cook_url():
    return True

def scrape_info(url, params = []):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title