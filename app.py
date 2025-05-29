# Import library yang diperlukan
from flask import Flask, request, jsonify  # Flask untuk API
import numpy as np                        # Untuk manipulasi array numerik
import tensorflow as tf                   # Untuk memuat model TensorFlow
import joblib                             # Untuk memuat scaler dan label encoder

# ======================
# 🔁 Load Model dan Preprocessing
# ======================

# Memuat model prediksi cuaca (.h5) hasil training
model = tf.keras.models.load_model("model_tf_weather.h5")

# Memuat scaler untuk normalisasi data input (hasil training)
scaler = joblib.load("scaler.save")

# Memuat label encoder untuk mengubah output angka menjadi label 'cerah', 'mendung', atau 'hujan'
label_encoder = joblib.load("label_encoder.save")

# ======================
# 🚀 Inisialisasi Aplikasi Flask
# ======================
app = Flask(__name__)

# Endpoint utama untuk cek apakah API aktif
@app.route('/')
def home():
    return "Weather Prediction API Aktif!"

# ======================
# 🔮 Endpoint Prediksi Cuaca
# ======================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data dari request JSON dengan key 'data'
        data = request.json['data']

        # Ubah data menjadi array NumPy
        data_np = np.array(data)

        # Normalisasi data menggunakan scaler yang sama seperti saat training
        data_scaled = scaler.transform(data_np)

        # Lakukan prediksi probabilitas dari model
        probs = model.predict(data_scaled)

        # Ambil indeks kelas dengan probabilitas tertinggi
        classes = np.argmax(probs, axis=1)

        # Ubah hasil prediksi angka menjadi label (cerah/mendung/hujan)
        labels = label_encoder.inverse_transform(classes)

        # Susun hasil akhir dalam format JSON
        result = [
            {
                "label": labels[i],
                "probability": probs[i].tolist()
            }
            for i in range(len(labels))
        ]

        return jsonify({"result": result})

    except Exception as e:
        # Tangani jika terjadi error saat prediksi
        return jsonify({"error": str(e)})

# ======================
# ▶️ Menjalankan Aplikasi
# ======================
if __name__ == '__main__':
    # Jalankan Flask di localhost:5000, debug=True untuk pengembangan
    app.run(debug=True)
