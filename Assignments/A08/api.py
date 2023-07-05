
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn
import csv



description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
# populates the `db` list with all the csv data
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

def getTotalDeathsByCountry(country):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if country.lower() == row[2].lower():
            if int(row[7]) > deathTotal:
                deathTotal = int(row[7])
    return deathTotal

def getTotalDeathsByCountry_timeframe(country, minDate, maxDate):
    global db
    deathTotal = 0
    for row in db:
        date = row[0]
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]
        dateT = datetime(int(year), int(month), int(day))
        #print(minDate)
        #print(dateT)
        #print(maxDate)
        inDate = maxDate >= dateT >= minDate
        if inDate and country.lower() == row[2].lower():
            if int(row[7]) > deathTotal:
                deathTotal = int(row[7])
    return deathTotal

def getTotalDeathsByRegion(region):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if region.lower() == row[3].lower():
            deathTotal += int(row[6])
    return deathTotal

def getTotalDeathsByCountryYear(country, year):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if country.lower() == row[2].lower():
            if year == int(row[0][:4]):
                deathTotal += int(row[6])
    return deathTotal

def getTotalDeathsByRegionYear(region, year):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if year == int(row[0][:4]) and region.lower() == row[3].lower():
            deathTotal += int(row[6])
    return deathTotal


def getTotalCasesByCountry(country):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if country.lower() == row[2].lower():
            if int(row[5]) > deathTotal:
                deathTotal = int(row[5])
    return deathTotal

def getTotalCasesByRegion(region):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if region.lower() == row[3].lower():
            deathTotal += int(row[4])
    return deathTotal

def getTotalCasesByCountryYear(country, year):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if country.lower() == row[2].lower():
            if year == int(row[0][:4]):
                deathTotal += int(row[4])
    return deathTotal

def getTotalCasesByRegionYear(region, year):
    global db
    deathTotal = 0
    for row in db:
        print(row)
        if year == int(row[0][:4]) and region.lower() == row[3].lower():
            deathTotal += int(row[4])
    return deathTotal

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():
    """
    Returns a list of all countries
    - **Params:**
      - None
    - **Returns:**
      - list (str) : All countries

    #### Example 1:

    [http://127.0.0.1:5000/countries/](http://127.0.0.1:5000/countries/)

    #### Response 1:
     {
  "countries": [
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
        ......
        ]
    }
    """
    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():
    """
    Returns all WHOS region codes
    - **Params:**
      - None
    - **Returns:**
      - (str) : All region codes

    #### Example 1:

    [http://127.0.0.1:5000/whos/](http://127.0.0.1:5000/whos/)

    #### Response 1:
    {
    "whos": [
        "EMRO",
        "EURO",
        "AFRO",
        "WPRO",
        "AMRO",
        "SEARO",
        "Other"
    ]
    }
    """
    return {"whos":getUniqueWhos()}

@app.get("/casesByRegionG/")
async def casesByRegionG(year:int = None):
    """
    Returns the number of cases by region (by dr griffin)

    """

    # create a dictionary as a container for our results
    # that will hold unique regions. Why, because there 
    # cannot be duplicate keys in a dictionary.
    cases = {}

    # return {'success':False,'message':'no database exists'}

    # loop through our db list
    for row in db:
        
        # If there is a year passed in and that year is not equal to this row
        # then skip the rest of code
        if year != None and year != int(row[0][:4]):
            continue
            
        # this line guarantees that the dictionary has the region as a key
        if not row[3] in cases:
            cases[row[3]] = 0
        
        # this line adds the case count to whatever is at that key location
        cases[row[3]] += int(row[4])    

    # return cases

    return {"data":cases,"success":True,"message":"Cases by Region Griffin","size":len(cases),"year":year}

