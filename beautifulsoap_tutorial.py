#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://parade.com/937586/parade/life-quotes/"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
titles = soup.find_all('p')