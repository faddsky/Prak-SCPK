import numpy as np
import streamlit as st
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Nama dan NIM
st.title("Tugas 4")
col1, col2 = st.columns(2)
with col1:
    st.write("Fadiah Nur Sabiyyah")
with col2:
    st.write("123230006")

# Pilihan Nomor
pilihan = st.sidebar.selectbox("Pilih Nomor", ["1", "2"])

# Logika pilihan
if pilihan == "1":
    import numpy as np
    import pandas as pd

    def calc_norm(M):
        if M.ndim == 1:
            return M / np.sum(M)
        else:
            return M / np.sum(M, axis=0)

    def calculate_ahp():
        motor_names = ['Yamaha', 'Honda', 'Suzuki', 'Kawasaki']

        with st.expander("1. Perbandingan Kriteria", expanded=True):
            MPBk = np.array([
                [1, 0.5, 3, 0.5],
                [2, 1, 4, 3],
                [1/3, 0.25, 1, 2],
                [2, 1/3, 0.5, 1]
            ])
            st.write("Matriks Perbandingan Kriteria:")
            st.write(MPBk)

            norm = calc_norm(MPBk)
            st.write("Normalisasi:")
            st.write(norm)

            V = np.sum(norm, axis=1)
            w_MPB = V / len(V)
            st.write("Eigenvector:")
            st.write(w_MPB)

        with st.expander("2. Alternatif - Gaya"):
            AKB_G = np.array([
                [1, 0.5, 2, 1/3],
                [2, 1, 3, 0.5],
                [0.5, 1/3, 1, 0.25],
                [3, 2, 4, 1]
            ])
            w_G = np.sum(calc_norm(AKB_G), axis=1) / 4
            st.write("Eigenvector Gaya:")
            st.write(w_G)

        with st.expander("3. Alternatif - Keandalan"):
            AKB_A = np.array([
                [1, 0.5, 3, 2],
                [2, 1, 4, 3],
                [1/3, 0.25, 1, 0.5],
                [0.5, 1/3, 2, 1]
            ])
            w_A = np.sum(calc_norm(AKB_A), axis=1) / 4
            st.write("Eigenvector Keandalan:")
            st.write(w_A)

        with st.expander("4. Alternatif - Keekonomisan"):
            ACM_Fe = np.array([60, 80, 60, 80])
            w_E = calc_norm(ACM_Fe)
            st.write("Normalisasi Keekonomisan:")
            st.write(w_E)

        with st.expander("5. Alternatif - Biaya"):
            costs = np.array([16, 30, 15, 40])
            w_C = calc_norm(costs)
            st.write("Normalisasi Biaya:")
            st.write(w_C)

        with st.expander("6. Jawaban Akhir dan Vektor Keputusan", expanded=True):
            W = np.column_stack((w_G, w_A, w_E, w_C))
            st.dataframe(pd.DataFrame(W, index=motor_names, columns=['Gaya', 'Keandalan', 'Keekonomisan', 'Biaya']))

            st.write("Bobot Kriteria:")
            st.dataframe(pd.DataFrame(w_MPB.reshape(1, -1), columns=['Gaya', 'Keandalan', 'Keekonomisan', 'Biaya']))

            nilai_akhir = np.dot(W, w_MPB)
            hasil = pd.DataFrame({'Motor': motor_names, 'Nilai Akhir': nilai_akhir}).sort_values('Nilai Akhir', ascending=False)
            st.dataframe(hasil)

            st.success(f"Motor terbaik adalah **{hasil.iloc[0]['Motor']}** dengan nilai akhir **{hasil.iloc[0]['Nilai Akhir']:.4f}**")

    calculate_ahp()

