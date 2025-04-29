import urllib.request
url = "https://www.chiesaevangelicapesaro.org/wp/"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
import bs4
doc = bs4.BeautifulSoup(text)
print(doc.prettify())
