import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

ipk = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'IPK')
penghasilan = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'Penghasilan Orang Tua')
tanggungan = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'Jumlah Tanggungan')
akademik = ctrl.Consequent(np.arange(0, 101, 1), 'Nilai Akademik')
finansial = ctrl.Consequent(np.arange(0, 101, 1), 'Kelayakan Finansial')
rekomendasi = ctrl.Consequent(np.arange(0, 101, 1), 'Rekomendasi Beasiswa')

ipk['rendah'] = fuzz.gaussmf(ipk.universe, 1.5, 0.6)
ipk['sedang'] = fuzz.gaussmf(ipk.universe, 3, 0.4)
ipk['tinggi'] = fuzz.gaussmf(ipk.universe, 4, 0.2)

penghasilan['rendah'] = fuzz.trimf(penghasilan.universe, [-1, 0, 4])
penghasilan['sedang'] = fuzz.trimf(penghasilan.universe, [2, 5, 8])
penghasilan['tinggi'] = fuzz.trimf(penghasilan.universe, [6, 10, 11])

tanggungan['sedikit'] = fuzz.trimf(tanggungan.universe, [-1, 0, 4])
tanggungan['sedang'] = fuzz.trimf(tanggungan.universe, [2, 5, 8])
tanggungan['banyak'] = fuzz.trimf(tanggungan.universe, [6, 10, 11])

akademik['rendah'] = fuzz.trimf(akademik.universe, [-1, 0, 40])
akademik['sedang'] = fuzz.trimf(akademik.universe, [30, 50, 70])
akademik['tinggi'] = fuzz.trimf(akademik.universe, [60, 100, 101])

finansial['tidak'] = fuzz.trimf(finansial.universe, [-1, 0, 40])
finansial['perlu'] = fuzz.trimf(finansial.universe, [30, 50, 70])
finansial['sangat'] = fuzz.trimf(finansial.universe, [60, 100, 101])

rekomendasi['kurang_layak'] = fuzz.trimf(rekomendasi.universe, [-1, 0, 40])
rekomendasi['dipertimbangkan'] = fuzz.trimf(rekomendasi.universe, [30, 50, 70])
rekomendasi['sangat_layak'] = fuzz.trimf(rekomendasi.universe, [60, 100, 101])

rules = [
    ctrl.Rule(ipk['tinggi'] & penghasilan['rendah'] & tanggungan['banyak'], 
              consequent=(akademik['tinggi'], finansial['sangat'], rekomendasi['sangat_layak'])),
    ctrl.Rule(ipk['tinggi'] & penghasilan['tinggi'] & tanggungan['sedikit'],
              consequent=(akademik['tinggi'], finansial['tidak'], rekomendasi['kurang_layak'])),
    ctrl.Rule(ipk['sedang'] & penghasilan['sedang'] & tanggungan['sedang'],
              consequent=(akademik['sedang'], finansial['perlu'], rekomendasi['dipertimbangkan'])),
    ctrl.Rule(ipk['rendah'] & penghasilan['tinggi'] & tanggungan['sedikit'],
              consequent=(akademik['rendah'], finansial['tidak'], rekomendasi['kurang_layak'])),
    ctrl.Rule(ipk['rendah'] & penghasilan['rendah'] & tanggungan['banyak'],
              consequent=(akademik['rendah'], finansial['sangat'], rekomendasi['dipertimbangkan'])),
    ctrl.Rule(ipk['sedang'] & penghasilan['rendah'] & tanggungan['banyak'],
              consequent=(akademik['sedang'], finansial['sangat'], rekomendasi['sangat_layak'])),
    ctrl.Rule(ipk['tinggi'] & penghasilan['sedang'] & tanggungan['sedang'],
              consequent=(akademik['tinggi'], finansial['perlu'], rekomendasi['sangat_layak'])),
    ctrl.Rule(ipk['rendah'] & penghasilan['sedang'] & tanggungan['sedang'],
              consequent=(akademik['rendah'], finansial['perlu'], rekomendasi['kurang_layak'])),
    ctrl.Rule(ipk['sedang'] & penghasilan['tinggi'] & tanggungan['sedikit'],
              consequent=(akademik['sedang'], finansial['tidak'], rekomendasi['dipertimbangkan'])),         
]

beasiswa_ctrl = ctrl.ControlSystem(rules)
beasiswa = ctrl.ControlSystemSimulation(beasiswa_ctrl)

st.title("👩‍🎓Sistem Fuzzy: Rekomendasi Penerima Beasiswa👩‍🎓")
st.write("Nama: Fadilah  Nur Sabiyyah")
st.write("NIM: 123230006")
ipk_input = st.slider("IPK (0-4)📚", 0.0, 4.0, 2.5, 0.1)
penghasilan_input = st.slider("Penghasilan Orang Tua (0-10)💸", 0.0, 10.0, 5.0, 0.1)
tanggungan_input = st.slider("Jumlah Tanggungan(0-10)🧍‍♀️", 0.0, 10.0, 3.0, 1.0)

beasiswa.input['IPK'] = ipk_input
beasiswa.input['Penghasilan Orang Tua'] = penghasilan_input
beasiswa.input['Jumlah Tanggungan'] = tanggungan_input
beasiswa.compute()

st.write("Hasil Perhitungan📝:")
st.write(f"Nilai Akademik: {beasiswa.output['Nilai Akademik']:.2f}")
st.write(f"Kelayakan Finansial: {beasiswa.output['Kelayakan Finansial']:.2f}")
st.write(f"Rekomendasi Beasiswa: {beasiswa.output['Rekomendasi Beasiswa']:.2f}")

def plot_membership(var, title):
    fig, ax = plt.subplots()
    for label in var.terms:
        ax.plot(var.universe, var[label].mf, label=label)
    ax.set_title(f"Fungsi Keanggotaan {title}")
    ax.set_xlabel(title)
    ax.set_ylabel('Derajat Keanggotaan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['IPK', 'Penghasilan Orang Tua', 'Jumlah Tanggungan', 'Nilai Akademik', 'Kelayakan Finansial', 'Rekomendasi Beasiswa'])
with tab1:
    plot_membership(ipk, "IPK")
with tab2:
    plot_membership(penghasilan, "Penghasilan Orang Tua")
with tab3:
    plot_membership(tanggungan, "Jumlah Tanggungan")
with tab4:
    plot_membership(akademik, "Nilai Akademik")
with tab5:
    plot_membership(finansial, "Kelayakan Finansial")
with tab6:
    plot_membership(rekomendasi, "Rekomendasi Beasiswa")