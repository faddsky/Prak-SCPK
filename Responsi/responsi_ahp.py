import numpy as np
import streamlit as st

# Fungsi Normalisasi Matriks
def calc_norm(M):
    if M.ndim == 1:  # Vektor
        sM = np.sum(M)
        return M / sM
    else:
        sM = np.sum(M, axis=0)
        return M / sM

# --- Judul Aplikasi ---
st.title("Sistem Pendukung Keputusan Pemilihan Laptop (Metode AHP)")

# --- Langkah 1: Matriks Perbandingan Kriteria ---
st.subheader("1. Matriks Perbandingan Kriteria")
MPBk = np.array([
    [1,   2/1,   3/1,   4/1,   5/1],   # CPU
    [1/2, 1,   2/1,   3/1,   4/1],   # GPU
    [1/3, 1/2, 1, 2/1, 3/1],   # Desain
    [1/4, 1/3, 1/2,   1,   2/1],   # Memory
    [1/5, 1/4, 1/3, 1/2, 1]    # Harga
])
st.write("Preferensi: CPU > GPU > Desain > RAM > Harga")
st.dataframe(MPBk)

norm_kriteria = calc_norm(MPBk)
eigen_kriteria = np.sum(norm_kriteria, axis=1) / norm_kriteria.shape[1]
st.write("Eigenvector Kriteria:")
st.write(eigen_kriteria)

# --- Langkah 2: Matriks Alternatif ---
alt = ['HP', 'Lenovo', 'Asus', 'Acer', 'Huawei']

# CPU
st.subheader("2.1. Perbandingan Alternatif - CPU")
CPU = np.array([
    [1, 2, 3, 3, 4],
    [0.5, 1, 2, 2, 3],
    [0.33, 0.5, 1, 2, 2],
    [0.33, 0.5, 0.5, 1, 2],
    [0.25, 0.33, 0.5, 0.5, 1]
])
st.dataframe(CPU)
norm_CPU = calc_norm(CPU)
eigen_CPU = np.sum(norm_CPU, axis=1) / norm_CPU.shape[1]
st.write("Eigenvector CPU:")
st.write(eigen_CPU)

# GPU
st.subheader("2.2. Perbandingan Alternatif - GPU")
GPU = np.array([
    [1,   2,   3,   3,   4],
    [0.5, 1,   2,   2,   3],
    [1/3, 0.5, 1,   2,   2],
    [1/3, 0.5, 0.5, 1,   2],
    [0.25,1/3, 0.5, 0.5, 1]
])
st.dataframe(GPU)
norm_GPU = calc_norm(GPU)
eigen_GPU = np.sum(norm_GPU, axis=1) / norm_GPU.shape[1]
st.write("Eigenvector GPU:")
st.write(eigen_GPU)

# RAM (Input Dinamis)
st.subheader("2.3. Input Alternatif - RAM (Kuantitatif)")
ram_values = []
for merk in alt:
    ram = st.number_input(f"RAM untuk {merk} (GB)", min_value=1, value=8)
    ram_values.append(ram)
RAM = np.array(ram_values)
norm_RAM = calc_norm(RAM)
st.write("Eigenvector RAM:")
st.write(norm_RAM)

# Desain
st.subheader("2.4. Perbandingan Alternatif - Desain")
Desain = np.array([
    [1, 2, 2, 3, 3],
    [0.5, 1, 1, 2, 2],
    [0.5, 1, 1, 2, 2],
    [1/3, 0.5, 0.5, 1, 1],
    [1/3, 0.5, 0.5, 1, 1]
])
st.dataframe(Desain)
norm_Desain = calc_norm(Desain)
eigen_Desain = np.sum(norm_Desain, axis=1) / norm_Desain.shape[1]
st.write("Eigenvector Desain:")
st.write(eigen_Desain)

# Harga
st.subheader("2.5. Perbandingan Alternatif - Harga")
Harga = np.array([
    [1, 0.8, 0.9, 0.7, 0.85],
    [1.25, 1, 0.89, 0.875, 0.94],
    [1.11, 1.12, 1, 0.78, 0.94],
    [1.43, 1.14, 1.28, 1, 1.21],
    [1.18, 1.06, 1.06, 0.83, 1]
])
st.dataframe(Harga)
norm_Harga = calc_norm(Harga)
eigen_Harga = np.sum(norm_Harga, axis=1) / norm_Harga.shape[1]
st.write("Eigenvector Harga:")
st.write(eigen_Harga)

# --- Langkah 3: Skor Akhir ---
st.subheader("3. Skor Akhir dan Rekomendasi")
all_eigen = np.column_stack((eigen_CPU, eigen_GPU, norm_RAM, eigen_Desain, eigen_Harga))
final_scores = np.dot(all_eigen, eigen_kriteria)

df_result = {
    'Merk': alt,
    'Skor Akhir': final_scores
}
df_result = sorted(zip(alt, final_scores), key=lambda x: x[1], reverse=True)
st.table(df_result)

best_choice = df_result[0][0]
st.success(f"Laptop terbaik berdasarkan metode AHP adalah: **{best_choice}**")
