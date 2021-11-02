from bs4 import BeautifulSoup
import requests


url = requests.get("https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d").text

soup = BeautifulSoup(url, 'lxml')

webpage_name = soup.title.string
print(webpage_name)


# print(soup.prettify())

ordered_list = soup.find('ol')
quotes_list = ordered_list.find_all('li')
# print(quotes_list)
qoutes = []

for ql in quotes_list:
    quote = ql.text
    final_quote = quote[:-8]
    qoutes.append(final_quote)


with open ("Quotes.txt", "w") as wf:
    for i,q in enumerate(qoutes, 1):
        wf.write(str(i)+ ") " + q.strip())
        wf.write("\n")



