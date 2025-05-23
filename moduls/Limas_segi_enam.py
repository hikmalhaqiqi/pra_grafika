import streamlit as st
import numpy as np
import plotly.graph_objects as go

def tampilkan():

    def create_hexagonal_pyramid(scale=1.0, rotation=(0, 0, 0), translation=(0, 0, 0)):
        # Titik dasar segi enam
        angle = np.linspace(0, 2 * np.pi, 7)[:-1]
        base_x = scale * np.cos(angle)
        base_y = scale * np.sin(angle)
        base_z = np.zeros_like(base_x)

        # Titik puncak limas
        apex = np.array([0, 0, scale * 2])

        # Gabungkan titik
        base_points = np.vstack((base_x, base_y, base_z)).T
        points = np.vstack((base_points, apex))

        # Rotasi
        rx, ry, rz = np.radians(rotation)
        Rx = np.array([[1, 0, 0],
                       [0, np.cos(rx), -np.sin(rx)],
                       [0, np.sin(rx), np.cos(rx)]])
        Ry = np.array([[np.cos(ry), 0, np.sin(ry)],
                       [0, 1, 0],
                       [-np.sin(ry), 0, np.cos(ry)]])
        Rz = np.array([[np.cos(rz), -np.sin(rz), 0],
                       [np.sin(rz), np.cos(rz), 0],
                       [0, 0, 1]])
        R = Rz @ Ry @ Rx
        points = points @ R.T

        # Translasi
        points += np.array(translation)

        return points

    def draw_hex_pyramid(points, face_color, border_color):
        x, y, z = points[:, 0], points[:, 1], points[:, 2]
        apex_index = len(points) - 1

        fig = go.Figure()

        # Buat sisi segitiga antara setiap sisi dasar dan apex
        for i in range(6):
            fig.add_trace(go.Mesh3d(
                x=[x[i], x[(i + 1) % 6], x[apex_index]],
                y=[y[i], y[(i + 1) % 6], y[apex_index]],
                z=[z[i], z[(i + 1) % 6], z[apex_index]],
                color=face_color,
                opacity=0.8,
                flatshading=True,
                showscale=False
            ))

        # Tambah sisi alas
        fig.add_trace(go.Mesh3d(
            x=x[:6], y=y[:6], z=z[:6],
            i=[0, 1, 2, 3],
            j=[1, 2, 3, 4],
            k=[2, 3, 4, 5],
            color=face_color,
            opacity=0.5,
            showscale=False
        ))

        # Tambah garis tepi
        for i in range(6):
            fig.add_trace(go.Scatter3d(
                x=[x[i], x[(i + 1) % 6]],
                y=[y[i], y[(i + 1) % 6]],
                z=[z[i], z[(i + 1) % 6]],
                mode='lines',
                line=dict(color=border_color, width=5),
                showlegend=False
            ))
            fig.add_trace(go.Scatter3d(
                x=[x[i], x[apex_index]],
                y=[y[i], y[apex_index]],
                z=[z[i], z[apex_index]],
                mode='lines',
                line=dict(color=border_color, width=5),
                showlegend=False
            ))

        fig.update_layout(
            scene=dict(aspectmode='data'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig

    st.title("🔺 Visualisasi Limas Segi Enam (Hexagonal Pyramid) 3D")

    st.subheader("⚙️ Kontrol Transformasi")

    col1, col2, col3 = st.columns(3)

    with col1:
        scale = st.slider("Skala", 0.1, 3.0, 1.0, 0.1)
        face_color = st.color_picker("Warna Objek", "#00ccff")
        border_color = st.color_picker("Warna Garis", "#000000")

    with col2:
        rot_x = st.slider("Rotasi X (°)", 0, 360, 0)
        rot_y = st.slider("Rotasi Y (°)", 0, 360, 0)
        rot_z = st.slider("Rotasi Z (°)", 0, 360, 0)

    with col3:
        trans_x = st.slider("Translasi X", -5.0, 5.0, 0.0, 0.1)
        trans_y = st.slider("Translasi Y", -5.0, 5.0, 0.0, 0.1)
        trans_z = st.slider("Translasi Z", -5.0, 5.0, 0.0, 0.1)

    points = create_hexagonal_pyramid(
        scale=scale,
        rotation=(rot_x, rot_y, rot_z),
        translation=(trans_x, trans_y, trans_z)
    )

    fig = draw_hex_pyramid(points, face_color, border_color)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    tampilkan()
