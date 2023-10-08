import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url,headers=headers)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")
name = soup.find_all("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-6fa21551-9 dKJKsK cli-title"})
rating = soup.find_all("span",{"class":"sc-6fa21551-1 GNFYN"})



a = float(input("Enter the IMDB value: "))

for baslik,puans in zip(name,rating):
    note = puans.text[0] + puans.text[1] + puans.text[2]
    if(float(note)>a):
        print("İsim: ",baslik.text)
        print("Reyting: ",puans.text[0]+puans.text[1]+puans.text[2])

