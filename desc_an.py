import pandas as pd 
import numpy as np
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

#load data
file='D:\\22611147\\UAS\\onlinefoods.csv'
food=pd.read_csv(file)
print(food)

#Analisis deskriptif
summary=food.describe()
print(summary)

#cek missing value
missing_value=food.isnull().sum()
print(missing_value)

#visualisasi age
usia_counts = food['Age'].value_counts().sort_index()
print(usia_counts)
plt.figure(figsize=(10, 6))
usia_counts.plot(kind='bar', color='skyblue')
plt.title('Diagram Batang Pengelompokkan Usia')
plt.xlabel('Usia')
plt.ylabel('Jumlah')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#visualisasi gender
gender_counts = food['Gender'].value_counts().sort_index()
print(gender_counts)
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Diagram Pie Gender')
plt.axis('equal')  # Membuat lingkaran terlihat lingkaran
plt.tight_layout()
plt.show()

#visualisasi status
status_counts = food['Marital Status'].value_counts().sort_index()
print(status_counts)
plt.figure(figsize=(8, 8))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Diagram Pie Gender')
plt.axis('equal')  # Membuat lingkaran terlihat lingkaran
plt.tight_layout()
plt.show()

#visualisasi occupation
occupation_counts = food['Occupation'].value_counts().sort_index()
print(occupation_counts)
plt.figure(figsize=(8, 8))
plt.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Diagram Status')
plt.axis('equal')  # Membuat lingkaran terlihat lingkaran
plt.tight_layout()
plt.show()

#visualisasi 

