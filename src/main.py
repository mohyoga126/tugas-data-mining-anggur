import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Baca data
data = pd.read_csv("../data/winequality-red.csv", sep=';')
print("Data berhasil dibaca!")

# Histogram kualitas anggur
plt.figure(figsize=(8,5))
plt.hist(data['quality'], bins=range(data['quality'].min(), data['quality'].max()+2),
         color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribusi Kualitas Anggur')
plt.xlabel('Kualitas')
plt.ylabel('Jumlah Sampel')
plt.xticks(range(data['quality'].min(), data['quality'].max()+1))
plt.grid(axis='y', alpha=0.75)
plt.show()

# Heatmap korelasi fitur
corr = data.corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap Korelasi Fitur Dataset Anggur')
plt.show()

# Scatter plot: Alcohol vs Quality
plt.figure(figsize=(8,6))
plt.scatter(data['alcohol'], data['quality'], alpha=0.6, edgecolors='w', color='green')
plt.title('Scatter Plot: Alcohol vs Quality')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.grid(True)
plt.show()

# Scatter plot: Volatile Acidity vs Quality
plt.figure(figsize=(8,6))
plt.scatter(data['volatile acidity'], data['quality'], alpha=0.6, edgecolors='w', color='red')
plt.title('Scatter Plot: Volatile Acidity vs Quality')
plt.xlabel('Volatile Acidity')
plt.ylabel('Quality')
plt.grid(True)
plt.show()

# Pisahkan fitur dan label
X = data.drop("quality", axis=1)
y = data["quality"]

# Bagi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi model:", accuracy)
