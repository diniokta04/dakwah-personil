import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="DigiDakwah - Oratorium Saintek", page_icon="🌙", layout="centered")

# 2. INISIALISASI DATABASE KONTEN (Jika belum ada)
# Menggunakan session_state agar perubahan Admin langsung terlihat
if 'materi_list' not in st.session_state:
    st.session_state.materi_list = [
        {"judul": "📖 Fikih Ibadah", "isi": "Panduan praktis tata cara salat dan thaharah sesuai tuntunan tarjih Muhammadiyah.", "warna": "#27ae60"},
        {"judul": "📱 Adab Medsos", "isi": "Edukasi pentingnya akhlakul karimah dalam berinteraksi di ruang virtual.", "warna": "#e67e22"}
    ]

if 'video_list' not in st.session_state:
    st.session_state.video_list = [
        {"judul": "Hadiah Allah Saat Kesulitan", "ustadz": "UAH", "link": "https://youtu.be/izYUMrsvVDQ"},
    ]

# 3. FUNGSI DATABASE PERTANYAAN
DB_FILE = "data_dakwah.csv"
def load_data():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    return pd.DataFrame(columns=["Waktu", "Nama", "Kontak", "Pertanyaan", "Status"])

# 4. SIDEBAR
with st.sidebar:
    st.title("🌙 DigiDakwah")
    menu = ["🏠 Home", "📺 Video", "📝 Tanya Ustadz", "🔐 Admin"]
    choice = st.selectbox("Menu", menu)
    st.caption("Developed by Dini Oktabiyanti")

# --- HALAMAN HOME ---
if choice == "🏠 Home":
    st.header("📚 Materi Dakwah")
    cols = st.columns(2)
    for i, m in enumerate(st.session_state.materi_list):
        with cols[i % 2]:
            st.info(f"**{m['judul']}**\n\n{m['isi']}")

# --- HALAMAN VIDEO ---
elif choice == "📺 Video":
    st.header("📺 Kajian Digital")
    for v in st.session_state.video_list:
        st.video(v['link'])
        st.caption(f"{v['judul']} - {v['ustadz']}")
        st.divider()

# --- HALAMAN TANYA USTADZ ---
elif choice == "📝 Tanya Ustadz":
    st.header("📝 Konsultasi Agama")
    with st.form("tanya", clear_on_submit=True):
        nama = st.text_input("Nama")
        kontak = st.text_input("WhatsApp")
        tanya = st.text_area("Pertanyaan")
        if st.form_submit_button("Kirim"):
            df = load_data()
            new_row = {"Waktu": datetime.now(), "Nama": nama, "Kontak": kontak, "Pertanyaan": tanya, "Status": "Belum"}
            pd.concat([df, pd.DataFrame([new_row])]).to_csv(DB_FILE, index=False)
            st.success("Terkirim!")

# --- HALAMAN ADMIN (FITUR LENGKAP) ---
elif choice == "🔐 Admin":
    pw = st.text_input("Password", type="password")
    if pw == "admin123":
        tab1, tab2, tab3 = st.tabs(["💬 Respon User", "🏠 Kelola Home", "📺 Kelola Video"])
        
        # TAB 1: RESPON USER
        with tab1:
            df = load_data()
            for i, r in df.iterrows():
                with st.expander(f"{r['Nama']} - {r['Status']}"):
                    st.write(r['Pertanyaan'])
                    c1, c2 = st.columns(2)
                    if c1.button("Selesai", key=f"s{i}"):
                        df.at[i, 'Status'] = "Sudah"
                        df.to_csv(DB_FILE, index=False)
                        st.rerun()
                    if c2.button("Hapus", key=f"h{i}"):
                        df.drop(i).to_csv(DB_FILE, index=False)
                        st.rerun()

        # TAB 2: KELOLA HOME (Tambah Materi)
        with tab2:
            st.subheader("Tambah Materi Baru")
            new_j = st.text_input("Judul Materi")
            new_i = st.text_area("Isi Materi")
            if st.button("Simpan Materi"):
                st.session_state.materi_list.append({"judul": new_j, "isi": new_i})
                st.success("Materi Ditambahkan!")
            
            st.divider()
            for i, m in enumerate(st.session_state.materi_list):
                if st.button(f"Hapus: {m['judul']}", key=f"mat{i}"):
                    st.session_state.materi_list.pop(i)
                    st.rerun()

        # TAB 3: KELOLA VIDEO (Tambah Video)
        with tab3:
            st.subheader("Tambah Video Baru")
            v_j = st.text_input("Judul Video")
            v_l = st.text_input("Link YouTube")
            if st.button("Tambah Video"):
                st.session_state.video_list.append({"judul": v_j, "link": v_l, "ustadz": "Admin"})
                st.success("Video Ditambahkan!")