@app.get("/cases_by_country/")
async def casesByCountry(country:str):
    """
    This method will return a total case count by country
    - **Params:**
      - country (str) : A country name (case insensitive)
    - **Returns:**
      - (int) : The total amount of cases

    #### Example 1:

    [http://localhost:5000/cases_by_country/?country=Albania](http://localhost:5000/cases_by_country/?country=Albania)

    #### Response 1:
        {
        "data": 3604,
        "success": true,
        "message": "Cases by Country",
        "size": 4
        }
        
    """
    deaths = getTotalCasesByCountry(country)
    return {"data":deaths, "success":True,"message":"Cases by Country","size":len(str(deaths))}

@app.get("/cases_by_country_year/{country}/{year}")
async def casesByCountryYear(country:str, year:int):
    """
    This method will return a total case count by  in a specific year
    - **Params:**
      - country (str) : A country name (case insensitive)
      - year (int) : A year
    - **Returns:**
      - (int) : The total amount of cases

    #### Example 1:

    [http://127.0.0.1:5000/cases_by_country_year/China/2022](http://127.0.0.1:5000/cases_by_country_year/China/2022)

    #### Response 1:
        {
            "data": 84792971,
            "success": true,
            "message": "Cases by Country Year",
            "size": 8
            }
        
    """
    deaths = getTotalCasesByCountryYear(country, year)
    return {"data":deaths, "success":True,"message":"Cases by Country Year","size":len(str(deaths))}


@app.get("/cases_by_region/")
async def casesByRegion(region:str):
    """
    This method will return a total case count by region
    - **Params:**
      - country (str) : A country name (case insensitive)
    - **Returns:**
      - (int) : The total amount of cases

    #### Example 1:

    [http://127.0.0.1:5000/cases_by_region/?region=AFRO](http://127.0.0.1:5000/cases_by_region/?region=AFRO)

    #### Response 1:
        {
            "data": 9538679,
            "success": true,
            "message": "Cases by Region",
            "size": 7
            }
        
    """
    deaths = getTotalCasesByRegion(region)
    return {"data":deaths, "success":True,"message":"Cases by Region","size":len(str(deaths))}

@app.get("/cases_by_region_year/{region}/{year}")
async def casesByRegionYear(region:str, year:int):
    """
    This method will return a total case count by region in a specific year
    - **Params:**
      - country (str) : A country name (case insensitive)
      - year (int) : A year
    - **Returns:**
      - (int) : The total amount of cases

    #### Example 1:

    [http://127.0.0.1:5000/cases_by_region_year/AFRO/2022](http://127.0.0.1:5000/cases_by_region_year/AFRO/2022)

    #### Response 1:
        {
        "data": 2144972,
        "success": true,
        "message": "Cases by Region Year",
        "size": 7
        }
        
    """
    deaths = getTotalCasesByRegionYear(region, year)
    return {"data":deaths, "success":True,"message":"Cases by Region Year","size":len(str(deaths))}


@app.get("/cases/")
async def cases():
    """
    This method will return a total number of cases 
    - **Params:**
      - None
    - **Returns:**
      - (int) : The total amount of cases

    #### Example 1:

    [http://localhost:5000/cases/](http://localhost:5000/cases/)

    #### Response 1:
        {
        "data": 768187119,
        "success": true,
        "message": "Cases",
        "size": 9
        }
        
    """
    deaths = 0
    for country in getUniqueCountries():
        deaths += getTotalCasesByCountry(country)
    return {"data":deaths, "success":True,"message":"Cases","size":len(str(deaths))}



@app.get("/deaths_by_country/")
async def deathsByCountry(country:str):
    """
    This method will return a total death count by country
    - **Params:**
      - country (str) : A country name (case insensitive)
    - **Returns:**
      - (int) : The total amount of deaths

    #### Example 1:

    [http://localhost:5000/deaths_by_country/?country=Albania](http://localhost:5000/deaths_by_country/?country=Albania)

    #### Response 1:
        {
        "data": 3604,
        "success": true,
        "message": "Deaths by Country",
        "size": 4
        }
        
    """
    deaths = getTotalDeathsByCountry(country)
    return {"data":deaths, "success":True,"message":"Deaths by Country","size":len(str(deaths))}

