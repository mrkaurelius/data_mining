'''
Data analysis and virtualisation
source: https://www.kaggle.com/ruchi798/book-crossing-starter-notebook-and-eda
'''
#%% imports

import requests

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from PIL import Image as im
from wordcloud import WordCloud,STOPWORDS
from IPython.core.display import Image
from colorama import Fore, Back, Style

y_ = Fore.YELLOW
r_ = Fore.RED
g_ = Fore.GREEN
b_ = Fore.BLUE
m_ = Fore.MAGENTA
sr_ = Style.RESET_ALL

custom_colors = ['#48bfe3','#56cfe1','#64dfdf','#72efdd','#80ffdb']
customPalette = sns.color_palette(custom_colors)

sns.palplot(sns.color_palette(custom_colors),size=1)

sns.set_context("poster")

#%% reading cvs

u_cols = ['user_id', 'location', 'age']
users = pd.read_csv('./data/book_x/BX-Users.csv', sep=';', names=u_cols, encoding='latin-1',low_memory=False)

#Books
i_cols = ['isbn', 'book_title' ,'book_author','year_of_publication', 'publisher', 'img_s', 'img_m', 'img_l']
items = pd.read_csv('./data/book_x/BX_Books.csv', sep=';', names=i_cols, encoding='latin-1',low_memory=False)

#Ratings
r_cols = ['user_id', 'isbn', 'rating']
ratings = pd.read_csv('./data/book_x/BX-Book-Ratings.csv', sep=';', names=r_cols, encoding='latin-1',low_memory=False)

#%% user

print(users.head(5))
print(users.describe())
print(f"{y_}{users.dtypes}\n") 

#%% items

print(items.head(5))
print(items.describe())
print(f"{y_}{items.dtypes}\n") 

#%% ratings

print(ratings.head(5))
print(ratings.describe())
print(f"{y_}{ratings.dtypes}\n") 


#%% 
print(f"{y_}{users.dtypes}\n") 
print(f"{y_}{items.dtypes}\n") 
print(f"{y_}{ratings.dtypes}\n") 


#%%
# users = users.drop(users.index[0])
# items = items.drop(items.index[0])
# ratings = ratings.drop(ratings.index[0])



#%% Changing datatypes and replacing nan values

# users['age'] = users['age'].astype(float)
# users['user_id'] = users['user_id'].astype(int)
# ratings['user_id'] = ratings['user_id'].astype(int)
# ratings['rating'] = ratings['rating'].astype(int)
# items['year_of_publication'] = items['year_of_publication'].astype(int)

# print(users.isnull().sum())
# print(users['age'].describe())

# users.loc[(users.age>99) | (users.age<5),'age'] = np.nan
# users.age = users.age.fillna(users.age.mean())


