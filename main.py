import streamlit as st
from moduls import Elipsoid, Limas_segi_enam, Oval_pipih, Prisma_segi_lima, Segiduabelas, segitiga_sama_kaki

st.sidebar.title("Menu Bangun Ruang")

kategori = st.sidebar.radio("Pilih kategori", ["Bangun 2D", "Bangun 3D"])

if kategori == "Bangun 2D":
    halaman = st.sidebar.selectbox("Pilih bentuk 2D", ["Segi dua belas", "Segitiga sama kaki", "Oval Pipih"])
    if halaman == "Segi dua belas":
        Segiduabelas.tampilkan()
    elif halaman == "Segitiga sama kaki":
        segitiga_sama_kaki.tampilkan()
    elif halaman == "Oval Pipih":
        Oval_pipih.tampilkan()

elif kategori == "Bangun 3D":
    halaman = st.sidebar.selectbox("Pilih bentuk 3D", ["Prisma segi lima", "Elipsoid", "Limas segi enam"])
    if halaman == "Prisma segi lima":
        Prisma_segi_lima.tampilkan()
    elif halaman == "Elipsoid":
        Elipsoid.tampilkan()
    elif halaman == "Limas segi enam":
        Limas_segi_enam.tampilkan()
