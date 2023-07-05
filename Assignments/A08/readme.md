## A08
### Dylan Miles
### Description:
Used Python and FastAPI to create an API of COVID-19 data

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [api.py](./api.py)         | Main driver of my project, run it to get the full experience.      |
|   2   | [data.csv](./data.csv)  | COVID-19 data in csv format, needed for my program to work |
|   3   | [report.md](./report.md)  |  brief report summarizing the implementation process, challenges faced, and any additional functionalities I may have added. |
|   4   | [requirements.txt](./requirements.txt) | List of python dependencies for this project |

### Instructions

Python 3, and the packages in [requirements.txt](./requirements.txt), are required

to run: `python -u "/home/bfce/4883-Software-Tools-Miles/Assignments/A08/api.py"`

# API endpoints: 

## Countries

  `

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
    `
## Whos

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
## Cases_by_country

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
                
## Cases_by_country_year

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
                
## cases_by_region

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
    
## cases_by_region_year

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

## cases

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
                
## deaths_by_country

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

## deaths_by_country_year

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
                
## deaths_by_region

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
                

## deaths_by_region_year

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
                
## deaths

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
                
## max_deaths

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

## min_deaths

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


## avg_deaths

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
                