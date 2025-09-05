# how to install beautifulsoup4
# pip install bs4
# doc - https://www.crummy.com/software/BeautifulSoup/bs4/doc/


with open("formy_page.html", "r") as reader:
    content = reader.read()

# how to use bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# soup.prettify()  # formats the HTML content

soup.title  # gets the title tag
soup.title.name  # gets the title tag name
soup.title.text  # gets the title tag text

soup.find('a')  # finds the first anchor tag
soup.find('a')['href']  # gets the href attribute of the first anchor tag
soup.find_all('a')  # finds all anchor tags
soup.find_all('a')[0]['href']  # gets the href attribute of the first anchor tag from all anchor tags
print(soup.find_all('a')) 

for link in soup.find_all('a'):
    print("href =", link.get('href'))  # prints all href attributes of anchor tags

