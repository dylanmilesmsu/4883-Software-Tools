""" 
Description:
    This is an example gui that allows you to enter the appropriate parameters to get the weather from wunderground.
TODO:
    - You will need to change the text input boxes to drop down boxes and add the appropriate values to the drop down boxes.
    - For example the month drop down box should have the values 1-12.
    - The day drop down box should have the values 1-31.
    - The year drop down box should have the values ??-2023.
    - The filter drop down box should have the values 'daily', 'weekly', 'monthly'.
"""
import PySimpleGUI as sg      
import pandas
def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month,current_day,current_year = currentDate('tuple')

    filterList = ['daily', 'weekly', 'monthly']

    #I'm not a python expert so this is the cleanest way i know how to do this
    #probably slow but cmon its python... its slow anyways :P
    monthList = []
    for i in range(1, 13):
        monthList.append(i)

    dayList = []
    for i in range(1, 32):
        dayList.append(i)

    yearList = []
    for i in range(2000, current_year+1):
        yearList.append(i)

    #read in icao codes with pandas
    #i think i heard about this in class or something
    pdcodes = pandas.read_json("airports-better.json")
    pdcodes = pdcodes.sort_values(by=["icao"])
    apcodes = pdcodes['icao'].tolist()

    # Create the gui's layout using text boxes that allow for user input without checking for valid input
    layout = [
        [sg.Text('Month')],[sg.Combo(monthList)],
        [sg.Text('Day')],[sg.Combo(dayList)],
        [sg.Text('Year')],[sg.Combo(yearList)],
        [sg.Text('Code')],[sg.Combo(apcodes)],
        [sg.Text('Daily / Weekly / Monthly')],[sg.Combo(filterList)],
        [sg.Submit(), sg.Cancel()]
    ]      

    window = sg.Window('Get The Weather', layout)    

    event, values = window.read()
    window.close()
        
    month = values[0]
    day = values[1]
    year = values[2]
    code = values[3]
    filter = values[4]

    #just default values if you dont input anything
    if len(str(month)) < 1:
        month = current_month
    if len(str(day)) < 1:
        day = current_day
    if len(str(year)) < 1:
        year = current_year
    if len(code) < 1:
        code = "KLAW"
    if len(filter) < 1:
        filter = "monthly"

    #sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

    base_url = "https://wunderground.com/history"
    airport = code
    #the date part was forgotten lol
    url = f"{base_url}/{filter}/{airport}/date/{year}-{month}-{day}"
    return url


if __name__=='__main__':
    buildWeatherURL()
