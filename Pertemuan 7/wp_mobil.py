import numpy as np
import pandas as pd

# Data Alternatif dan Kriteria (Contoh)
alternatives = ['Mobil A', 'Mobil B', 'Mobil C']
criteria = ['Harga', 'Efisiensi Bahan Bakar', 'Kekuatan Mesin']

# Data yang dimasukkan oleh pengguna
# Harga (Juta), Efisiensi Bahan Bakar (km/l), Kekuatan Mesin (HP)
data = np.array([
    [300, 15, 150],  # Mobil A
    [250, 18, 180],  # Mobil B
    [350, 12, 160]   # Mobil C
])

# Penentuan Benefit/cost tiap kriteria
# Benefit = 1, Cost = -1
k = [-1, 1, 1]

# Bobot Tiap Kriteria
weights = [5, 4, 4]

# Matriks Keputusan
df = pd.DataFrame(data, index=alternatives, columns=criteria)
print("Matriks Keputusan:")
print(df)

# Normalisasi Nilai Bobot
# Ambil dimensi dari matriks keputusan
# m = Jumlah alternatif, n = Jumlah kriteria
m = len(data)
n = len(data[0])

# Normalisasi bobot kriteria
weights_norm = [data/sum(weights) for data in weights]
print("\nNormalisasi Bobot:")
print(weights_norm)

# Menghitung Vektor S
s = []
for i in range(m):
    s_value = 1
    for j in range(n):
        s_value *= data[i][j] **  (k[j] * weights_norm[j])
    s.append(s_value)

# Menyajikan hasil Vektor S dalam bentuk tabel
s_df = pd.DataFrame(s, index=alternatives, columns=["Vektor S"])
print("\nVektor S:")
print(s_df)

# Menghitung Vektor V untuk mencari nilai Terbaik
total_s = sum(s)
v = [s_value / total_s for s_value in s]

# Menyajikan hasil Vektor V dalam bentuk tabel
v_df = pd.DataFrame(v, index=alternatives, columns=["Vektor V"])
print("\nVektor V:")
print(v_df)

# Menentukan Alternatif Terbaik
best_alternative = alternatives[v.index(max(v))]
print(f"\nAlternatif terbaik adalah: {best_alternative}")