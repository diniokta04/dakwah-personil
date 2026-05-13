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
        height: 230px;
        transition: transform 0.3s;
        margin-bottom: 20px;
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

# Fungsi Database (Menambah Kolom Status)
DB_FILE = "data_dakwah.csv"
def load_data():
    if os.path.exists(DB_FILE):
        df = pd.read_csv(DB_FILE)
        # Jika kolom Status belum ada (untuk file lama), tambahkan otomatis
        if "Status" not in df.columns:
            df["Status"] = "Belum Dijawab"
            df.to_csv(DB_FILE, index=False)
        return df
    else:
        return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan", "Status"])

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004613.png", width=100)
    st.title("DigiDakwah")
    menu = ["🏠 Home & Materi", "📺 Video Kajian", "📝 Tanya Ustadz", "🔐 Panel Admin"]
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
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="materi-card"><h3>📖 Fikih Ibadah</h3><p>Panduan praktis tata cara salat dan thaharah sesuai tuntunan tarjih Muhammadiyah.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="materi-card" style="border-top-color: #e67e22;"><h3>📱 Adab Medsos</h3><p>Edukasi pentingnya akhlakul karimah dalam berinteraksi di ruang virtual.</p></div>', unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="materi-card" style="border-top-color: #3498db;"><h3>🚿 Thaharah</h3><p>Kupas tuntas tata cara bersuci, wudhu, dan tayamum yang benar.</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="materi-card" style="border-top-color: #9b59b6;"><h3>💰 Zakat & Infaq</h3><p>Memahami pengelolaan harta untuk pemberdayaan umat di lingkungan kampus.</p></div>', unsafe_allow_html=True)

    st.write("---")
    with st.expander("✨ Tentang Program DigiDakwah", expanded=True):
        st.write("""
            Program ini dikelola oleh **Lembaga Dakwah Oratorium Fakultas Sains dan Teknologi UMSIDA**. 
            Aplikasi ini bertujuan untuk mendigitalisasi layanan tanya-jawab keagamaan yang biasanya dilakukan pada kajian rutin.
        """)
        st.caption("📍 Lokasi: Oratorium Lantai 4, Kampus 2 UMSIDA")

# --- MENU 2: VIDEO KAJIAN ---
elif choice == "📺 Video Kajian":
    st.header("📺 Arsip Video Kajian")
    st.video("https://www.youtube.com/watch?v=zPrS0A6r_hM")

# --- MENU 3: TANYA USTADZ ---
elif choice == "📝 Tanya Ustadz":
    st.header("📝 Form Tanya Ustadz")
    st.write("Silakan ajukan pertanyaan Anda.")
    with st.form(key='tanya_form', clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        kontak = st.text_input("Nomor WhatsApp (Contoh: 08123xxx)")
        pertanyaan = st.text_area("Tulis Pertanyaan Anda")
        submit = st.form_submit_button("Kirim ke Ustadz")
    
    if submit:
        if nama and pertanyaan and kontak:
            # Status default adalah Belum Dijawab
            new_data = {
                "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                "Nama": nama, 
                "Kontak": kontak, 
                "Pertanyaan": pertanyaan,
                "Status": "Belum Dijawab"
            }
            df = load_data()
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DB_FILE, index=False)
            st.success("✅ Alhamdulillah, pertanyaan Anda telah masuk ke sistem!")
        else:
            st.error("⚠️ Mohon lengkapi semua kolom.")

# --- MENU 4: PANEL ADMIN ---
elif choice == "🔐 Panel Admin":
    st.header("🔐 Panel Administrasi Oratorium")
    password = st.text_input("Masukkan Password Admin", type="password")
    
    if password == "admin123":
        st.success("Akses Diterima.")
        df_admin = load_data()
        
        if not df_admin.empty:
            # Filter tampilan
            filter_status = st.radio("Tampilkan:", ["Semua", "Belum Dijawab", "Sudah Dijawab"], horizontal=True)
            
            if filter_status != "Semua":
                df_filtered = df_admin[df_admin["Status"] == filter_status]
            else:
                df_filtered = df_admin

            st.metric("Jumlah Pertanyaan", f"{len(df_filtered)} User")
            st.divider()
            
            for index, row in df_filtered.iterrows():
                # Warna label status
                status_color = "🔴" if row['Status'] == "Belum Dijawab" else "🟢"
                
                with st.expander(f"{status_color} Dari: {row['Nama']} ({row['Waktu']})"):
                    st.write(f"**Pertanyaan:**\n{row['Pertanyaan']}")
                    st.write(f"**Kontak:** {row['Kontak']}")
                    st.write(f"**Status Saat Ini:** {row['Status']}")
                    
                    col_wa, col_mark = st.columns([1, 1])
                    
                    with col_wa:
                        # Format WhatsApp
                        wa_num = str(row['Kontak'])
                        if wa_num.startswith('0'): wa_num = '62' + wa_num[1:]
                        elif wa_num.startswith('8'): wa_num = '62' + wa_num
                        
                        pesan = f"Assalamualaikum {row['Nama']}, Admin DigiDakwah ingin menjawab pertanyaan Anda: "
                        wa_link = f"https://wa.me/{wa_num}?text={pesan}"
                        
                        st.markdown(f"""
                            <a href="{wa_link}" target="_blank">
                                <button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold; width: 100%;">
                                    💬 Balas & Buka WA
                                </button>
                            </a>
                        """, unsafe_allow_html=True)
                    
                    with col_mark:
                        if st.button(f"Tandai Sudah Dijawab", key=f"btn_{index}"):
                            df_admin.at[index, "Status"] = "Sudah Dijawab"
                            df_admin.to_csv(DB_FILE, index=False)
                            st.rerun()

        else:
            st.info("Belum ada pertanyaan masuk.")
    elif password != "":
        st.error("Password Salah!")
