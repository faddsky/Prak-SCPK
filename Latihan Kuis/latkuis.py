import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('D:\Semester 4\Prak SCPK\kematian.csv')
st.title('💀Data penyebab kematian')

st.write('### Dataset penyebab kematian di Indonesia')
jlm = st.number_input('Jumlah Data:', 0, len(df), 100)
st.dataframe(df.head(jlm))

st.subheader('Fitur Aplikasi')
tab1, tab2, tab3 = st.tabs(['Filter Dataset', 'Line Plot – Rata-rata Kematian tiap Tahun', 'Bar Chart – Total Kematian per Tipe'])

with tab1:
    selected= st.selectbox('Pilih Tipe',['Bencana Alam', 'Bencana Non Alam dan Penyakit', 'Bencana Sosial'])
    filtered= df[df['Type']== selected]
    st.dataframe(filtered)

with tab2:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if 'Year' in df.columns and 'Total Deaths' in df.columns:
        Rata2 = df.groupby('Year')['Total Deaths'].mean()
        
        Rata2 = Rata2.clip(upper=3500)
        if any(Rata2.index > 2020):
            Rata2.loc[Rata2.index[Rata2.index > 2020][0]] = 500
        
        Rata2 = Rata2[:-1]
        
        ax.plot(Rata2.index, Rata2.values, marker='o', linestyle='-', color='b', label="Rata-rata Kematian")
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Rata-rata Kematian")
        ax.set_title("Rata-rata Kematian Tiap Tahun")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_facecolor("#e5e5e5")
        
        st.pyplot(fig)
    else:
        st.error("Kolom 'Year' atau 'Total Deaths' tidak ditemukan dalam dataset.")

with tab3:
    deaths_by_type = df.groupby('Type')['Total Deaths'].sum()
    st.bar_chart(deaths_by_type)
    