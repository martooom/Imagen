# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MoJe46G9R84_IbWsPB0OFlIP4et6bw-w
"""

import streamlit as st

image_url = "https://sl.bing.net/kNp02BQuOrI"

 st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;  /* Ajusta la imagen para que cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        background-repeat: no-repeat;  /* Evita que la imagen se repita */
        height: 100vh;  /* Hace que la imagen cubra toda la altura de la ventana */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