elif pilihan == "2":
    import numpy as np
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    import matplotlib.pyplot as plt

    def plot_trimf(var, title, output_value=None):
        fig, ax = plt.subplots()
        for term in var.terms:
            ax.plot(var.universe, var[term].mf, label=term)
        if output_value is not None:
            ax.axvline(x=output_value, color='black', linestyle='--', linewidth=2, label=f'Hasil = {output_value:.2f}')
        ax.set_title(title)
        ax.legend()
        st.pyplot(fig)

    suhu_luar = st.slider("Suhu Udara Luar (0-10):", 0.0, 10.0, 5.0)
    suhu_dalam = st.slider("Suhu Udara Dalam (0-10):", 0.0, 10.0, 5.0)
    kelembaban = st.slider("Kelembaban (0-10):", 0.0, 10.0, 5.0)

    range_input = np.arange(0, 11, 1)
    range_output = np.arange(0, 26, 1)

    suhu_udara_luar = ctrl.Antecedent(range_input, 'suhu_udara_luar')
    suhu_udara_dalam = ctrl.Antecedent(range_input, 'suhu_udara_dalam')
    kelembaban_udara_dalam = ctrl.Antecedent(range_input, 'kelembaban_udara_dalam')

    kipas_angin = ctrl.Consequent(range_output, 'kipas_angin')
    pendingin_udara = ctrl.Consequent(range_output, 'pendingin_udara')
    pemanas = ctrl.Consequent(range_output, 'pemanas')

    suhu_udara_luar['dingin'] = fuzz.trimf(suhu_udara_luar.universe, [0, 0, 5])
    suhu_udara_luar['sejuk'] = fuzz.trapmf(suhu_udara_luar.universe, [0, 4, 6, 10])
    suhu_udara_luar['hangat'] = fuzz.trimf(suhu_udara_luar.universe, [5, 10, 10])

    suhu_udara_dalam['sejuk'] = fuzz.trimf(suhu_udara_dalam.universe, [0, 0, 5])
    suhu_udara_dalam['nyaman'] = fuzz.trapmf(suhu_udara_dalam.universe, [0, 3, 7, 10])
    suhu_udara_dalam['hangat'] = fuzz.trimf(suhu_udara_dalam.universe, [5, 10, 10])

    kelembaban_udara_dalam['kering'] = fuzz.trimf(kelembaban_udara_dalam.universe, [0, 0, 5])
    kelembaban_udara_dalam['sedang'] = fuzz.trapmf(kelembaban_udara_dalam.universe, [0, 4, 6, 10])
    kelembaban_udara_dalam['lembab'] = fuzz.trimf(kelembaban_udara_dalam.universe, [5, 10, 10])

    kipas_angin['lambat'] = fuzz.trimf(kipas_angin.universe, [0, 0, 12])
    kipas_angin['sedang'] = fuzz.trimf(kipas_angin.universe, [0, 12, 25])
    kipas_angin['cepat'] = fuzz.trimf(kipas_angin.universe, [12, 25, 25])

    pendingin_udara['sedikit'] = fuzz.trimf(pendingin_udara.universe, [0, 0, 12])
    pendingin_udara['sedang'] = fuzz.trimf(pendingin_udara.universe, [0, 12, 25])
    pendingin_udara['banyak'] = fuzz.trimf(pendingin_udara.universe, [12, 25, 25])

    pemanas['rendah'] = fuzz.trimf(pemanas.universe, [0, 0, 12])
    pemanas['sedang'] = fuzz.trimf(pemanas.universe, [0, 12, 25])
    pemanas['tinggi'] = fuzz.trimf(pemanas.universe, [12, 25, 25])

    rules = [
        ctrl.Rule(suhu_udara_luar['dingin'] & suhu_udara_dalam['sejuk'] & kelembaban_udara_dalam['kering'],
                  (kipas_angin['lambat'], pendingin_udara['sedikit'], pemanas['tinggi'])),
        ctrl.Rule(suhu_udara_luar['sejuk'] & suhu_udara_dalam['nyaman'] & kelembaban_udara_dalam['sedang'],
                  (kipas_angin['sedang'], pendingin_udara['sedang'], pemanas['rendah'])),
        ctrl.Rule(suhu_udara_luar['hangat'] & suhu_udara_dalam['hangat'] & kelembaban_udara_dalam['lembab'],
                  (kipas_angin['cepat'], pendingin_udara['sedikit'], pemanas['rendah'])),
        ctrl.Rule(suhu_udara_luar['sejuk'] & suhu_udara_dalam['sejuk'] & kelembaban_udara_dalam['sedang'],
                  (kipas_angin['lambat'], pendingin_udara['banyak'], pemanas['sedang'])),
        ctrl.Rule(suhu_udara_luar['hangat'] & suhu_udara_dalam['nyaman'] & kelembaban_udara_dalam['sedang'],
                  (kipas_angin['cepat'], pendingin_udara['sedang'], pemanas['rendah']))
    ]

    control_system = ctrl.ControlSystem(rules)
    simulasi = ctrl.ControlSystemSimulation(control_system)
    simulasi.input['suhu_udara_luar'] = suhu_luar
    simulasi.input['suhu_udara_dalam'] = suhu_dalam
    simulasi.input['kelembaban_udara_dalam'] = kelembaban
    simulasi.compute()

    st.subheader("Hasil Output Sistem")
    st.write(f"**Kipas Angin:** {simulasi.output['kipas_angin']:.2f}")
    st.write(f"**Pendingin Udara:** {simulasi.output['pendingin_udara']:.2f}")
    st.write(f"**Pemanas:** {simulasi.output['pemanas']:.2f}")

    with st.expander("Visualisasi Fungsi Keanggotaan - Input"):
        col1, col2, col3 = st.columns(3)
        with col1:
            plot_trimf(suhu_udara_luar, "Suhu Udara Luar")
        with col2:
            plot_trimf(suhu_udara_dalam, "Suhu Udara Dalam")
        with col3:
            plot_trimf(kelembaban_udara_dalam, "Kelembaban Udara Dalam")

    with st.expander("Visualisasi Fungsi Keanggotaan - Output"):
        col1, col2, col3 = st.columns(3)
        with col1:
            plot_trimf(kipas_angin, "Kipas Angin", simulasi.output['kipas_angin'])
        with col2:
            plot_trimf(pendingin_udara, "Pendingin Udara", simulasi.output['pendingin_udara'])
        with col3:
            plot_trimf(pemanas, "Pemanas", simulasi.output['pemanas'])
