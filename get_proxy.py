from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from bs4 import BeautifulSoup
import json

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    trs = soup.select("#proxylisttable tr")    
    #parser = fromstring(response.text)
    proxies = set()
    for tr in trs:
        tds=tr.select("td")
        if len(tds) > 6:
            ip = tds[0].text
            port = tds[1].text
            anonymity = tds[4].text
            ifScheme = tds[6].text
            if ifScheme == 'yes': 
                scheme = 'https'
            else: scheme = 'http'
            proxy = "%s://%s:%s"%(scheme, ip, port)
            meta = {
                    'port': port,
                    'proxy': proxy,
                    'dont_retry': True,
                    'download_timeout': 3,
                    '_proxy_scheme': scheme,
                    '_proxy_ip': ip
                    }
            proxies.add(proxy)
    # for i in parser.xpath('//tbody/tr')[:999]:
    #     if i.xpath('.//td[7][contains(text(),"yes")]'):
    #         proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
    #         proxies.add(proxy)
    return proxies


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
proxies = get_proxies()
proxy_pool = cycle(proxies)
print(proxies)

url = 'https://httpbin.org/ip'
for i in range(1,len(proxies)):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response['origin'].json())
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
        print("Skipping. Connnection error")