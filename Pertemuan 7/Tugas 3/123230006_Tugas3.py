import streamlit as st
import pandas as pd
import numpy as np

st.title('Tugas 3 - SPK dengan WP')
st.subheader('123230006 - Fadilah Nur Sabiyyah')
st.write('#### Dataframe')

tab1, tab2, tab3 = st.tabs(['Kriteria', 'Alternatif', 'Matrix'])

# Tab Kriteria
with tab1:
    jumlah_kriteria = st.number_input("Masukkan jumlah kriteria:", min_value=1, step=1, value=1)
    
    if 'nama_kriteria' not in st.session_state or len(st.session_state.nama_kriteria) != jumlah_kriteria:
        st.session_state.nama_kriteria = [""] * jumlah_kriteria
        st.session_state.bobot_kriteria = [1] * jumlah_kriteria
        st.session_state.keterangan_kriteria = ["Benefit"] * jumlah_kriteria
    
    for i in range(jumlah_kriteria):
        col1, col2, col3 = st.columns([2, 2, 2])
        with col1:
            nama = st.text_input(f"Kriteria {i+1}", key=f"nama_{i}")
            st.session_state.nama_kriteria[i] = nama

            label_bobot = f"Bobot {nama}" if nama else "Bobot"
            label_keterangan = f"Keterangan {nama}" if nama else "Keterangan"
            
        with col2:
            bobot = st.number_input(label_bobot, min_value=0, step=1, value=1, key=f"bobot_{i}")
            st.session_state.bobot_kriteria[i] = bobot

        with col3:
            keterangan = st.selectbox(label_keterangan, ["Benefit", "Cost"], key=f"keterangan_{i}")
            st.session_state.keterangan_kriteria[i] = keterangan

# Tab Alternatif
with tab2:
    jumlah_alternatif = st.number_input("Masukkan jumlah alternatif:", min_value=1, step=1, value=1)

    if 'nama_alternatif' not in st.session_state or len(st.session_state.nama_alternatif) != jumlah_alternatif:
        st.session_state.nama_alternatif = [""] * jumlah_alternatif

    for i in range(jumlah_alternatif):
        nama = st.text_input(f"Alternatif {i+1}", key=f"alt_{i}")
        st.session_state.nama_alternatif[i] = nama

# Tab Matrix
with tab3:
    st.write("Matriks Alternatif")

    nama_kriteria = st.session_state.nama_kriteria
    bobot_kriteria = st.session_state.bobot_kriteria

    header = [f"{nama_kriteria[i]} ({bobot_kriteria[i]})" for i in range(jumlah_kriteria)]

    nilai_matriks = {}
    col_widths = [1.5] + [2 for _ in range(jumlah_kriteria)]
    cols = st.columns(col_widths)

    with cols[0]:
        st.markdown("**Alternatif**")
    for j in range(jumlah_kriteria):
        with cols[j+1]:
            st.markdown(f"**{header[j]}**")

    for i in range(jumlah_alternatif):
        cols = st.columns(col_widths)
        with cols[0]:
            st.markdown(f"**{st.session_state.nama_alternatif[i]}**")
        for j in range(jumlah_kriteria):
            with cols[j+1]:
                label = f"{i},{j}"
                st.markdown(label)
                
                key = f"nilai_{i}_{j}"
                nilai = st.number_input("", 
                                      key=key, 
                                      format="%.2f",
                                      value=0.00,
                                      step=1.00,
                                      label_visibility="collapsed")
                nilai_matriks[(i, j)] = nilai

if st.button('Buat Data Frame', key='btn_df_all_tabs'):
    data = []
    for i in range(jumlah_alternatif):
        row = [st.session_state.nama_alternatif[i]]  
        for j in range(jumlah_kriteria):  
            row.append(nilai_matriks.get((i, j), 0.00))
        data.append(row)  
    
    columns = ['Alternatif'] + nama_kriteria
    df = pd.DataFrame(data, columns=columns)
    
    total_bobot = sum(bobot_kriteria)
    normalized_weights = [b/total_bobot for b in bobot_kriteria]
    
    st.session_state.df = df
    st.session_state.normalized_weights = normalized_weights
    
    st.write("### Dataframe Hasil Input")
    st.dataframe(df, hide_index=True)  


if st.button('Find Best Alternative', key='btn_best_all_tabs'):
    if 'df' not in st.session_state:
        st.warning("Harap buat dataframe terlebih dahulu")
    else:
        df = st.session_state.df
        normalized_weights = st.session_state.normalized_weights
        keterangan_kriteria = st.session_state.keterangan_kriteria
        nama_kriteria = st.session_state.nama_kriteria
        bobot_kriteria = st.session_state.bobot_kriteria
        jumlah_alternatif = len(st.session_state.nama_alternatif)
        jumlah_kriteria = len(nama_kriteria)

        # Hitung vektor S
        s_vector = []
        for i in range(jumlah_alternatif):
            product = 1.0
            for j in range(jumlah_kriteria):
                value = df.iloc[i, j+1]  # Kolom ke-(j+1) karena kolom ke-0 biasanya nama alternatif
                weight = normalized_weights[j]
                if keterangan_kriteria[j] == "Benefit":
                    product *= (value ** weight)
                else:  # Cost
                    product *= (value ** (-weight))
            s_vector.append(product)

        # Hitung vektor V
        total_s = sum(s_vector)
        v_vector = [s / total_s for s in s_vector]

        # Cari alternatif terbaik
        best_index = np.argmax(v_vector)
        best_alternative = st.session_state.nama_alternatif[best_index]
        best_score = v_vector[best_index]

        st.write("### Hasil Perhitungan")

        # Tampilkan normalized weights
        df_weights = pd.DataFrame({
            'Kriteria': nama_kriteria,
            'Normalized Weight': normalized_weights
        })
        st.write("#### Normalized Weights:")
        st.dataframe(df_weights, hide_index=True)

        # Tampilkan vektor S
        df_s = pd.DataFrame({
            'Alternatif': st.session_state.nama_alternatif,
            'Vektor S': s_vector
        })
        st.write("#### Vektor S:")
        st.dataframe(df_s, hide_index=True)

        # Tampilkan vektor V
        df_v = pd.DataFrame({
            'Alternatif': st.session_state.nama_alternatif,
            'Vektor V': v_vector
        })
        st.write("#### Vektor V:")
        st.dataframe(df_v, hide_index=True)

        # Tampilkan alternatif terbaik
        st.write(f"Alternatif terbaik adalah: {best_alternative}")
