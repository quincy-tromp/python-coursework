from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify()) 

print(soup.a) # To find the first anchor tag
all_anchor_tags = soup.find_all(name="a") # To find all anchor tags. Returns a list 
print(all_anchor_tags)

# How to get a hold of string inside all anchor tags? Use for loop and getText()
for tag in all_anchor_tags: 
    print(tag.getText()) 
    # How to get the link inside anchor tag?
    print(tag.get("href")) # You can use get() to get the value of any of the attributes ("href" in this case)

heading = soup.find(name="h1", id="name") # Use find() to find the first item that matches the query
print(heading)

# To find target a html class with the find() method, use class_=""
section_heading = soup.find(name="h3", class_="heading") # Notice the underscore after class
print(section_heading.string)
print(section_heading.getText())

# Use select() to get all the tags specified, with CSS selector syntax
# Use select_one() to select a specific tag, with CSS selector syntax
company_url = soup.select_one(selector="p a") # selector="p a" here means select the a tag inside the p tag. Can also leave selector out and just type "p a" 
print(company_url)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])