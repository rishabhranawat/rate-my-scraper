import urllib
from bs4 import BeautifulSoup

url = "https://www.ratemyprofessors.com/search.jsp?query=Chee+Yap"
html_doc = urllib.urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')
search_url = "http://www.ratemyprofessors.com/"

for link in soup.find_all("a"):
	val = link.get("href")
	if val and ("/ShowRatings.jsp?") in val:
		search_url += val
		break

next_page = urllib.urlopen(search_url).read()
soup2 = BeautifulSoup(next_page, 'html.parser')
grade = soup2.findAll("div", {"class":"grade"})[0]
print(grade.text)
