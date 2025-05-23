import streamlit as st
import numpy as np
import plotly.graph_objects as go

def tampilkan():
    st.title("🔵 Transformasi Oval Pipih (Elips 2D)")

    # Fungsi membuat koordinat elips
    def create_ellipse(rx=1.0, ry=0.5, rotation=0.0, translation=(0.0, 0.0)):
        t = np.linspace(0, 2 * np.pi, 100)
        x = rx * np.cos(t)
        y = ry * np.sin(t)

        # Rotasi
        theta = np.radians(rotation)
        x_rot = x * np.cos(theta) - y * np.sin(theta)
        y_rot = x * np.sin(theta) + y * np.cos(theta)

        # Translasi
        x_final = x_rot + translation[0]
        y_final = y_rot + translation[1]
        return x_final, y_final

    # Fungsi menggambar objek dan garis sumbu
    def draw_ellipse(x, y, fill_color, border_color):
        fig = go.Figure()

        # Garis sumbu X dan Y
        fig.add_trace(go.Scatter(
            x=[-20, 20], y=[0, 0],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[0, 0], y=[-20, 20],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))

        # Gambar oval
        fig.add_trace(go.Scatter(
            x=np.append(x, x[0]),
            y=np.append(y, y[0]),
            mode='lines+markers',
            fill='toself',
            fillcolor=fill_color,
            line=dict(color=border_color, width=3),
            marker=dict(size=4, color=border_color),
            showlegend=False
        ))

        fig.update_layout(
            xaxis=dict(scaleanchor="y", range=[-20, 20], zeroline=False, showgrid=True),
            yaxis=dict(range=[-20, 20], zeroline=False, showgrid=True),
            margin=dict(l=10, r=10, t=10, b=10),
            height=500
        )
        return fig

    # Kontrol transformasi
    st.subheader("⚙️ Kontrol Transformasi")

    col1, col2, col3 = st.columns(3)
    with col1:
        rx = st.slider("Skala Horizontal (rx)", 0.5, 10.0, 3.0, 0.1)
        fill_color = st.color_picker("Warna Objek", "#00ccff")

    with col2:
        ry = st.slider("Skala Vertikal (ry)", 0.5, 10.0, 1.0, 0.1)
        border_color = st.color_picker("Warna Garis", "#000000")
        rotation = st.slider("Rotasi (°)", 0, 360, 0)

    with col3:
        trans_x = st.slider("Translasi X", -10.0, 10.0, 0.0, 0.1)
        trans_y = st.slider("Translasi Y", -10.0, 10.0, 0.0, 0.1)

    # Buat dan tampilkan elips berdasarkan kontrol saat ini
    x, y = create_ellipse(rx, ry, rotation, (trans_x, trans_y))
    fig = draw_ellipse(x, y, fill_color, border_color)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    tampilkan()
