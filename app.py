from utils import *
import streamlit as st
from random import choice, randint

isStart = st.button("Click to Start.")

if isStart:
    choosen_image = choice(list_image)
    skin = choosen_image.split('/')[-1].split('.')[0].capitalize()

    st.image(choosen_image)

    col_1, _, col_2 = st.columns([5, 1, 5])

    with col_1:

        st.markdown(
            """
            <style>
                .stProgress > div > div > div > div {
                    background-color: #5cdb7e;
                }
            </style>""",
            unsafe_allow_html=True,
        )

        st.metric("Age Estimation", randint(15, 31), delta_color = "off")

    with col_2:

        st.markdown(
            """
            <style>
                .stProgress > div > div > div > div {
                    background-color: #5cdb7e;
                }
            </style>""",
            unsafe_allow_html=True,
        )

        nums = randint(50, 91)
        st.metric("Skin Problem Severity", f"{nums} %", delta_color = "off")
        st.progress(nums)

    face_type = skin if skin == 'Oily' else choice(list_type)

    st.error(f"Most Skin Problem is  : {skin}")
    st.error(f"Face Type Detected is : {skin if skin == 'Oily' else face_type}")

    st.success("Personalisasi Produk Perawatan Kulit")

    cols1, cols2, cols3 = st.columns(3)
    prods = prod_type[face_type]

    with cols1:

        prod_0 = prods[0]
        url = prod_0['url']

        st.image(url)
        st.write(prod_0['nme'])
        st.write(prod_0['prc'])

        isBuy = st.button("Beli Produk Di Bawah Ini.", key = "1")
        st.write(prod_0['str'])

    with cols2:

        prod_1 = prods[1]
        url = prod_1['url']

        st.image(url)
        st.write(prod_1['nme'])
        st.write(prod_1['prc'])

        isBuy = st.button("Beli Produk Di Bawah Ini.", key = "2")
        st.write(prod_1['str'])

    with cols3:

        prod_2 = prods[2]
        url = prod_2['url']

        st.image(url)
        st.write(prod_2['nme'])
        st.write(prod_2['prc'])

        isBuy = st.button("Beli Produk Di Bawah Ini.", key = "3")
        st.write(prod_2['str'])