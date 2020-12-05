import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

def recommend(model, vong1, vong2, vong3, chieu_cao, nhom_mau):
  arr = np.array([[vong1, vong2, vong3, chieu_cao, nhom_mau]])
  pred = model.predict(arr)
  return lookup[lookup['cluster'] == pred[0]].sample(10)

actress = pd.read_json("data/data_json/actress.json")
print(actress.head())

df = actress[['bust', 'waist', 'hip', 'height', 'blood_type']]
print(df.info())
df = df.dropna()
print(df.info())
print(df.head())

print(df.blood_type.value_counts())
mapper = {'O': 0, 'A':1, 'B':2, 'AB':3}
df['blood_type'] = df['blood_type'].map(mapper)
print(df.head())

actress_np = df.to_numpy()
print(actress_np)

k_mean_5 = KMeans(n_clusters=5)
k_mean_5.fit(actress_np)
label_5 = k_mean_5.labels_
print(label_5)
print(metrics.silhouette_score(actress_np, label_5, metric='euclidean'))
print(metrics.calinski_harabasz_score(actress_np, label_5))

k_mean_10 = KMeans(n_clusters=10)
k_mean_10.fit(actress_np)
label_10 = k_mean_10.labels_
print(label_10)
print(metrics.silhouette_score(actress_np, label_10, metric='euclidean'))
print(metrics.calinski_harabasz_score(actress_np, label_10))

sum_distances = []
K = range(1,15)
for k in K:
  k_mean = KMeans(n_clusters=k)
  k_mean.fit(actress_np)
  sum_distances.append(k_mean.inertia_)

plt.plot(K, sum_distances, 'bx-')
plt.show()

k_mean_3 = KMeans(n_clusters=3)
model = k_mean_3.fit(actress_np)
result = k_mean_3.labels_
print(result)
print(metrics.silhouette_score(actress_np, result, metric='euclidean'))
print(metrics.calinski_harabasz_score(actress_np, result))

print(df.head())
plt.scatter(actress_np[:,0], actress_np[:,3])
plt.show()

plt.scatter(
    actress_np[result == 0, 0], actress_np[result == 0, 3],
    c='lightgreen',
    marker='s', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    actress_np[result == 1, 0], actress_np[result == 1, 3],
    c='orange',
    marker='o', edgecolor='black',
    label='cluster 2'
)

plt.scatter(
    actress_np[result == 2, 0], actress_np[result == 2, 3],
    c='lightblue',
    marker='v', edgecolor='black',
    label='cluster 3'
)

plt.scatter(
    model.cluster_centers_[:, 0], model.cluster_centers_[:, 3],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)

plt.legend(scatterpoints=1)
plt.grid()
plt.show()

# Input: vong 1, vong 2, vong 3, chieu cao, nhom mau
#
# -> thuoc ve cum nao (which cluster?)
#
# random(10) in the clusters

df1 = actress[['id','bust', 'waist', 'hip', 'height', 'blood_type']]
df1 = df1.dropna()
print(df1.info())

df2 = actress[['id', 'name', 'japanName']]
print(df2.head())

lookup = df1.merge(df2, on='id', how='left')
print(lookup.info())
lookup['cluster'] = result
print(lookup.head())

vong1 = 85
vong2 = 55
vong3 = 88
chieu_cao = 155
nhom_mau = 0 # nhom mau 0

print(recommend(model, vong1, vong2, vong3, chieu_cao, nhom_mau))