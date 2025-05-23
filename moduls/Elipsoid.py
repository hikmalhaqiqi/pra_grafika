import streamlit as st
import numpy as np
import plotly.graph_objects as go

def tampilkan():
    
    def create_ellipsoid(scale=(1, 1, 1), rotation=(0, 0, 0), translation=(0, 0, 0), resolution=30):
        u = np.linspace(0, 2 * np.pi, resolution)
        v = np.linspace(0, np.pi, resolution)
        u, v = np.meshgrid(u, v)

        x = scale[0] * np.cos(u) * np.sin(v)
        y = scale[1] * np.sin(u) * np.sin(v)
        z = scale[2] * np.cos(v)

        # Flatten
        x = x.flatten()
        y = y.flatten()
        z = z.flatten()

        points = np.vstack((x, y, z)).T

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
        rotated_points = points @ R.T

        # Translasi
        rotated_points += np.array(translation)

        x, y, z = rotated_points[:, 0], rotated_points[:, 1], rotated_points[:, 2]
        return x.reshape((resolution, resolution)), y.reshape((resolution, resolution)), z.reshape((resolution, resolution))

    def draw_ellipsoid(x, y, z, face_color):
        fig = go.Figure(data=[go.Surface(
            x=x, y=y, z=z,
            colorscale=[[0, face_color], [1, face_color]],
            showscale=False,
            opacity=0.8
        )])

        fig.update_layout(
            scene=dict(aspectmode='data'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig

    st.title("🔵 Visualisasi Elipsoid 3D Interaktif")

    st.subheader("⚙️ Kontrol Transformasi")

    col1, col2, col3 = st.columns(3)

    with col1:
        scale_x = st.slider("Skala X", 0.1, 5.0, 2.0, 0.1)
        scale_y = st.slider("Skala Y", 0.1, 5.0, 1.0, 0.1)
        scale_z = st.slider("Skala Z", 0.1, 5.0, 1.0, 0.1)
        face_color = st.color_picker("Warna Objek", "#00aaff")

    with col2:
        rot_x = st.slider("Rotasi X (°)", 0, 360, 0)
        rot_y = st.slider("Rotasi Y (°)", 0, 360, 0)
        rot_z = st.slider("Rotasi Z (°)", 0, 360, 0)

    with col3:
        trans_x = st.slider("Translasi X", -5.0, 5.0, 0.0, 0.1)
        trans_y = st.slider("Translasi Y", -5.0, 5.0, 0.0, 0.1)
        trans_z = st.slider("Translasi Z", -5.0, 5.0, 0.0, 0.1)

    # Buat elipsoid berdasarkan input user
    x, y, z = create_ellipsoid(
        scale=(scale_x, scale_y, scale_z),
        rotation=(rot_x, rot_y, rot_z),
        translation=(trans_x, trans_y, trans_z)
    )

    fig = draw_ellipsoid(x, y, z, face_color)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    tampilkan()