# Wordcloud

[worldcloud.py](https://github.com/Vivienyiwen/automation/blob/main/Data%20Visualization/wordcloud.py) show as an example

Note that we need to first download and merge each instructor's csv file within a new csv file.

This step of the merge can be achieved with the following command in the terminal:
```ruby
import pandas as pd
import glob
import os

files = os.path.join("/Users/wen9953/Desktop/REV/customer's reviews_Aug/","ratings*.csv") #put the path of file. ratings*.csv here means every .csvfile titled ratings
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(df)

df.to_csv(r"/Users/wen9953/Desktop/REV/customer's reviews_Aug/test01.csv",index=False,header=True)
```
