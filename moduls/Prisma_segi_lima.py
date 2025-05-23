import streamlit as st
import numpy as np
import plotly.graph_objects as go

def tampilkan():
    
    def create_prism(scale=1.0, rotation=(0, 0, 0), translation=(0, 0, 0)):
        angle = np.linspace(0, 2 * np.pi, 6)[:-1]
        r = 1 * scale

        x_base = r * np.cos(angle)
        y_base = r * np.sin(angle)
        z_base = np.zeros_like(x_base)
        z_top = np.ones_like(x_base) * scale * 2

        points = []
        for x, y, z in zip(x_base, y_base, z_base):
            points.append([x, y, z])
        for x, y, z in zip(x_base, y_base, z_top):
            points.append([x, y, z])

        points = np.array(points)
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

        points += np.array(translation)
        return points

    def draw_prism(points, face_color, border_color):
        fig = go.Figure()

        x, y, z = points[:, 0], points[:, 1], points[:, 2]
        faces = [
            [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1],  # bottom
            [5, 6, 7], [5, 7, 8], [5, 8, 9], [5, 9, 6],  # top
            [0, 1, 6], [0, 6, 5],
            [1, 2, 7], [1, 7, 6],
            [2, 3, 8], [2, 8, 7],
            [3, 4, 9], [3, 9, 8],
            [4, 0, 5], [4, 5, 9]
        ]

        for f in faces:
            fig.add_trace(go.Mesh3d(
                x=x, y=y, z=z,
                i=[f[0]], j=[f[1]], k=[f[2]],
                color=face_color, opacity=0.8,
                flatshading=True, showscale=False
            ))

        # Garis tepi
        for i in range(5):
            fig.add_trace(go.Scatter3d(
                x=[x[i], x[(i + 1) % 5]],
                y=[y[i], y[(i + 1) % 5]],
                z=[z[i], z[(i + 1) % 5]],
                mode='lines', line=dict(color=border_color, width=5), showlegend=False
            ))
            fig.add_trace(go.Scatter3d(
                x=[x[i + 5], x[(i + 1) % 5 + 5]],
                y=[y[i + 5], y[(i + 1) % 5 + 5]],
                z=[z[i + 5], z[(i + 1) % 5 + 5]],
                mode='lines', line=dict(color=border_color, width=5), showlegend=False
            ))
            fig.add_trace(go.Scatter3d(
                x=[x[i], x[i + 5]],
                y=[y[i], y[i + 5]],
                z=[z[i], z[i + 5]],
                mode='lines', line=dict(color=border_color, width=5), showlegend=False
            ))

        fig.update_layout(
            scene=dict(aspectmode='data'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig

    st.title("🎲 Interaktif Prisma Segi Lima 3D")

    # Kontrol Transformasi
    st.subheader("⚙️ Kontrol Transformasi")

    col1, col2, col3 = st.columns(3)
    with col1:
        scale = st.slider("Skala", 0.1, 10.0, 1.0, 0.1)
        face_color = st.color_picker("Warna Objek", "#00aaff")
        border_color = st.color_picker("Warna Garis", "#000000")

    with col2:
        rot_x = st.slider("Rotasi X (°)", 0, 360, 0)
        rot_y = st.slider("Rotasi Y (°)", 0, 360, 0)
        rot_z = st.slider("Rotasi Z (°)", 0, 360, 0)

    with col3:
        trans_x = st.slider("Translasi X", -5.0, 5.0, 0.0, 0.1)
        trans_y = st.slider("Translasi Y", -5.0, 5.0, 0.0, 0.1)
        trans_z = st.slider("Translasi Z", -5.0, 5.0, 0.0, 0.1)

    # Buat prisma langsung dari kontrol
    prism = create_prism(scale, (rot_x, rot_y, rot_z), (trans_x, trans_y, trans_z))
    fig = draw_prism(prism, face_color, border_color)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    tampilkan()
