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

all_tags = str(res_b.find("div", class_ = "tags tags-news").find_all("span")).replace("<span>","").replace("</span>","").replace("[","").replace("]","")
print("tags for this news: ",all_tags)
