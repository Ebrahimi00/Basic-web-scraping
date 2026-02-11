from urllib.request import urlopen 
from bs4 import BeautifulSoup 
from urllib.parse import urlparse

# بارگذاری صفحه وب
url = urlopen('https://www.bishtarazyek.com/%D8%AA%D9%85%D8%B1%DB%8C%D9%86%D8%A7%D8%AA-%D9%81%D9%86-%D8%A8%DB%8C%D8%A7%D9%86/#deny')   
bs = BeautifulSoup(url, 'html.parser')

def getInternalLinks(bs, pageUrl):     
    netloc = urlparse(pageUrl).netloc     
    scheme = urlparse(pageUrl).scheme     
    internalLinks = set()     
    
    for link in bs.find_all('a'):         
        if not link.attrs.get('href'):             
            continue   
        
        parsed = urlparse(link.attrs['href'])                
        
        if parsed.netloc == '':   
            # لینک نسبی
            l = f'{scheme}://{netloc}/{link.attrs["href"].strip("/")}'    
            internalLinks.add(l)            
        elif parsed.netloc == netloc:   
            # لینک داخلی
            internalLinks.add(link.attrs['href'])         
    
    return list(internalLinks)

# دریافت و چاپ لینک‌های داخلی
links = getInternalLinks(bs, 'https://www.bishtarazyek.com/')
for link in links:
    print(link)