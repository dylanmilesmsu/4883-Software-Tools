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
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page... If ads decide to load its probably going to be slow")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 5 seconds for dynamic data to load...")
        time.sleep(5)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML

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
    #only the first table has the stuff i want
    tableImInterestedIn = table[0]
    if 'daily' in url:
        lists = []
        for row in tableImInterestedIn.findAll("tr"):
            tempList = []
            for item in row.findAll("td"):
                #go through all the items and add them to a temporary list
                 #print(item.text)
                 tempList.append(item.text)
            #check if theres actual content... for some reason theres blanks
            if len(tempList) > 0:
                #then add those temp lists to the main list
                #this way we have a list of lists for the table
                lists.append(tempList)
                #print("--------")
        # print(lists)
        openTable(lists, True)
        
    #most of the code is the same for the weekly/monthly,
    #ill make notes of the different parts
    else:
        lists = []
        skip = 0;
        for row in tableImInterestedIn.findAll("tr"):
            #the first tow is junk so throw away
            if skip > 1:
                tempList = []
                for item in row.findAll("td"):
                    #print(item.text)
                    tempList.append(item.text)
                lists.append(tempList)
                #print("--------")
            skip += 1
        #print(lists)
        #after its done, everything is in one list
        # but we need to differentiate them into multiple
        # the max avg min serves as an indicator to know when to split it
        # or 'total' in the case of the last one 
        table = []
        tempTable = []
        i = 0;
        for data in lists:
            if 'Max' in data[0] or 'Total' in data[0]:
                #this is our flag for a new column
                #we still wanna add the 'max avg min'
                #to the start of the next column
                table.append(tempTable)
                #clear temp table
                tempTable = []
                fullText = ""
                for text in data:
                    fullText += text + " "
                tempTable.append(fullText.strip())
            else:
                #instead of 'Max', 'Avg', 'Min'
                #we want 'Max Avg Min'
                fullText = ""
                for text in data:
                    fullText += text + " "
                #add to tempList
                tempTable.append(fullText.strip())
        #add tempList to main list `table`
        table.append(tempTable)
        
        # print(table)
        openTable(table, False)