import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import rcParams
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('data/data_csv/diemthidhqg2020_test.csv')

ten = data['ten'].dropna()
# ten.to_csv('name.csv')
# ten = ["Lê", "Phương", "Nam","Lê", "Nam","Lê", "Phương", "Nguyễn", "Thị", "Hồng", "Hoa"]
ten_string = ' '.join(ten)
# print(ten_string)

rcParams['figure.figsize'] = 10,15
mask = np.array(Image.open('vn_mask.jpg'))
# wordcloud = WordCloud(max_words=len(ten), max_font_size=100, scale=20).generate(ten_string)
wordcloud = WordCloud(max_words=len(ten), background_color="white", mask=mask, max_font_size=100, scale=8, collocations=False).generate(ten_string)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# toan = data['toan_hoc'].dropna()
# print(len(toan)) #74205
#
# van = data['ngu_van'].dropna()
# print(len(van)) #72648
#
# anh = data['tieng_anh'].dropna()
# print(len(anh)) #65898




# toan.plot(figsize=(10,10),bins=100)
# plt.show()

# plt.plot(toan.value_counts().sort_index(), color='red', linestyle = ':', marker='.', markersize=10)
# plt.grid(True)
# plt.legend(['Mon Toan'])
# plt.xlabel('Diem')
# plt.ylabel('So luong')
# plt.title('Thong ke diem mon Toan')
# print(toan.value_counts())
# # plt.plot(toan.value_counts().sort_index())
# plt.show()
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# def du_doan_gia_dat(x1):
#     y1 = w[0] + w[1] * x1
#     print('Gia nha cho ' + str(x1) + 'm2 la: ', y1)
#
# data = pd.read_csv('data/data_csv/gia_nha_dat.csv').values
# N = data.shape[0]
# x = data[:,0].reshape(-1,1)
# y = data[:,1].reshape(-1,1)
# plt.scatter(x,y)
# plt.xlabel('met vuong')
# plt.ylabel('gia (*1000nvd)')
# x = np.hstack((np.ones((N, 1)), x))
# w = np.array([0.,1.]).reshape(-1,1)
# numOfIrentation = 100
# cost = np.zeros((numOfIrentation,1))
# learning_rate = 0.000001
# for i in range(1, numOfIrentation):
#     r = np.dot(x,w) - y
#     cost[i] = 0.5*np.sum(r*r)
#     w[0] -= learning_rate*np.sum(r)
#     w[1] -= learning_rate*np.sum(np.multiply(r, x[:,1].reshape(-1,1)))
#     print(cost[i])
# predict = np.dot(x,w)
# plt.plot((x[0][1], x[N-1][1]), (predict[0], predict[N-1]), 'r')
# plt.show()
#
# du_doan_gia_dat(294)

# percents = [9.4, 10.8, 11.3, 12.4, 24.8, 31.3]
# programming_languages = ["C++", "C#", "Javascript", "PHP", "Python", "Java"]
# explode = [0, 0.1, 0, 0, 0, 0]
# plt.pie(percents, labels=programming_languages, autopct='%1.3f%%', explode=explode)
# plt.show()

# print(van.value_counts().sort_index())
# print(anh.value_counts().sort_index())
# plt.pie(anh.value_counts().sort_index(), autopct='%1.2f%%', wedgeprops={'edgecolor': 'white', 'linewidth':1.5})
# anh = round(anh*1)/1
# print(anh.value_counts().sort_index())
# plt.pie(anh.value_counts().sort_index(), autopct='%1.2f%%')
# diem_thi = ["Diem 0", "Diem 1", "Diem 2", "Diem 3", "Diem 4", "Diem 5", "Diem 6", "Diem 7", "Diem 8", "Diem 9", "Diem 10"]
# diem_thi = anh.value_counts().sort_index().index.tolist()
# explode = [0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0]
# plt.pie(anh.value_counts().sort_index(), pctdistance=1.2, autopct='%1.2f%%', wedgeprops={'edgecolor': 'white', 'linewidth':0.5}, explode=explode)
# plt.figlegend(diem_thi)
# plt.title('Thong ke diem mon Tieng Anh')
# plt.show()

# van = round(van*2)/2
# plt.figure(figsize = (15,5))
# diem_thi = van.value_counts().sort_index().index.tolist()
# diem_thi = list(map(str,diem_thi))
# plt.grid(True)
# plt.bar(diem_thi, van.value_counts().sort_index(), color='g')
# plt.legend(['Mon Van'])
# plt.xlabel('Diem')
# plt.ylabel('So luong')
# plt.title('Thong ke diem mon Ngu Van')
# plt.show()