import streamlit as st
import numpy as np
import plotly.graph_objects as go

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

    # Buat dan tampilkan objek tunggal berdasarkan kontrol saat ini
    x, y = create_dodecagon(radius, rotation, (trans_x, trans_y))
    fig = draw_dodecagon(x, y, fill_color, border_color)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    tampilkan()