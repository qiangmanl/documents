import asyncio
from werkzeug.local import Local
from pyppeteer import launch
import pyppeteer
import os
local = Local()
current_url = local("current_url")
page = local("page")
task_urls = local("task_urls")
symbols = local("symbols")
local.symbols = []



local.current_url =''
local.page = None
local.task_urls = dict()
local.task_urls["symbol_list_url"] = "https://data.binance.vision/?prefix=data/spot/monthly/klines/"
local.task_urls["symbol_data_link_pattern"] = "https://data.binance.vision/data/spot/monthly/klines/%s/1m"


def get_months_in_year(year, start, end):
    months = []
    for month in range(start, end+1):
        if month < 10:
            month = f'0{str(month)}'
        months.append(str(month))
    return year, months


def get_filter_symbol(symbol,has_word="USDT"):
    if symbol[-5:-1] == has_word:
        symbol =  symbol[:-1]
        return symbol
    return


def system_call_wget(url):
    call = os.popen(f'wget {url}',"r",1)
    if not call.close():
        return True
    return

def download_data():
    year, month = get_months_in_year(2023,1,11)
    url_pattern = local.task_urls["symbol_data_link_pattern"]
    for symbol in local.symbols:
        for i in month:
            url = f'{url_pattern%symbol}/{symbol}-1m-{year}-{i}.zip'
            if system_call_wget(url):
               print(url) 


async def get_href_from_element(element):
    href = await element.getProperty('href')
    href = await href.jsonValue()
    text = await element.getProperty('textContent')
    text = await text.jsonValue()
    return href, text

async def waiting_url_done(url,wait_time=20):
    await local.page.goto(url,{"waitUntil": 'networkidle2'})
    while True:
        if wait_time == 0:
            break
        await asyncio.sleep(0.1)
        wait_time -= 1
        if local.page.url == url:
            local.current_url = url
            return True
    return 

async def get_symbols():
    i = 0
    while True:
        symbol_xpath =f'/html/body/div/table/tbody/tr[{i}]/td[1]/a'
        try:
            element = await local.page.waitForXPath(symbol_xpath,{"timeout": 1000})
        except pyppeteer.errors.TimeoutError:
            element = None
        i += 1
        if element:
            _, text = await get_href_from_element(element)
            text = get_filter_symbol(text)
            if text:
                local.symbols.append(text)
        else:
            continue
        if i == 2389:
            break
async def wait_page_init():
    browser = await launch(headless=True, userDataDir="user-data", args=["--disable-infobars","--no-sandbox"])
    context = await browser.createIncognitoBrowserContext()
    local.page = await context.newPage()
    await local.page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    return True

async def main():
    await wait_page_init()
    if await waiting_url_done(local.task_urls["symbol_list_url"]):

        await get_symbols()
    download_data()
    input("end?")


asyncio.get_event_loop().run_until_complete(main())

