import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- MENU 1: HOME & MATERI ---
if choice == "Home & Materi":
    # Membuat Header yang lebih menarik
    st.markdown("""
        <div style="background-color:#27ae60; padding:20px; border-radius:10px; margin-bottom:25px">
            <h1 style="color:white; text-align:center; margin:0;">Daftar Materi Dakwah</h1>
            <p style="color:white; text-align:center; opacity:0.9;">Tingkatkan Ilmu, Perbaiki Adab di Era Digital</p>
        </div>
    """, unsafe_allow_html=True)

    # Menggunakan columns untuk tampilan kartu materi
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style="background-color:white; padding:20px; border-radius:10px; border-top: 5px solid #2ecc71; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); height: 180px;">
                <h3 style="color:#2c3e50; margin-top:0;">📖 Fikih Ibadah</h3>
                <p style="color:#7f8c8d; font-size:14px;">Pelajari tata cara ibadah yang benar dengan panduan praktis sesuai sunnah untuk kaum muslimin di era digital.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background-color:white; padding:20px; border-radius:10px; border-top: 5px solid #e67e22; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); height: 180px;">
                <h3 style="color:#2c3e50; margin-top:0;">📱 Adab Medsos</h3>
                <p style="color:#7f8c8d; font-size:14px;">Menjaga lisan dalam ketikan. Panduan bijak berinteraksi di ruang publik virtual sesuai tuntunan Islam.</p>
            </div>
        """, unsafe_allow_html=True)

    # Memberikan ruang kosong
    st.write("#")
    
    # Bagian Tentang Program dengan tampilan Box yang rapi
    with st.expander("✨ Tentang Program DigiDakwah", expanded=True):
        st.write("""
            Aplikasi ini dirancang khusus untuk mengintegrasikan nilai-nilai dakwah dengan efisiensi teknologi. 
            Dengan memanfaatkan **Python** sebagai mesin utama dan **Pandas** untuk manajemen data, 
            setiap pertanyaan jemaah dikelola secara sistematis guna memastikan pelayanan dakwah yang responsif dan terukur.
        """)
        st.caption("Versi 1.0.0 | Dikembangkan untuk Tugas Informatika")
# 3. Navigasi Menu
menu = ["Home & Materi", "Video Kajian", "Tanya Ustadz"]
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
    # Kamu bisa ganti link ini dengan video dakwah favoritmu
    st.video("https://www.youtube.com/watch?v=zPrS0A6r_hM") 
    st.caption("Kajian Singkat: Adab Menuntut Ilmu")

# --- MENU 3: TANYA USTADZ ---
elif choice == "Tanya Ustadz":
    st.header("Form Tanya Ustadz")
    
    # Database CSV Sederhana
    DB_FILE = "data_dakwah.csv"
    
    # Fungsi Load Data
    def load_data():
        if os.path.exists(DB_FILE):
            try:
                return pd.read_csv(DB_FILE)
            except:
                # Jika file rusak/kosong, buat baru
                return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])
        else:
            return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])

    # Form Input
    with st.form(key='tanya_form', clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("WhatsApp/Email")
        pertanyaan = st.text_area("Tulis Pertanyaan Anda")
        submit = st.form_submit_button("Kirim")

    if submit:
        if nama and pertanyaan:
            new_data = {
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Nama": nama,
                "Kontak": kontak,
                "Pertanyaan": pertanyaan
            }
            df = load_data()
            # Gunakan pd.DataFrame([new_data]) untuk menggabungkan data baru
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("Alhamdulillah, data berhasil disimpan!")
            st.rerun() # Refresh agar data terbaru langsung muncul di tabel
        else:
            st.warning("Mohon isi nama dan pertanyaan.")

    # Menampilkan Tabel Data
    st.divider()
    st.subheader("Data Pertanyaan Masuk (Database CSV)")
    df_display = load_data()
    st.dataframe(df_display, use_container_width=True)
