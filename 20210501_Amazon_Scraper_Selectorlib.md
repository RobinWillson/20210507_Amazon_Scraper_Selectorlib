# Amazon_Scraper_Selectorlib

This is a amazon scraper based on selectorlib python plugin.<BR>
Slim and easy modify.

## A00_Single Product page Scrape
Get datas from amazon single product page.<br>
You will see "/dp/" and ASIN number in the link, such as :<br>
<code>https://www.amazon.com/dp/B083KTYFCW/</code><br>
##### Pre-Setting
* Do <code>pip install selectorlib</code>
* Copy amazon product url into <code>A02_single_url_list.txt</code> file, format as below
> https://www.amazon.com/AmazonBasics-USB-C-Adapter-Thunderbolt-Compatible/dp/B083KTYFCW?ref_=Oct_DLandingS_D_eb6f7141_60&smid=ATVPDKIKX0DER<BR>
>https://www.amazon.com/Disposable-Breathable-Comfortable-Pollution-Protection/dp/B07P4DQDHJ/ref=gbps_img_m-9_475e_2b328fb6?smid=A2WFJ1LMWGTLQ5&pf_rd_p=5d86def2-ec10-4364-9008-8fbccf30475e&pf_rd_s=merchandised-search-9&pf_rd_t=101&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=WA3TNZA91GM89F6MDJS1
* Default output file is <code>A03_single_product_output.jsonl</code> file.<br>
For better orginize your resule, you canmodify <code>output_filename</code> as your wish in <code>A00_amz_single_product.py</code> file

##### Usage
* <code>python A00_amz_single_product.py</code>

##### Config
* in <code>A01_single_selectors.yml</code>, you can modify items you want to scrape
* install Selectorlib in Chrome Extension Store, you can get your <code>A01_single_selectors.yml</code> by just mouse click! Read the manual of the extension for more detail usage.
* use [Ditto](https://ditto-cp.sourceforge.io/) clipboard tool, you can get url_list easily.

## B00_Search Product Page Scrape
Get datas from amazon search product page.<br>
You can see "?k=" in the link, such as :<br>
<code>https://www.amazon.com/s?k=seat+cushion</code><br>

##### Pre-Setting
* Do <code>pip install selectorlib</code>
* Copy amazon search url into <code>B02_search_list.txt</code> file, format as below
>https://www.amazon.com/s?k=thanksgiving<BR>
>https://www.amazon.com/s?k=thanksgiving&page=2<BR>
>https://www.amazon.com/s?k=thanksgiving&page=3<BR>
* Default output file is <code>B03_search_output.jsonl</code> file.<br>
For better orginize your resule, you canmodify <code>output_filename</code> as your wish in <code>B00_amz_searcht_results.py</code> file

##### Usage
* <code>python B00_amz_searcht_results.py</code>

##### Config
* in <code>B01_search_selectors.yml</code>, you can modify items you want to scrape
* install Selectorlib in Chrome Extension Store, you can get your <code>B01_search_selectors.yml</code> by just mouse click! Read the manual of the extension for more detail usage.
* use [Ditto](https://ditto-cp.sourceforge.io/) clipboard tool, you can get url_list easily.

## Advanced use
* As amazon always ban your action if you scrape too much, B00_amz_searcht_results has some basic setup to avoid the ban.
* <code>'user-agent' : ua.random</code> this code fake you access website by random browser.
* <code>proxies={...}</code> here you can input proxies for better fake access.
* You can get proxies by <code>get_proxy.py</code>