import urllib3
import json
from bs4 import BeautifulSoup
import re

header_raw = """
!! PASTE YOUR HEADER HERE (COPY RAW HEADER FROM FIREFOX) !!
"""

headers = dict([line.split(": ", 1) for line in header_raw.strip().split("\n")])

url = "https://www.bilinovel.com/novel/2597/catalog"
base_url = "https://www.bilinovel.com"

http = urllib3.PoolManager()
response = http.request("GET", url)
soup = BeautifulSoup(response.data, "html.parser")


# fetch all links in the url:
links = []
for a in soup.find_all("a", href=True):
    if re.search(r"\d+/\d+.html", a["href"]):
        links.append(base_url + a["href"])

# fetch all chapters
jpg_links = []
for link in links:
    response = http.request("GET", link, headers=headers)
    # r"https://img3.readpai.com/2/\d+/\d+/\d+.jpg":
    # print(response.data.decode("utf-8"))
    jpg_links += re.findall(
        r"https://img3.readpai.com/2/\d+/\d+/\d+\.jpg", response.data.decode("utf-8")
    )
    # print(jpg_links)

print(len(jpg_links))

# dump to json:
with open("data.json", "w") as f:
    json.dump(jpg_links, f)
