# Weather Prediction - Capstone Project

Proyek ini merupakan bagian dari Capstone Project yang bertujuan untuk membangun model prediksi kondisi cuaca berdasarkan data historis. Proyek dilakukan menggunakan dataset cuaca dari BMKG yang telah diproses dan dianalisis untuk menghasilkan model klasifikasi cuaca: cerah, mendung, dan hujan.

## 📁 Tahapan Proyek

### 1. Pengumpulan dan Penyimpanan Dataset
- Dataset cuaca diperoleh dari sumber resmi BMKG.
- Dataset diunggah ke GitHub agar mudah diakses selama pengembangan.

### 2. Import Library
- Library utama yang digunakan antara lain:  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `imbalanced-learn`, dan `tensorflow`.

### 3. Data Preparation
- Pembacaan data dan eksplorasi awal dilakukan untuk mengecek:
  - Nilai yang hilang (*missing values*)
  - Duplikasi data
  - Distribusi fitur seperti suhu, kelembapan, curah hujan, dan penyinaran matahari

### 4. Data Preprocessing
- Melakukan:
  - *Cleaning* nilai tak valid
  - *Encoding* fitur kategorikal
  - Normalisasi data numerik
  - Pembagian data menjadi training, validation, dan testing
- Menggunakan teknik **SMOTE** untuk menangani ketidakseimbangan kelas.

### 5. Exploratory Data Analysis (EDA)
- Visualisasi distribusi dan korelasi antar fitur menggunakan `matplotlib` dan `seaborn`.
- Tujuan EDA adalah untuk memahami pola dan fitur penting dalam prediksi cuaca.

### 6. Modeling
- Beberapa model diuji, di antaranya:
  - Random Forest
  - XGBoost
  - KNN
  - MLPClassifier (Scikit-learn)
  - MLPClassifier (TensorFlow)
- Evaluasi menggunakan metrik: **Accuracy, Precision, Recall, F1-Score**
- Model **MLP TensorFlow** menunjukkan hasil terbaik pada data validasi dan testing.

### 7. Inference
- Model terbaik digunakan untuk memprediksi tiga contoh data (cuaca: cerah, mendung, hujan).
- Hasil prediksi disertai probabilitas untuk tiap kelas.
- Menunjukkan model mampu melakukan prediksi dengan baik pada data nyata.

## 📊 Hasil Evaluasi

- Akurasi model terbaik (MLP TensorFlow) cukup tinggi dengan hasil yang stabil pada training dan validation.
- Disediakan juga *confusion matrix* dan *classification report* untuk masing-masing model.

## 📌 Teknologi yang Digunakan
- Python
- TensorFlow
- Scikit-learn
- imbalanced-learn (SMOTE)
- Matplotlib & Seaborn
- Jupyter Notebook
