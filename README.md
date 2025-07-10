# 🍇 Tugas Data Mining - Klasifikasi Kualitas Anggur Merah

Proyek ini merupakan implementasi algoritma **Decision Tree Classifier** menggunakan Python untuk memprediksi kualitas anggur merah berdasarkan fitur-fitur kimia. Dataset yang digunakan berasal dari **UCI Machine Learning Repository**.

---

## 📁 Struktur Folder

tugas-data-mining-anggur

├── Data

│ └── winequality-red.csv # Dataset anggur merah

├── src

│ └── main.py # Program utama Python

├── README.md # Penjelasan proyek


---

## 📊 Dataset

Dataset: [Wine Quality - Red Wine (UCI)](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)  
Jumlah data: 1.599 sampel  
Fitur: 11 kolom input (seperti acidity, sugar, pH, alcohol)  
Label: kolom `quality` (nilai 0-10)

Contoh fitur:
- `fixed acidity`
- `volatile acidity`
- `citric acid`
- `residual sugar`
- `chlorides`
- `free sulfur dioxide`
- `total sulfur dioxide`
- `density`
- `pH`
- `sulphates`
- `alcohol`

---

## 🧠 Algoritma: Decision Tree

Langkah-langkah yang dilakukan di `main.py`:

1. Membaca dataset CSV
2. Memisahkan fitur (X) dan label (y)
3. Split data: 80% training, 20% testing
4. Latih model dengan `DecisionTreeClassifier`
5. Evaluasi model dengan akurasi

---

## ✅ Hasil Akurasi Model

Contoh hasil setelah dijalankan:

Data berhasil dibaca!

Akurasi model: 0.56


Akurasi bisa berubah tergantung hasil training.

---

## 📈 Visualisasi

Beberapa visualisasi yang ditampilkan:

- **Distribusi Kualitas Anggur:**
  Menampilkan histogram jumlah sampel untuk setiap nilai kualitas.

- **Heatmap Korelasi antar Fitur:**
  Menunjukkan korelasi antar kolom fitur untuk melihat mana yang paling berpengaruh.

---

## ▶️ Cara Menjalankan

### 1. Pastikan Python dan pustaka sudah terinstal:

```bash
pip install pandas matplotlib seaborn scikit-learn
cd src
python main.py

Visualisasi akan muncul dalam jendela grafik (matplotlib/seaborn).
```

✍️ Pembuat

Nama            : Mohammad Yoga Firnanda

NIM             : 221080200126

Tugas           : Project Data Mining untuk Memenuhi Ujian Akhir Semester

Dosen Pengampu  : Mochamad Alfan Rosid, S.Kom., M.Kom., Dr.


Referensi

UCI ML Repository - Wine Quality Dataset

Scikit-learn Documentation

