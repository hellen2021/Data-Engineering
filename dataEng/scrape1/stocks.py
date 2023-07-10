import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url ="https://uk.finance.yahoo.com/quote/ASPL.L"

r = requests.get(url)

#print(r.status_code)

soup = BeautifulSoup(r.text , 'html.parser')

#print(soup.title.text)

price = soup.find('fin-streamer', {'class':'D(ib) Va(m) Maw(65%) Ov(h)'})#.find_all('value')[0].text

#<fin-streamer class="Fw(b) Fz(36px) Mb(-4px) D(ib)" data-symbol="ASPL.L" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="4" value="0.13" active="">0.1300</fin-streamer>

print(price)
#<div class="D(ib) Va(m) Maw(65%) Ov(h)"><div class="D(ib) Mend(20px)"><fin-streamer class="Fw(b) Fz(36px) Mb(-4px) D(ib)" data-symbol="ASPL.L" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="4" value="0.13" active="">0.1300</fin-streamer><fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="ASPL.L" data-test="qsp-price-change" data-field="regularMarketChange" data-trend="txt" data-pricehint="4" value="0.014999993" active=""><span class="C($positiveColor)">+0.0150</span></fin-streamer> <fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="ASPL.L" data-field="regularMarketChangePercent" data-trend="txt" data-pricehint="4" data-template="({fmt})" value="0.1304347" active=""><span class="C($positiveColor)">(+13.04%)</span></fin-streamer><fin-streamer class="D(n)" data-symbol="ASPL.L" changeev="regularTimeChange" data-field="regularMarketTime" data-trend="none" value="" active="true"></fin-streamer><fin-streamer class="D(n)" data-symbol="ASPL.L" changeev="marketState" data-field="marketState" data-trend="none" value="" active="true"></fin-streamer><div id="quote-market-notice" class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)"><span>As of 30 June 03:53PM BST. Market open.</span></div></div></div>