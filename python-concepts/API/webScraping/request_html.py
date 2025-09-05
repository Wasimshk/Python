# how to install
# pip install requests-html
# doc - https://requests.readthedocs.io/projects/requests-html/en/latest/

from requests_html import HTMLSession
# from lxml.html.clean import Cleaner # optional
session = HTMLSession()

response = session.get("https://formy-project.herokuapp.com/")

print(response.html.links)  # prints all the links in the page
print(response.html.absolute_links)  # prints all the absolute links in the page        
print(response.html.url)  # prints the URL of the page
print(response.html.find('#about', first=True))  # prints the status code of the page
print(response.html.find('a'))  # prints all the anchor tags in the page
print(response.html.find('a')[5].text)  # prints the text of the first

print(response.html.find('.btn-lg'))  # prints all the elements with class 'btn-lg'