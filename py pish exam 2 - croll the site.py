import requests
from bs4 import BeautifulSoup
# for i in range(1974776,1975776):
url = f"https://www.varzesh3.com/news/{1974776}"
res = requests.get(url).text
res_b = BeautifulSoup(res , "html.parser")
##################################################################
all_title = res_b.find("div" , class_ = "news-detail-text")

title = str(all_title.find("h1" , class_ = "headline")).replace('<h1 class="headline">' , '' ).replace("</h1>","")
# print("title : ",title)

view = int(str(all_title.find("div", class_ = "news-info")).split("<span>")[3].replace("| </span>","").replace(" بازدید", "").replace("K",""))*1000
# print("view : ",view)
####################################################################

all_tags = str(res_b.find("div", class_ = "tags tags-news")).replace('<div class="tags tags-news">\n<div class="tag">\n<a href="/tag/', "").replace('">',"").replace("<span>", "").replace("</span>","").replace("</a>\n","")

# tag = all_tags.find("div", class_ = "tag")

print(all_tags)

# i += 1