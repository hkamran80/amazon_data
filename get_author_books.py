#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests

r_headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'}

url = input("Author URL (Amazon): ")
parsed = bs(requests.get(url, headers=r_headers).text, "html.parser")
free_books = []

count = 0

author = parsed.find("div", attrs={"id":"ap-author-name"}).find("h1").string

print("")

for b in parsed.find("ul", attrs={"class":"s-result-list"}).find_all("li"):
	title = parsed.find("ul", attrs={"class":"s-result-list"}).find_all("li")[count].find("h2", attrs={"class":"a-size-medium"}).string
	price = parsed.find("ul", attrs={"class":"s-result-list"}).find_all("li")[count].find("span", attrs={"class":"a-offscreen"}).string

	print(title)
	print(author)
	print(price)
	print("")

	if price == "$0.00":
		free_books.append([title, author, price, parsed.find("ul", attrs={"class":"s-result-list"}).find_all("li")[0].find("a", attrs={"class":"a-link-normal"})["href"]])

	count = count + 1

if len(free_books) > 0:
	print(free_books)
