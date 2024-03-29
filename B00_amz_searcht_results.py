from selectorlib import Extractor
import requests 
import json 
from time import sleep
from fake_useragent import UserAgent
from proxy_requests import ProxyRequests, ProxyRequestsBasicAuth

Preset_yml_filename = "B01_search_selectors.yml"
Input_filename = "B02_search_list.txt"
Output_filename = "B03_search_output.jsonl"

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file(Preset_yml_filename)
ua = UserAgent()

def scrape(url):  

    proxies={
        # 'https':'https://169.57.1.84:8123',
        # 'http':'http://31.192.107.162:3128'
    }

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'user-agent' : ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers, proxies=proxies)
    # r=ProxyRequests(url)
    # r.set_headers(headers)
    # r.get_with_headers()
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

# product_data = []
with open(Input_filename,'r') as urllist, open(Output_filename,'w') as outfile:
    for url in urllist.read().splitlines():
        data = scrape(url) 
        if data:
            for product in data['products']:
                product['search_url'] = url
                print("Saving Product: %s"%product['title'])
                json.dump(product,outfile)
                outfile.write("\n")
                # sleep(5)