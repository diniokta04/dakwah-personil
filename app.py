import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="DigiDakwah - Oratorium Saintek", page_icon="🌙", layout="centered")

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .materi-card {
        background-color: white; 
        padding: 25px; 
        border-radius: 15px; 
        border-top: 6px solid #27ae60; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
        height: 220px;
        transition: transform 0.3s;
    }
    .materi-card:hover { transform: translateY(-5px); }
    .stButton>button {
        width: 100%; background-color: #27ae60; color: white;
        border-radius: 10px; border: none; padding: 10px; font-weight: bold;
    }
    .quote-box {
        padding: 20px; border-left: 5px solid #27ae60; 
        background-color: #e8f5e9; font-style: italic; 
        border-radius: 0 10px 10px 0; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004613.png", width=100)
    st.title("DigiDakwah")
    menu = ["🏠 Home & Materi", "📺 Video Kajian", "📝 Tanya Ustadz"]
    choice = st.selectbox("Pilih Halaman:", menu)
    st.divider()
    st.info("**Narasumber:**\nAsatidz Oratorium Saintek UMSIDA")
    st.caption("Developed by Dini Oktabiyanti - Informatika UMSIDA")

# --- MENU 1: HOME & MATERI ---
if choice == "🏠 Home & Materi":
    st.markdown("""
        <div style="background-color:#27ae60; padding:30px; border-radius:15px; margin-bottom:25px; text-align:center;">
            <h1 style="color:white; margin:0;">🌙 DigiDakwah</h1>
            <p style="color:white; opacity:0.9; font-size:18px;">Pusat Edukasi Digital Oratorium Fak. Saintek UMSIDA</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="quote-box">"Sampaikanlah dariku walau hanya satu ayat." (HR. Bukhari)</div>', unsafe_allow_html=True)

    st.subheader("📚 Materi Dakwah Pilihan")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="materi-card">
                <h3 style="color:#27ae60;">📖 Fikih Ibadah</h3>
                <p style="color:#5f6368; font-size:15px;">Panduan praktis tata cara salat dan thaharah sesuai tuntunan tarjih Muhammadiyah untuk jemaah milenial.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="materi-card" style="border-top-color: #e67e22;">
                <h3 style="color:#e67e22;">📱 Adab Medsos</h3>
                <p style="color:#5f6368; font-size:15px;">Edukasi pentingnya akhlakul karimah dalam berinteraksi di ruang virtual guna mewujudkan internet sehat.</p>
            </div>
        """, unsafe_allow_html=True)
        with col3:
        st.markdown("""
            <div class="materi-card" style="border-top-color: #3498db;">
                <h3 style="color:#3498db;">🚿 Thaharah</h3>
                <p style="color:#5f6368; font-size:15px;">Kupas tuntas tata cara bersuci, wudhu, dan tayamum yang benar sebagai kunci utama sahnya ibadah salat.</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="materi-card" style="border-top-color: #9b59b6;">
                <h3 style="color:#9b59b6;">💰 Zakat & Infaq</h3>
                <p style="color:#5f6368; font-size:15px;">Memahami pengelolaan harta melalui zakat mal, fitrah, dan infaq untuk pemberdayaan umat di lingkungan kampus.</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    with st.expander("✨ Tentang Program DigiDakwah", expanded=True):
        st.write("""
            Program ini dikelola oleh **Lembaga Dakwah Oratorium Fakultas Sains dan Teknologi UMSIDA**. 
            Aplikasi ini bertujuan untuk mendigitalisasi layanan tanya-jawab keagamaan yang biasanya dilakukan pada kajian rutin.
            
            **Cara Kerja:**
            Pertanyaan yang masuk melalui form akan direkap oleh tim Informatika dan diserahkan kepada Ustadz pembina Oratorium untuk dijawab secara berkala.
        """)
        st.caption("📍 Lokasi: Oratorium Lantai 4, Kampus 2 UMSIDA")

# --- MENU 2: VIDEO KAJIAN ---
elif choice == "📺 Video Kajian":
    st.header("📺 Arsip Video Kajian")
    st.markdown("Dokumentasi kajian rutin dan video singkat edukatif.")
    st.video("https://www.youtube.com/watch?v=zPrS0A6r_hM")
    st.info("**Kajian Hari Ini:** Adab Menuntut Ilmu di Perguruan Tinggi")

# --- MENU 3: TANYA USTADZ ---
elif choice == "📝 Tanya Ustadz":
    st.header("📝 Form Tanya Ustadz")
    st.write("Ajukan pertanyaan seputar hukum Islam. Identitas Anda aman dalam database kami.")
    
    DB_FILE = "data_dakwah.csv"
    
    def load_data():
        if os.path.exists(DB_FILE):
            try: return pd.read_csv(DB_FILE)
            except: return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])
        else: return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan"])

    with st.form(key='tanya_form', clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp (Aktif)")
        pertanyaan = st.text_area("Tulis Pertanyaan Anda secara detail")
        submit = st.form_submit_button("Kirim ke Ustadz")

    if submit:
        if nama and pertanyaan:
            new_data = {
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Nama": nama, "Kontak": kontak, "Pertanyaan": pertanyaan
            }
            df = load_data()
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("✅ Alhamdulillah, pertanyaan Anda telah masuk ke sistem Oratorium Saintek!")
            st.rerun()
        else:
            st.error("⚠️ Mohon lengkapi Nama dan Pertanyaan.")

    st.divider()
    st.subheader("📊 Monitoring Database Pertanyaan (Admin Only)")
    df_display = load_data()
    if not df_display.empty:
        st.dataframe(df_display, use_container_width=True)
