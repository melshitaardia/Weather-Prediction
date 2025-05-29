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

### 6. Pemodelan
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

### 🚀 8. Deployment

Model yang telah dilatih dan disimpan (`model_tf_weather.h5`) di-*deploy* dalam bentuk REST API menggunakan **Flask**. API ini memungkinkan pengguna untuk mengirim data cuaca dalam format JSON dan menerima prediksi kondisi cuaca sebagai respons.

#### 🔧 Teknologi
- Flask (untuk membuat REST API)
- TensorFlow (untuk model prediksi)
- Joblib (untuk menyimpan dan memuat preprocessing: `scaler`, `label_encoder`)

#### 📥 Input API (`POST /predict`)
```json
{
  "data": [[
    28.5, 34.0, 25.1, // suhu: rata-rata, max, min
    78.2,             // kelembapan
    4.3,              // curah hujan
    6.8,              // lama penyinaran matahari
    9.2, 5.5,         // kecepatan angin max, rata-rata
    180.0             // ← contoh fitur ke-9 (misalnya arah angin atau lainnya)
  ]]
}
```
### 📌 Langkah Menjalankan API
jalankan dan simpan model dan preprocessing:
 - model.save("model_tf_weather.h5")
 - joblib.dump(scaler, "scaler.save")
 - joblib.dump(label_encoder, "label_encoder.save")
cukup dengan menjalankan file Weather Prediction_Capstone Project.ipynb

Jalankan file app.py di terminal:
python app.py

setelah local host aktif kita uji dengan sampe data dari json yang udah kita buat dengan perintah berikut:
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @sample.json

maka output akan menampilkan hasil dari model

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
