from bs4 import BeautifulSoup
import requests

counter=1

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' }
response = requests.get("https://www.art.com/",headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

result = soup.find_all("div",attrs={"class":"hero-panel-group carousel-item-wrapper"})
categ=[]
for item in result:
    uu = 'https://www.art.com' + item.a['href']
    categ.append(uu)

subcateg=[]

for index in range(len(categ)):
    currentUrl=categ[index+7] + '&page={}'
    i = 1
    while(True):
        try:
            ul = currentUrl.format(i)
            response2 = requests.get(currentUrl,headers=headers)
            soup2 = BeautifulSoup(response2.content, "html.parser")
            result4 = soup2.find_all("div",attrs={"class":"product-container gtm_bestseller"})
            result3 = soup2.find_all("div",attrs={"class":"product-container"})
            result2=result3+result4
            result2 = list( dict.fromkeys(result2) )
            i+=1;
            if i>4:
                break
            print(i)
            for item in result2:
                uu = 'https://www.art.com' + item.a['href']
                subcateg.append(uu)
    
        
        except:
            break
    for j in range(len(subcateg)):
        response3 = requests.get(subcateg[j],headers=headers)
        soup3 = BeautifulSoup(response3.content, "html.parser")
        result5 = soup3.find_all("div",attrs={"class":"cart-upsell-offer-img"})
        result6 = soup3.find_all("h1",attrs={"class":"title-text"})
        if len(result5)>0:
            artName=''
            imag=''
            for item in result6:
                artName = item.text


            for item in result5:
                imag=item.img['src']
                
            imag=imag.replace("p=1","p=0")
            imag=imag+'&h=10000&w=10000'
            r=requests.get(imag,headers=headers)
            picName=artName +'.jpg'
            picName=picName.replace(':', '')   
            print(counter)
            counter+=1
            with open(picName, 'wb') as outfile:
                outfile.write(r.content)