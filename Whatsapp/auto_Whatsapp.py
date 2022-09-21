import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import re

#Ensure that the .csv is in the correct format, otherwise the encoding format may be incorrect!
data = pd.read_csv('/Users/wen9953/Desktop/REV/Auto_Whatsapp/Customer04.csv', encoding='utf-8-sig')

data_dict = data.to_dict('list')
leads = data_dict['phone'] #Enter the corresponding column name in single quotes, and make sure the column name is correct
instructors = data_dict['INSTRUCTOR']
name = data_dict['NAME']
combo = zip(leads, instructors, name)
first = True
for leads, instructors, name in combo:
    time.sleep(4)
    
    i = instructors
    i = ''.join(re.findall('[A-Za-z]*\s*[A-Za-z]*\s*[A-Za-z]', i))
    web.open('https://web.whatsapp.com/send?phone=' + leads + '&text=' + "Hello " + name + "! I'm Chevon, a membership consultant from Revolution and I noticed that you recently attended " + i + "'s class! How was it? I would love to hear any feedback that you may have for us! :)")
    if first:
        time.sleep(6)
        first = False
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')

