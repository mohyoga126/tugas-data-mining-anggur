````markdown
# Proyek Klasifikasi Kualitas Anggur

## Deskripsi Proyek
Proyek ini bertujuan untuk membangun model machine learning yang dapat mengklasifikasikan kualitas anggur merah berdasarkan beberapa fitur kimiawi menggunakan dataset Wine Quality (red wine). Model yang dibangun menggunakan Decision Tree Classifier untuk memprediksi kualitas berdasarkan fitur-fitur seperti kadar alkohol, keasaman, pH, dan lainnya.

## Dataset
Dataset yang digunakan adalah `winequality-red.csv`, yang berisi 1599 sampel anggur merah dengan 12 kolom, yaitu 11 fitur kimiawi dan 1 label kualitas (`quality`). Label kualitas merupakan skor numerik yang menunjukkan mutu anggur, biasanya dalam rentang 3 sampai 8.

### Fitur dalam dataset:
- fixed acidity  
- volatile acidity  
- citric acid  
- residual sugar  
- chlorides  
- free sulfur dioxide  
- total sulfur dioxide  
- density  
- pH  
- sulphates  
- alcohol  

## Metode
- Dataset dibagi menjadi data latih dan data uji dengan perbandingan 80:20 menggunakan `train_test_split` dari scikit-learn.  
- Model yang digunakan adalah Decision Tree Classifier, yang dilatih pada data latih dan diuji pada data uji.  
- Evaluasi model dilakukan menggunakan metrik akurasi, yang menunjukkan persentase prediksi benar dari total data uji.

## Visualisasi Data
Untuk memberikan gambaran lebih baik mengenai data, beberapa visualisasi dibuat:
- **Histogram distribusi kualitas anggur:** Menampilkan sebaran jumlah sampel berdasarkan nilai kualitasnya.  
- **Heatmap korelasi fitur:** Menunjukkan hubungan positif atau negatif antar fitur dalam dataset.  
- **Scatter plot:** Memvisualisasikan hubungan dua fitur penting (`alcohol` dan `volatile acidity`) dengan kualitas anggur.

## Hasil
Model Decision Tree berhasil mencapai akurasi sekitar **56%** pada data uji, menunjukkan kemampuan model dalam mengklasifikasikan kualitas anggur berdasarkan fitur-fitur kimiawi.

## Cara Menjalankan Proyek

### Persyaratan
Pastikan Python sudah terinstall, serta beberapa package berikut:

```bash
pip install pandas matplotlib seaborn scikit-learn
````

### Langkah menjalankan

1. Pastikan file dataset `winequality-red.csv` berada di folder `data/`.
2. Jalankan script Python utama:

```bash
python src/main.py
```

Script akan melakukan:

* Membaca dataset
* Menampilkan histogram kualitas
* Menampilkan heatmap korelasi fitur
* Menampilkan scatter plot `alcohol` vs `quality` dan `volatile acidity` vs `quality`
* Melatih model Decision Tree
* Menampilkan akurasi model

## Struktur Folder Proyek

```
project-folder/
│
├─ data/
│   └─ winequality-red.csv
├─ src/
│   └─ main.py
├─ README.md
```

## Penulis

Mohammad Yoga Firnanda - 221080200126

---

## Referensi

* [Wine Quality Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)
* Dokumentasi [scikit-learn Decision Tree Classifier](https://scikit-learn.org/stable/modules/tree.html)
* Dokumentasi [matplotlib](https://matplotlib.org/) dan [seaborn](https://seaborn.pydata.org/)

---

## Catatan

Proyek ini dapat dikembangkan lebih lanjut dengan mencoba algoritma lain seperti Random Forest, SVM, atau tuning hyperparameter untuk meningkatkan performa model.

---

Jika ada pertanyaan atau butuh bantuan, silakan hubungi saya.
Terima kasih sudah melihat proyek ini!

```
