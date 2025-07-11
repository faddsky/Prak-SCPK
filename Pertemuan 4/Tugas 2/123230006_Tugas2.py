import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("D:\Semester 4\Prak SCPK\community.csv")

df = load_data()

nilai = st.sidebar.number_input('Jumlah data yang ditampilkan', 0, 555, 10)

st.title("Aplikasi Eksplorasi Dataset Community")
st.write("Menyajikan dataset iris secara interaktif")
st.subheader("Dataset Community")
st.dataframe(df.head(nilai))

st.subheader("Statistik Deskriptif")
st.write('Expander')
with st.expander('Lihat Detail'):
    st.write(f"Dimensi Dataset: {df.shape}")
    st.write("Dimensi Statistik:")
    st.write(df.describe())
    st.write("Missing Values:")
    st.write(df.isnull().sum())

st.subheader("Visualisasi Data")
tab1, tab2 = st.tabs(['Age', 'Height'])

with tab1:
    st.subheader("Line Plot - Age per Index")
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    benua_list = ["Australia", "Europe", "South America", "Africa", "Asia", "North America"]
    colors = ["#FF0000", "#008000", "#0000FF", "#00FFFF", "#FF00FF", "#FFFF00"]
  
    
    for ax, benua, color in zip(axes.flatten(), benua_list, colors):
        subset = df[df["Continent"] == benua]  
        if not subset.empty:
            ax.plot(subset.index, subset["Age"], marker='o', linestyle='-', color=color, label=benua)
            ax.set_title(benua)
            ax.legend(loc='upper left')
            ax.grid(True)
    
    plt.tight_layout(pad=3.0)  
    st.pyplot(fig)

with tab2:
    st.subheader("Line Plot - Height per Index")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for benua in benua_list:
        subset = df[df["Continent"] == benua] 
        if not subset.empty:
            ax.plot(subset.index, subset["Height"], marker='o', linestyle='-', label=benua)
    
    ax.set_title("Line Plot - Height per Index")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)