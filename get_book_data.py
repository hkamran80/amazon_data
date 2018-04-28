#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests

r_headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}

url = input("Book URL (Amazon): ")
parsed = bs(requests.get(url, headers=r_headers).text, "html.parser")

title = parsed.find("span", attrs={"id":"ebooksProductTitle"}).string

if len(parsed.find("span", attrs={"class":"author"}).find("a", attrs={"class":"a-link-normal"}).string.split(" ")) > 2:
	author = parsed.find("span", attrs={"class":"author"}).find("a", attrs={"class":"a-link-normal"}).string.split(" ")[2] + " " + parsed.find("span", attrs={"class":"author"}).find("a", attrs={"class":"a-link-normal"}).string.split(" ")[3]
else:
	author = parsed.find("span", attrs={"class":"author"}).find("a", attrs={"class":"a-link-normal"}).string

try:
	price = str(parsed.find("td", attrs={"class":"a-color-price"})).replace("\n", "").replace(" ", "").split(">")[1].split("<")[0]
except TypeError:
	price = parsed.find("td", attrs={"class":"a-color-base a-align-bottom a-text-strike"}).string.strip()

print("")

print("Title: {}".format(title))
print("Author: {}".format(author))
print("Price: {}".format(price))