@app.get("/deaths_by_country_year/{country}/{year}")
async def deathsByCountryYear(country:str, year:int):
    """
    This method will return a total death count by country in a given year
    - **Params:**
      - country (str) : A country name (case insensitive)
      - year (int) : A year
    - **Returns:**
      - (int) : The total amount of deaths

    #### Example 1:

    [http://127.0.0.1:5000/deaths_by_country_year/Albania/2022](http://127.0.0.1:5000/deaths_by_country_year/Albania/2022)

    #### Response 1:
        {
        "data": 384,
        "success": true,
        "message": "Deaths by Country Year",
        "size": 3
        }
        
    """
    deaths = getTotalDeathsByCountryYear(country, year)
    return {"data":deaths, "success":True,"message":"Deaths by Country Year","size":len(str(deaths))}


@app.get("/deaths_by_region/")
async def deathsByRegion(region:str):
    """
    This method will return a total death count by region
    - **Params:**
      - country (str) : A region name (case insensitive)
    - **Returns:**
      - (int) : The total amount of deaths

    #### Example 1:

    [http://127.0.0.1:5000/deaths_by_region/?region=AFRO](http://127.0.0.1:5000/deaths_by_region/?region=AFRO)

    #### Response 1:
        {
        "data": 175394,
        "success": true,
        "message": "Deaths by Region",
        "size": 6
        }
        
    """
    deaths = getTotalDeathsByRegion(region)
    return {"data":deaths, "success":True,"message":"Deaths by Region","size":len(str(deaths))}

@app.get("/deaths_by_region_year/{region}/{year}")
async def deathsByRegionYear(region:str, year:int):
    """
    This method will return a total death count by region in a specific year
    - **Params:**
      - country (str) : A region name (case insensitive)
      - year (int) : A year
    - **Returns:**
      - (int) : The total amount of deaths

    #### Example 1:

    [http://127.0.0.1:5000/deaths_by_region_year/AFRO/2022](http://127.0.0.1:5000/deaths_by_region_year/AFRO/2022)

    #### Response 1:
        {
        "data": 18955,
        "success": true,
        "message": "Deaths by Region",
        "size": 5
        }
        
    """
    deaths = getTotalDeathsByRegionYear(region, year)
    return {"data":deaths, "success":True,"message":"Deaths by Region Year","size":len(str(deaths))}


@app.get("/deaths/")
async def deaths():
    """
    This method will return a total of all deaths
    - **Params:**
      - None
    - **Returns:**
      - (int) : The total amount of deaths

    #### Example 1:

    [http://localhost:5000/deaths/](http://localhost:5000/deaths/)

    #### Response 1:
        {
            "data": 6948647,
            "success": true,
            "message": "Deaths",
            "size": 7
            }
        
    """
    deaths = 0
    for country in getUniqueCountries():
        deaths += getTotalDeathsByCountry(country)
    return {"data":deaths, "success":True,"message":"Deaths","size":len(str(deaths))}

@app.get("/max_deaths/")
async def maxDeaths(min_date:str or None = None, max_date:str or None = None):
    """
    This method will return the country with the most deaths in a timespan, as well as how many deaths that country had
    You can input no dates or a start date and an end date
    - **Params:**
      - (optional) min_date (str) - the earliest date to look at
      - (optional) max_date (str) - the latest date to look at
    - **Returns:**
      - (str) : The country that had the least deaths
      - (int) : The amount of deaths that country had

    #### Example 1:

    [http://127.0.0.1:5000/max_deaths/](http://127.0.0.1:5000/max_deaths/)

    #### Response 1:
        {
        "data": "United States of America",
        "deaths": 1127152,
        "success": True
        }
        
    #### Example 2:

    [http://127.0.0.1:5000/max_deaths/?min_date=2020-01-01&max_date=2021-05-05](http://127.0.0.1:5000/max_deaths/?min_date=2020-01-01&max_date=2021-05-05)

    #### Response 2:
        {
        "data": "United States of America",
        "deaths": 577163,
        "success": true
        }
    """
    killFlag = False
    if ((min_date is None) ^ (max_date is None)):
        killFlag = True
    # python got mad if i don't use a bool like this for the error return
    if killFlag:
        return {"success":False, "message":"Must input two dates or no dates"}

    if min_date is not None:
        try:
           minYear = min_date.split("-")[0]
           minMonth = min_date.split("-")[1]
           minDay = min_date.split("-")[2]

           minDateT = datetime(int(minYear), int(minMonth), int(minDay))

           maxYear = max_date.split("-")[0]
           maxMonth = max_date.split("-")[1]
           maxDay = max_date.split("-")[2]

           maxDateT = datetime(int(maxYear), int(maxMonth), int(maxDay))
        except Exception as e:
            print(e)
            
            return {"success":False, "message":"Date format invalid"}

    maxDeaths = 0
    country = ""
    for countries in getUniqueCountries():
        if min_date is not None:
            countryDeaths = getTotalDeathsByCountry_timeframe(countries, minDateT, maxDateT)
        else:
            countryDeaths = getTotalDeathsByCountry(countries)
        if maxDeaths < countryDeaths:
            maxDeaths = countryDeaths
            country = countries
    return {"data":country, "deaths":maxDeaths, "success":True}

