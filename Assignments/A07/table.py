import PySimpleGUI as psg
import numpy as np
#Modified from this tutorial
#https://www.tutorialspoint.com/pysimplegui/pysimplegui_table_element.htm
def openTable(table, isDaily):
        psg.set_options(font=("Arial Bold", 14))
        #Daily has different information than others
        if isDaily:
                toprow = ['Time', 'Temp', 'Dew Point', 'Humidity', 'Wind', 'Wind Speed', 'Wind Gust', 'Pressure', 'Precipitation', 'Condition']
                rows = table
        else:
                toprow = ['Time', 'Temp', 'Dew Point', 'Humidity', 'Wind', 'Pressure', 'Precipitation']
                #However i pull in my data, it needs to be transposed to work properly with psg tables
                #But the daily tables don't for ... some reason
                rows = np.array(table).T.tolist()
        tbl1 = psg.Table(values=rows, headings=toprow,
        auto_size_columns=True,
        display_row_numbers=False,
        justification='center', key='-TABLE-',
        selected_row_colors='red on yellow',
        enable_events=True,
        expand_x=True,
        expand_y=True,
        enable_click_events=True)
        layout = [[tbl1]]
        #Adapt window size
        window = psg.Window("Weather stats", layout, size=(tbl1.get_size()[0], tbl1.get_size()[1]), resizable=True)
        window.read()
        #Just so it doesn't close the window when you click
        while True:
                event, values = window.read()
                if event == psg.WIN_CLOSED:
                        break

#mainly for testing
if __name__=='__main__':
        table = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
         ['86   77.3   67', '89   74.6   65', '83   71.2   64', '85   74.4   64', '88   75.2   65', '89   77.0   64', '88   74.0   63',
          '89   75.3   62', '95   80.2   64', '92   78.0   67', '95   80.9   66', '75   66.8   62', '80   71.4   64', '89   72.0   65',
           '93   74.4   64', '88   76.0   67', '90   75.9   65', '88   74.0   63', '95   81.1   63', '92   82.2   78'], ['66   64.3   60',
            '68   64.5   63', '66   63.5   62', '66   62.2   59', '65   61.8   57', '64   61.6   59', '65   62.7   61', '65   62.4   60',
             '70   65.4   63', '67   64.5   61', '69   64.5   61', '63   60.4   57', '70   64.9   58', '69   65.1   57', '71   63.9   59',
              '67   64.4   63', '74   67.3   62', '67   60.8   57', '77   69.6   61', '77   76.4   76'], ['87   65.9   46', '94   73.5   43',
               '93   77.9   53', '93   67.7   44', '87   65.8   37', '90   61.4   37', '93   70.3   40', '96   67.6   40', '96   64.3   36',
                '87   65.6   41', '93   61.0   35', '93   80.5   62', '93   80.3   66', '100   82.7   35', '93   72.2   38', '90   69.3   45',
                 '97   76.4   49', '93   66.0   39', '93   69.6   51', '93   82.9   62'], ['16   8.9   0', '23   12.2   3', '14   5.3   0',
                  '21   7.3   0', '9   3.7   0', '15   6.2   0', '16   3.6   0', '12   5.4   0', '8   3.0   0', '22   9.7   0', '20   8.1   0',
                   '24   14.0   7', '12   6.2   0', '9   2.9   0', '40   15.3   0', '12   6.7   0', '23   9.3   0', '26   7.1   0', '16   10.8   0',
                    '15   11.3   7'], ['28.8   28.7   28.7', '28.8   28.7   28.6', '28.8   28.7   28.6', '28.8   28.7   28.7', '28.9   28.8   28.8',
                     '28.8   28.8   28.7', '28.8   28.7   28.6', '28.7   28.7   28.6', '28.7   28.6   28.6', '28.7   28.6   28.5', '28.7   28.6   28.6',
                      '28.9   28.8   28.7', '28.8   28.7   28.6', '28.6   28.6   28.6', '28.6   28.6   28.4', '28.7   28.7   28.6', '28.8   28.7   28.5',
                       '28.7   28.6   28.6', '28.7   28.6   28.6', '28.6   28.6   28.6'], ['0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.01',
                        '0.00', '0.01', '0.02', '0.00', '0.62', '0.04', '0.00', '0.97', '0.00', '0.27', '0.00', '0.00']]
        openTable(table, False)