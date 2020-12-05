# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from wordcloud import WordCloud
from matplotlib import rcParams
from PIL import Image

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

actress = pd.read_json('data/data_json/actress.json')
print(actress.head())
print(actress.info())

actress['birthday'] = pd.to_datetime(actress['birthday'], yearfirst=True)
actress['age'] = 2020 - pd.DatetimeIndex(actress['birthday']).year
print(actress.head())
# actress['age'] = actress.age.fillna(35)
print(actress.info())

print(actress['age'].min())
print('Minimum age: ' + str(actress.age.min()))
print(actress[actress['age'] == actress.age.min()])
print(actress.describe())

sns.displot(actress.age.dropna())
plt.show()

actress.bust.plot.hist(figsize=(10,6),bins=50)
plt.show()

print(actress[actress.name.str.contains("Mikami")])

hobby_df = actress[actress.hobby.notnull()]
print(hobby_df.info())
hobby_txt = ' '.join(hobby_df['hobby'])
rcParams['figure.figsize'] = 15,8
wordcloud = WordCloud(font_path='data/data_json/jp.otf', max_words=200, max_font_size=40, scale=5, background_color="black").generate(hobby_txt)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

mask = np.array(Image.open('data/data_json/mask_black.png'))
wordcloud = WordCloud(font_path='data/data_json/jp.otf', max_words=200, background_color="white", mask=mask).generate(hobby_txt)
plt.figure(figsize=(30,15))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()