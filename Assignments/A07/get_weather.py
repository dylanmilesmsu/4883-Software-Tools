"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function

from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager
from gui import buildWeatherURL
from table import openTable
import pprint


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 5 seconds for dynamic data to load...")
        time.sleep(5)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML
    
def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    url = buildWeatherURL()
    print(url)

    # get the page source HTML from the URL
    page = asyncGetWeather(url)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    history = soup.find('lib-city-history-observation')
    soup.contents
    table = history.findAll("table")
    # print the parsed HTML
    tableImInterestedIn = table[0]
    if 'daily' in url:
        lists = []
        for row in tableImInterestedIn.findAll("tr"):
            tempList = []
            for item in row.findAll("td"):
                 print(item.text)
                 tempList.append(item.text)
            if len(tempList) > 0:
                lists.append(tempList)
                print("--------")
        print(lists)
        openTable(lists, True)
        
    else:
        lists = []
        skip = 0;
        for row in tableImInterestedIn.findAll("tr"):
            if skip > 1:
                tempList = []
                for item in row.findAll("td"):
                    print(item.text)
                    tempList.append(item.text)
                lists.append(tempList)
                print("--------")
            skip += 1
        print(lists)

        table = []
        tempTable = []
        i = 0;
        for data in lists:
            if 'Max' in data[0] or 'Total' in data[0]:
                table.append(tempTable)
                tempTable = []
                fullText = ""
                for text in data:
                    fullText += text + " "
                tempTable.append(fullText.strip())
            else:
                fullText = ""
                for text in data:
                    fullText += text + " "
                tempTable.append(fullText.strip())
        table.append(tempTable)
        
        # print(table)
        openTable(table, False)