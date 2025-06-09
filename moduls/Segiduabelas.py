import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

def tampilkan():
    st.title("🔷 Transformasi Segi Dua Belas (2D)")

    # Fungsi membuat koordinat segi dua belas
    def create_dodecagon(radius=1.0, rotation=0.0, translation=(0.0, 0.0)):
        angle = np.linspace(0, 2 * np.pi, 13)[:-1]
        x = radius * np.cos(angle + np.radians(rotation)) + translation[0]
        y = radius * np.sin(angle + np.radians(rotation)) + translation[1]
        return x, y

    # Fungsi menggambar objek dan garis sumbu
    def draw_dodecagon(x, y, fill_color, border_color):
        fig = go.Figure()

        # Garis sumbu X dan Y
        fig.add_trace(go.Scatter(
            x=[-10, 10],
            y=[0, 0],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[0, 0],
            y=[-10, 10],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))

        # Dodecagon
        fig.add_trace(go.Scatter(
            x=np.append(x, x[0]),
            y=np.append(y, y[0]),
            mode='lines+markers',
            fill='toself',
            fillcolor=fill_color,
            line=dict(color=border_color, width=3),
            marker=dict(size=5, color=border_color),
            showlegend=False
        ))

        fig.update_layout(
            xaxis=dict(scaleanchor="y", range=[-10, 10], zeroline=False, showgrid=True),
            yaxis=dict(range=[-10, 10], zeroline=False, showgrid=True),
            margin=dict(l=10, r=10, t=10, b=10),
            height=500
        )
        return fig

    # Kontrol transformasi
    st.subheader("⚙️ Kontrol Transformasi")

    col1, col2, col3 = st.columns(3)
    with col1:
        radius = st.slider("Skala (Radius)", 0.5, 10.0, 1.0, 0.1)
        fill_color = st.color_picker("Warna Objek", "#ffcc00")

    with col2:
        rotation = st.slider("Rotasi (°)", 0, 360, 0)
        border_color = st.color_picker("Warna Garis", "#000000")

    with col3:
        trans_x = st.slider("Translasi X", -5.0, 5.0, 0.0, 0.1)
        trans_y = st.slider("Translasi Y", -5.0, 5.0, 0.0, 0.1)

    # Tombol animasi dan kontrol kecepatan
    st.subheader("🎬 Kontrol Animasi")
    col_anim1, col_anim2 = st.columns(2)
    
    with col_anim1:
        animate_button = st.button("🔄 Gerakkan", type="primary")
        
    with col_anim2:
        animation_speed = st.selectbox("Kecepatan Animasi", 
                                     ["Lambat", "Normal", "Cepat"], 
                                     index=1)
    
    # Tentukan delay berdasarkan kecepatan
    speed_map = {"Lambat": 0.2, "Normal": 0.1, "Cepat": 0.05}
    delay = speed_map[animation_speed]

    # Container untuk plot
    plot_container = st.empty()

    # Jika tombol ditekan, jalankan animasi
    if animate_button:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Parameter animasi
        total_frames = 60
        
        for frame in range(total_frames):
            # Hitung rotasi dan translasi Y berdasarkan frame
            animated_rotation = rotation + (frame * 360 / total_frames)
            animated_trans_y = trans_y + 2 * np.sin(frame * 2 * np.pi / 20)  # Gerakan naik turun
            
            # Buat objek dengan parameter yang dianimasi
            x, y = create_dodecagon(radius, animated_rotation, (trans_x, animated_trans_y))
            fig = draw_dodecagon(x, y, fill_color, border_color)
            
            # Update plot
            with plot_container.container():
                st.plotly_chart(fig, use_container_width=True)
            
            # Update progress dan status
            progress = (frame + 1) / total_frames
            progress_bar.progress(progress)
            status_text.text(f"Frame {frame + 1}/{total_frames} - Rotasi: {animated_rotation:.1f}° - Y: {animated_trans_y:.2f}")
            
            # Delay untuk mengontrol kecepatan animasi
            time.sleep(delay)
        
        # Bersihkan progress bar dan status
        progress_bar.empty()
        status_text.empty()
        st.success("✅ Animasi selesai!")
        
    else:
        # Tampilkan objek statis berdasarkan kontrol saat ini
        x, y = create_dodecagon(radius, rotation, (trans_x, trans_y))
        fig = draw_dodecagon(x, y, fill_color, border_color)
        with plot_container.container():
            st.plotly_chart(fig, use_container_width=True)

    # Informasi tambahan
    st.subheader("ℹ️ Informasi")
    st.info("""
    **Cara menggunakan animasi:**
    1. Atur parameter transformasi sesuai keinginan
    2. Pilih kecepatan animasi (Lambat/Normal/Cepat)
    3. Klik tombol "🔄 Gerakkan" untuk memulai animasi
    4. Segi dua belas akan berputar 360° sambil bergerak naik-turun
    """)

if __name__ == "__main__":
    tampilkan()
