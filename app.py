import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Konfigurasi Tampilan
st.set_page_config(page_title="DigiDakwah App", page_icon="🌙", layout="centered")

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #27ae60; color: white; }
    .quote-box { padding: 20px; border-left: 5px solid #27ae60; background-color: #e8f5e9; font-style: italic; }
    </style>
    """, unsafe_allow_stdio=True)

# 2. Header & Kutipan
st.title("🌙 DigiDakwah")
st.subheader("Platform Dakwah Digital Berbasis Data")
st.markdown('<div class="quote-box">"Sampaikanlah dariku walau hanya satu ayat." (HR. Bukhari)</div>', unsafe_allow_stdio=True)

# 3. Navigasi Menu
menu = ["Home & Materi", "Video Kajian", "Tanya Ustadz (Admin)"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

# --- MENU 1: HOME & MATERI ---
if choice == "Home & Materi":
    st.header("Daftar Materi Dakwah")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Fikih Ibadah**\n\nPanduan salat di era digital.")
    with col2:
        st.info("**Adab Medsos**\n\nMenjaga lisan dalam ketikan.")
    
    st.write("### Tentang Program")
    st.write("Aplikasi ini menggunakan teknologi Python dan Pandas untuk mengelola data pertanyaan jemaah secara sistematis.")

# --- MENU 2: VIDEO KAJIAN ---
elif choice == "Video Kajian":
    st.header("Video Kajian Terbaru")
    st.video("https://www.youtube.com/watch?v=zPrS0A6r_hM") # Kamu bisa ganti link ini
    st.caption("Kajian Singkat: Adab Menuntut Ilmu")

# --- MENU 3: TANYA USTADZ ---
elif choice == "Tanya Ustadz (Admin)":
    st.header("Form Tanya Ustadz")
    
    # Database CSV Sederhana
    DB_FILE = "data_dakwah.csv"
    
    # Fungsi Load Data
    def load_data():
        if os.path.exists(DB_FILE):
            return pd.read_csv(DB_FILE)
        else:
            return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])

    # Form Input
    with st.form(key='tanya_form', clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("WhatsApp/Email")
        pertanyaan = st.text_area("Tulis Pertanyaan Anda")
        submit = st.form_submit_button("Kirim Ke Database")

    if submit:
        if nama and pertanyaan:
            new_data = {
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Nama": nama,
                "Kontak": kontak,
                "Pertanyaan": pertanyaan
            }
            df = load_data()
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("Data berhasil disimpan ke CSV!")
        else:
            st.warning("Mohon isi nama dan pertanyaan.")

    # Menampilkan Tabel Data (Hanya muncul di menu Admin)
    st.divider()
    st.subheader("Data Pertanyaan Masuk (Database CSV)")
    df_display = load_data()
    st.dataframe(df_display, use_container_width=True)