import streamlit as st
import pickle
import requests
from PIL import Image
from io import BytesIO
import gzip
import pickle

st.set_page_config(
    page_title="Product Recommender System",
    page_icon="🤖",
    layout="wide"
)
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        body {
            background-color: white;
            font-family: 'Playfair Display', serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 100vh;
        }

        .title-container {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            width: 100%;
            padding-top: 60px;
            z-index: 10;
            background-color: #000000;
            color: white;
            border-bottom: 5px solid #FFD700;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .main-title {
            font-size: 60px;
            font-weight: bold;
            text-transform: uppercase;
            text-align: center;
            letter-spacing: 6px;
            display: inline-block;
            position: relative;
            background: linear-gradient(45deg, #FFD700, #4B0082, #1E90FF);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            transform: perspective(1000px);
        }

        .main-title::before,
        .main-title::after {
            content: 'SMART PICK';
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1;
            color: transparent;
            background: linear-gradient(45deg, #4B0082, #FFD700);
            -webkit-background-clip: text;
            background-clip: text;
        }

        .main-title::before {
            transform: translateZ(-8px);
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .main-title::after {
            transform: translateZ(-16px);
            text-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .tagline {
            font-size: 30px;
            font-weight: 400;
            text-align: center;
            text-transform: none;
            color: #FFD700;
            margin-top: 0px;
            background: linear-gradient(45deg, #FFD700, #4B0082);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-family: 'Roboto', sans-serif;
        }

        .content {
            margin-top: 180px;
            width: 100%;
            text-align: center;
        }

        .main-title:hover::before {
            transform: translateZ(-10px);
        }

        .main-title:hover::after {
            transform: translateZ(-20px);
        }

    </style>
    <div class="title-container">
        <div class="main-title">
        SMART PICK
        </div>
        <div class="tagline">
            A PRODUCT RECOMMENDER SYSTEM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<br><br><br><br>', unsafe_allow_html=True)

names_trim = pickle.load(open("names_trim.pkl", "rb"))
names = pickle.load(open("names.pkl", "rb"))
images = pickle.load(open("images1.pkl", "rb"))

link = pickle.load(open("link.pkl", "rb"))

#similarity = pickle.load(open("similarity1.pkl", "rb"))




with gzip.open('compressed_similarity.pkl.gz', 'rb') as f_in:
    similarity= pickle.load(f_in)

st.markdown("""
    <div>
        <p style="font-size:14px; color:#555; text-align:center;">
            Important Information: Search and discover personalized recommendations for products such as mobiles, headphones, watches, televisions, and shoes.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>

        .css-1wa3eu0 {
            width: 200px !important; /* Set the desired width */
        }
    </style>
""", unsafe_allow_html=True)

selected_product_name = st.selectbox("", options=names_trim, index=None, placeholder="Search")


def recommend(product):
    product_index = names_trim[names_trim == product].index[0]
    sim = list(enumerate(similarity[product_index]))
    sim.sort(reverse=True, key=lambda y: y[1])
    rec = sim[1:40]
    recommended_products = []
    for ind in rec:
        recommended_products.append(ind[0])
    return recommended_products


if st.button("Recommend"):
    try:
        if selected_product_name == None:
            st.write("No recommendations: Please select a product")

        else:
            recommended_products1 = recommend(selected_product_name)
            x = 0
            img_width = 200
            img_height = 300
            for i in range(4):
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    resp = requests.get(images[recommended_products1[x]])
                    img = Image.open(BytesIO(resp.content))
                    resized_img = img.resize((img_width, img_height))
                    st.image(resized_img)
                    st.markdown(
                        f'<a href="{link[recommended_products1[x]]}" style="color: black; text-decoration: none;">{names[recommended_products1[x]]}</a>',
                        unsafe_allow_html=True)
                    x += 1

                with col2:
                    resp = requests.get(images[recommended_products1[x]])
                    img = Image.open(BytesIO(resp.content))
                    resized_img = img.resize((img_width, img_height))
                    st.image(resized_img)
                    st.markdown(
                        f'<a href="{link[recommended_products1[x]]}" style="color: black; text-decoration: none;">{names[recommended_products1[x]]}</a>',
                        unsafe_allow_html=True)
                    x += 1

                with col3:
                    resp = requests.get(images[recommended_products1[x]])
                    img = Image.open(BytesIO(resp.content))
                    resized_img = img.resize((img_width, img_height))
                    st.image(resized_img)
                    st.markdown(
                        f'<a href="{link[recommended_products1[x]]}" style="color: black; text-decoration: none;">{names[recommended_products1[x]]}</a>',
                        unsafe_allow_html=True)
                    x += 1
                with col4:
                    resp = requests.get(images[recommended_products1[x]])
                    img = Image.open(BytesIO(resp.content))
                    resized_img = img.resize((img_width, img_height))
                    st.image(resized_img)
                    st.markdown(
                        f'<a href="{link[recommended_products1[x]]}" style="color: black; text-decoration: none;">{names[recommended_products1[x]]}</a>',
                        unsafe_allow_html=True)
                    x += 1
                with col5:
                    resp = requests.get(images[recommended_products1[x]])
                    img = Image.open(BytesIO(resp.content))
                    resized_img = img.resize((img_width, img_height))
                    st.image(resized_img)
                    st.markdown(
                        f'<a href="{link[recommended_products1[x]]}" style="color: black; text-decoration: none;">{names[recommended_products1[x]]}</a>',
                        unsafe_allow_html=True)
                    x += 1
    except Exception as e:
        st.error("Unable to fetch the results")