@app.get("/min_deaths/")
async def minDeaths(min_date:str or None = None, max_date:str or None = None):
    """
    This method will return the country with the least deaths in a timespan, as well as how many deaths that country had
    You can input no dates or a start date and an end date
    - **Params:**
      - (optional) min_date (str) - the earliest date to look at
      - (optional) max_date (str) - the latest date to look at
    - **Returns:**
      - (str) : The country that had the least deaths
      - (int) : The amount of deaths that country had

    #### Example 1:

    [http://127.0.0.1:5000/min_deaths/](http://127.0.0.1:5000/min_deaths/)

    #### Response 1:
        {
        "data": "Democratic People's Republic of Korea",
        "deaths": 0,
        "success": true
        }

    #### Example 2:

    [http://127.0.0.1:5000/min_deaths/?min_date=2020-01-01&max_date=2021-05-05](http://127.0.0.1:5000/min_deaths/?min_date=2020-01-01&max_date=2021-05-05)

    #### Response 2:
        {
        "data": "Democratic People's Republic of Korea",
        "deaths": 0,
        "success": true
        }

    """
    killFlag = False
    if ((min_date is None) ^ (max_date is None)):
        killFlag = True
    # python got mad if i don't use a bool like this for the error return idk why
    if killFlag:
        return {"success":False, "message":"Must input two dates or no dates", "success":True}

    if min_date is not None:
        try:
           minYear = min_date.split("-")[0]
           minMonth = min_date.split("-")[1]
           minDay = min_date.split("-")[2]

           minDateT = datetime(int(minYear), int(minMonth), int(minDay))

           maxYear = max_date.split("-")[0]
           maxMonth = max_date.split("-")[1]
           maxDay = max_date.split("-")[2]

           maxDateT = datetime(int(maxYear), int(maxMonth), int(maxDay))
        except Exception as e:
            print(e)
            
            return {"success":False, "message":"Date format invalid"}

    minDeaths = 99999999999999
    country = ""
    for countries in getUniqueCountries():
        if min_date is not None:
            countryDeaths = getTotalDeathsByCountry_timeframe(countries, minDateT, maxDateT)
        else:
            countryDeaths = getTotalDeathsByCountry(countries)
        if minDeaths > countryDeaths:
            minDeaths = countryDeaths
            country = countries
    return {"data":country, "deaths":minDeaths}
        
@app.get("/avg_deaths/")
async def avgDeaths():
    """
    This method will return an average of all deaths
    - **Params:**
      - None
    - **Returns:**
      - (int) : The average amount of deaths

    #### Example 1:

    [http://localhost:5000/avg_deaths/](http://localhost:5000/avg_deaths/)

    #### Response 1:
        {
        "data": 3241295.860759494,
        "success": true
        }
        
    """
    countryCount = 0
    deathCount = 0
    for countries in getUniqueCountries():
        countryCount += 1
        deathCount += getTotalCasesByCountry(countries)
    return {"data":(deathCount / countryCount), "success":True}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
