import streamlit as st
from moduls import Elipsoid, Limas_segi_enam, Oval_pipih, Prisma_segi_lima, Segiduabelas, segitiga_sama_kaki

# Judul Aplikasi Utama
st.title("Visualisasi Bangun Geometri Interaktif")
st.write("Pilih bangun geometri di bawah ini untuk ditampilkan:")

# Inisialisasi session state jika belum ada
if 'selected_shape' not in st.session_state:
    st.session_state.selected_shape = None
if 'category_selected' not in st.session_state:
    st.session_state.category_selected = None

# Fungsi untuk mengatur bentuk yang dipilih
def select_shape(shape_name):
    st.session_state.selected_shape = shape_name

# Fungsi untuk mengatur kategori yang dipilih
def select_category(category_name):
    st.session_state.category_selected = category_name
    st.session_state.selected_shape = None # Reset pilihan bentuk jika kategori berubah

# --- Tombol Kategori ---
col_cat1, col_cat2 = st.columns(2)
with col_cat1:
    if st.button("Tampilkan Bangun 2D", use_container_width=True, key="cat_2d"):
        select_category("Bangun 2D")

with col_cat2:
    if st.button("Tampilkan Bangun 3D", use_container_width=True, key="cat_3d"):
        select_category("Bangun 3D")

st.markdown("---") # Pemisah

# --- Tombol Bentuk Berdasarkan Kategori yang Dipilih ---
if st.session_state.category_selected == "Bangun 2D":
    st.subheader("Pilih Bentuk 2D")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Segi Dua Belas", on_click=select_shape, args=("Segi dua belas",), use_container_width=True):
            pass
    with col2:
        if st.button("Segitiga Sama Kaki", on_click=select_shape, args=("Segitiga sama kaki",), use_container_width=True):
            pass
    with col3:
        if st.button("Oval Pipih", on_click=select_shape, args=("Oval Pipih",), use_container_width=True):
            pass

elif st.session_state.category_selected == "Bangun 3D":
    st.subheader("Pilih Bentuk 3D")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Prisma Segi Lima", on_click=select_shape, args=("Prisma segi lima",), use_container_width=True):
            pass
    with col2:
        if st.button("Elipsoid", on_click=select_shape, args=("Elipsoid",), use_container_width=True):
            pass
    with col3:
        if st.button("Limas Segi Enam", on_click=select_shape, args=("Limas segi enam",), use_container_width=True):
            pass

st.markdown("---") # Pemisah

# --- Tampilkan Bentuk yang Dipilih ---
if st.session_state.selected_shape:
    if st.session_state.selected_shape == "Segi dua belas":
        Segiduabelas.tampilkan()
    elif st.session_state.selected_shape == "Segitiga sama kaki":
        segitiga_sama_kaki.tampilkan()
    elif st.session_state.selected_shape == "Oval Pipih":
        Oval_pipih.tampilkan()
    elif st.session_state.selected_shape == "Prisma segi lima":
        Prisma_segi_lima.tampilkan()
    elif st.session_state.selected_shape == "Elipsoid":
        Elipsoid.tampilkan()
    elif st.session_state.selected_shape == "Limas segi enam":
        Limas_segi_enam.tampilkan()
