import streamlit as st
import pandas as pd

st.title('Ini Judul')
st.header('Ini Header')
st.text('Ini Text')

st.write('## Ini Write **Bold** *Italic*')

df = {
    'Nama': ['Ion','Havas','Yon'],
    'Umur': [10,15,50],
    'Asal': ['Sleman','Condongcatur','Seturan']
} 
st.write('Contoh Dataframe')
st.dataframe(df)

st.write('Ini Tombol')
if st.button('Tombol Nuklir'):
    st.write('DUAR')

st.write('Slider')
st.slider('Nilai',0,100,45)

st.write('Masukkan Nilai')
nilai = st.number_input('Nilai',0,100,10)
st.write(nilai)

st.write('Select Box')
st.selectbox('Kota', ['Jogja', 'Jakarta', 'Bandung'], 2)

st.write('Teks Input')
st.text_input('Masukkan kata : ', placeholder='masukkan')

st.write('Status')
st.success('Berhasil')
st.error('Gagal')

st.write('Text Area')
st.text_area('Masukkan Kata', placeholder='masukkan')

st.write('Column')
col1, col2 = st.columns(2)
with col1:
    st.write('Ini Col 1')
with col2:
    st.write('Ini Col 2')

st.write('Expander')
with st.expander('Lihat Detail'):
    st.write('lorem ipsum')
    st.text_input('Masukkan Kata', placeholder='masukkan')

st.write('Ini Tabs')
tab1, tab2 = st.tabs(['Informasi', 'Visualisasi'])
with tab1:
    st.write('Ini Tab 1')
    st.write('lorem')
with tab2:
    st.write('Ini tab 2')
    st.write('ipsum')