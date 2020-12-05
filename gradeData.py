import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from matplotlib import rcParams
from PIL import Image
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('data/data_csv/diemthidhqg2020.csv')
print(data)
print(data.head())
data[data[:] == -1] = np.nan
print(data.info())
# sns.displot(data.toan_hoc.dropna())
data.yyyy.plot.hist(figsize=(10,10),bins=1)
plt.show()
sns.displot(data.yyyy.dropna())
plt.show()