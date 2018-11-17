import bs4 as bs
import urllib.request

sauce=urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(sauce,'lxml')

print("Title: {}".format(soup.title))
print("Title Name: {}".format(soup.title.name))
print("Title String: {}".format(soup.title.string))
print("Paragraph: {}".format(soup.p))
print("-------------------------------------\n-------------------------------------")
print("Paragraph: {}".format(soup.p))

print("-------------------------------------\n-------------------------------------")
print("Read entire file\n\n {}".format(sauce))
