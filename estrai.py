import urllib.request
import math
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")
import bs4
doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag :
        tds = tr.contents
        sequ = int(tds[0].get_text())
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".",""))
        sigl = tds[7].get_text()
        kmq = int(tds[4].get_text().replace(".",""))
        denso = float(tds[5].get_text().replace(".","").replace(",","."))
        densc = math.floor(10 * resi / kmq) / 10
        #densc = round(resi / kmq, 1)
        if denso != densc:
            print(f"{sigl} {prov:25s} {resi:9d} {kmq} {denso:5} {densc:5}")
