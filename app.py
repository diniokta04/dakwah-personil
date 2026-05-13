import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="DigiDakwah App", page_icon="🌙", layout="centered")

# 2. CUSTOM CSS (Mempercantik UI)
st.markdown("""
    <style>
    /* Mengubah font dan background utama */
    .main { background-color: #f8f9fa; }
    
    /* Styling Kartu Materi */
    .materi-card {
        background-color: white; 
        padding: 25px; 
        border-radius: 15px; 
        border-top: 6px solid #27ae60; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
        height: 220px;
        transition: transform 0.3s;
    }
    .materi-card:hover {
        transform: translateY(-5px);
    }
    
    /* Styling Tombol */
    .stButton>button {
        width: 100%;
        background-color: #27ae60;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
    
    /* Quote Box */
    .quote-box {
        padding: 20px; 
        border-left: 5px solid #27ae60; 
        background-color: #e8f5e9; 
        font-style: italic; 
        border-radius: 0 10px 10px 0;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004613.png", width=100) # Icon islami
    st.title("Navigasi")
    menu = ["🏠 Home & Materi", "📺 Video Kajian", "📝 Tanya Ustadz"]
    choice = st.selectbox("Pilih Halaman:", menu)
    st.divider()
    st.caption("DigiDakwah v1.0 - Tugas Informatika")

# --- MENU 1: HOME & MATERI ---
if choice == "🏠 Home & Materi":
    # Hero Section
    st.markdown("""
        <div style="background-color:#27ae60; padding:30px; border-radius:15px; margin-bottom:25px; text-align:center;">
            <h1 style="color:white; margin:0;">🌙 DigiDakwah</h1>
            <p style="color:white; opacity:0.9; font-size:18px;">Platform Dakwah Digital Berbasis Data</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="quote-box">"Sampaikanlah dariku walau hanya satu ayat." (HR. Bukhari)</div>', unsafe_allow_html=True)

    st.subheader("📚 Daftar Materi Unggulan")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="materi-card">
                <h3 style="color:#27ae60;">📖 Fikih Ibadah</h3>
                <p style="color:#5f6368; font-size:15px;">
                Panduan praktis tata cara ibadah salat, thaharah, dan puasa yang disesuaikan dengan tantangan di era digital.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="materi-card" style="border-top-color: #e67e22;">
                <h3 style="color:#e67e22;">📱 Adab Medsos</h3>
                <p style="color:#5f6368; font-size:15px;">
                Edukasi pentingnya menjaga lisan dan etika dalam berkomunikasi di ruang publik virtual sesuai syariat Islam.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    # Tentang Program
    with st.expander("✨ Tentang Program DigiDakwah", expanded=True):
        st.write("""
            Aplikasi ini dirancang untuk mengintegrasikan nilai-nilai dakwah dengan efisiensi teknologi modern. 
            Menggunakan **Python** sebagai mesin utama dan **Pandas** untuk manajemen data pertanyaan jemaah.
        """)

# --- MENU 2: VIDEO KAJIAN ---
elif choice == "Video Kajian":
    st.header("📺 Video Kajian Terbaru")
    st.markdown("Tonton kajian singkat untuk menyejukkan hati hari ini.")
    
    # Video Card
    st.video("https://www.youtube.com/watch?v=zPrS0A6r_hM")
    st.info("**Judul:** Adab Menuntut Ilmu dalam Islam")

# --- MENU 3: TANYA USTADZ ---
elif choice == "Tanya Ustadz":
    st.header("Form Tanya Ustadz")
    st.write("Silakan ajukan pertanyaan Anda, data akan tersimpan secara sistematis.")
    
    DB_FILE = "data_dakwah.csv"
    
    def load_data():
        if os.path.exists(DB_FILE):
            try:
                return pd.read_csv(DB_FILE)
            except:
                return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])
        else:
            return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])

    # UI Form yang rapi
    with st.container():
        with st.form(key='tanya_form', clear_on_submit=True):
            nama = st.text_input("Nama Lengkap")
            kontak = st.text_input("WhatsApp / Email")
            pertanyaan = st.text_area("Apa yang ingin Anda tanyakan?")
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
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("✅ Alhamdulillah, pertanyaan Anda telah tersimpan di database!")
            st.rerun()
        else:
            st.error("⚠️ Mohon isi Nama dan Pertanyaan terlebih dahulu.")

    # Tampilan Tabel Admin
    st.divider()
    st.subheader("📊 Data Pertanyaan Masuk")
    df_display = load_data()
    if not df_display.empty:
        st.dataframe(df_display, use_container_width=True)
    else:
        st.write("Belum ada data pertanyaan.")
