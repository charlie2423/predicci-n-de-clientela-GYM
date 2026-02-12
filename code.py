import pandas as pd 
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



gym_churn = pd.read_csv('/datasets/gym_churn_us.csv')
gym_churn.info()
print(gym_churn.head(10))
print(gym_churn.describe())


group_one = gym_churn.groupby('Churn').mean()
print(group_one)

plt.hist(gym_churn[gym_churn['Churn']==0]['Age'],alpha=0.5,label='se quedaron')
plt.hist(gym_churn[gym_churn['Churn']==1]['Age'],alpha=0.5,label='no se quedaron')
plt.legend()


corr_m = gym_churn.corr()
plt.figure(figsize= (20,20))
sns.heatmap(corr_m,square= True, annot= True)


X = gym_churn.drop('Churn',axis=1)
y = gym_churn['Churn']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

scaler = StandardScaler()
x_train_st = scaler.fit_transform(X_train)
x_test_st = scaler.transform(X_test)


model_lr = LogisticRegression(random_state=42)
model_lr.fit(x_train_st,y_train)
prediction_lr = model_lr.predict(x_test_st)

model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(x_train_st,y_train)
prediction_rf = model_rf.predict(x_test_st)

print('Exactitud: {:.2f}'.format(accuracy_score(y_test,prediction_lr)))
print('Precisión: {:.2f}'.format(precision_score(y_test,prediction_lr)))
print('Recall: {:.2f}'.format(recall_score(y_test,prediction_lr)))
print()
print('Exactitud: {:.2f}'.format(accuracy_score(y_test,prediction_rf)))
print('Precisión: {:.2f}'.format(precision_score(y_test,prediction_rf)))
print('Recall: {:.2f}'.format(recall_score(y_test,prediction_rf)))


x_ = gym_churn.drop(columns = ['Age'],axis=1)
y_ = gym_churn['Age']

x_sc = scaler.fit_transform(x_)
linked = linkage(x_sc,method= 'ward')

plt.figure(figsize = (15,15))
dendrogram(linked, orientation='top')
plt.title('Agrupación jerárquica para GYM')
plt.show()

X_SC = scaler.fit_transform(gym_churn)
k_m = KMeans(n_clusters=5,random_state=42)
labels = k_m.fit_predict(X_SC)
gym_churn['cluster_km'] = labels

print(gym_churn['cluster_km'].head(20))




group_mean = gym_churn.groupby('cluster_km').mean()
print(group_mean)




plt.figure(figsize=(15,15))
sns.scatterplot(data=gym_churn,x='cluster_km',y='Age')
plt.show()




plt.figure(figsize=(15,15))
sns.scatterplot(data=gym_churn,x='cluster_km',y='Lifetime')
plt.show()




plt.figure(figsize=(15,15))
sns.scatterplot(data=gym_churn,x='cluster_km',y='Avg_additional_charges_total')
plt.show()


plt.figure(figsize=(15,15))
sns.scatterplot(data=gym_churn,x='cluster_km',y='Avg_class_frequency_total')
plt.show()


plt.figure(figsize=(15,15))
sns.scatterplot(data=gym_churn,x='cluster_km',y='Avg_class_frequency_current_month')
plt.show()

tasa_cancelacion = gym_churn.groupby('cluster_km')['Churn'].mean().reset_index()
print(tasa_cancelacion)