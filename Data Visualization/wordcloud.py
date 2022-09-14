#make sure you have install all these package in your library
from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
import pandas as pd
import matplotlib.pylab as plt
from PIL import Image
import numpy as np


stopwords = set(STOPWORDS)
#set your wordcloud image template, you can choose whatever image you like
mask = np.array(Image.open("/Users/wen9953/Desktop/REV/template01.png"))#input your image's path

#we will read the text
data_file = pd.read_csv("/Users/wen9953/Desktop/REV/customer's reviews_Aug/test01.csv")#input your csv file's path

#wordcloud
#you can change the szie of image here
wordcloud = WordCloud(stopwords = stopwords , width=1600 , height=800,mask=mask,background_color="White",colormap="Set2").generate(''.join(map(str, data_file['COMMENT'])))#I use map(str, data_flie) here to avoid data type conversion errors 
plt.figure(figsize=(20,10),facecolor='k')
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.tight_layout (pad=0)

#saving the image of wordcloud
wordcloud.to_file ("/Users/wen9953/Desktop/REV/wordcloud.png")#input your saving path and name the saved file
plt.show()
