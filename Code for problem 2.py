import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data = pd.read_csv('Mall_Customers.csv')
purchase_data = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]  # Replace with your features

scaler = StandardScaler()
scaled_data = scaler.fit_transform(purchase_data)

k = 3

kmeans = KMeans(n_clusters=k, random_state=0)

kmeans.fit(scaled_data)

customer_clusters = kmeans.labels_

data['cluster'] = customer_clusters

for i in range(k):
  cluster_data = data[data['cluster'] == i]
  print(f"Cluster {i+1} summary:")


features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']  


cluster_data = {}
for i in range(k):
  cluster_data[i] = data[data['cluster'] == i][features]


plt.figure(figsize=(8, 6))
for cluster, data_points in cluster_data.items():
  plt.scatter(data_points.iloc[:, 0], data_points.iloc[:, 1], label=f"Cluster {cluster+1}")

plt.xlabel(features[0])
plt.ylabel(features[1])
plt.title('Customer Segmentation using K-Means')
plt.legend()
plt.grid(True)
plt.show()




data['cluster'] = customer_clusters  
data.to_csv('clustered_data.csv', index=False)  

print("Clustered data exported to clustered_data.csv")