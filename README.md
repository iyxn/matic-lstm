
# MATIC LSTM

Dashboard Harga, Peramalan Harga MATIC nggunakan model LSTM (Long Short Term Memory). Model yang digunakan dapat memprediksi satu jam kedepan.

# Fitur
## Dashboard Utama
![App Screenshot](https://raw.githubusercontent.com/iyxn/matic-lstm/main/screenshoot/home.jpg)

## Peramalan
![App Screenshot](https://raw.githubusercontent.com/iyxn/matic-lstm/main/screenshoot/forecast.jpg)


# Instalasi

Clone repository ini

```bash
  git clone https://github.com/hardianalkori/matic-lstm.git
  cd matic-lstm
```
Install library yang diperlukan
```bash
  pip install -r requirements.txt
```
Jalankan
```bash
  streamlit run "Home.py"
```
# Catatan Penting

- Butuh Koneksi Internet
-  Model di desain memprediksi 1 langkah kedepan (Hari ini)
-  Model ini menggunakan input window size 4 jam kebelakang untuk memprediksi 1 Jam Kedepan.

# To Do
- [x] Model LSTM untuk data per-jam.
- [x] Candlestick Chart.
- [ ] Model LSTM untuk data harian.
- [ ] Dashboard Performa.
