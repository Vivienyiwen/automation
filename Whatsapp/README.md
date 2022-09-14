# Automatically send personalized messages to multiple people
1.prepare a .csv file

[modeltable.csv](https://github.com/Vivienyiwen/automation/blob/main/Whatsapp/modeltable.csv) as an example

2.Modify the corresponding information in .py against the information in the table

e.g.
```ruby
data = pd.read_csv('/Users/wen9953/Desktop/REV/Auto_Whatsapp/xxx.csv')
#Change the name of your corresponding csv file
#xxx.csv --> modeltable.csv
```
3.run the .py
```ruby
python3 auto_Whatsapp.py
```
[auto_Whatsapp.py](https://github.com/Vivienyiwen/automation/blob/main/Whatsapp/auto_Whatsapp.py) as an example

*However, it is to be noted that ***each account*** sent to an account will open ***another whatsapp web window***.
