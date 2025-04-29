def main():
  url = input("URL della pagina di partenza")
  visited = []
  depth = 3
  crawl(url, depth, visited)
def crawl(url, depth, visited):
   if depth == 0:
     return
   response = urllib.request.urlopen(url)
   doc = bs4.BeatifulSoup(response)
   for link in doc.find_all("a"):
     href = link["href"]
     if href [0:4] == "http" and href not in visited:
       visited.append(href)
       crawl(href, visited)
 except return
main()
