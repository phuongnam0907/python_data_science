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
print(data.info())