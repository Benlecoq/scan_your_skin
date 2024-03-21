import streamlit as st
from PIL import Image
import requests

# Sidebar
#st.sidebar.markdown('''
## <span style="font-size: 14px;">Jihyeong LEE</span><br><span style="font-size: 14px;">Julijana STEIMLE</span><br><span style="font-size: 14px;">Liridone ZHUGOLLI</span><br><span style="font-size: 14px;">Loredana HOREZEANU</span>
#''', unsafe_allow_html=True)


# Title
highlighted_text_title = (
    "<span style='font-size: 40px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

def display_side_content(side):
    if side == "Problem":
        #st.image("images/survival_rate.png", use_column_width=True)  # Display the image
        st.image("images/survival_rate.png", width=650)
        st.markdown("""
        - <span style="font-size:larger">Melanoma, known as "black tumor", is the deadliest skin cancer</span>
        - <span style="font-size:larger">Early treatment is crucial, Delays can be life-threatening</span>
        - <span style="font-size:larger">Detection in early stages ensures nearly 99% survival rate</span>
        """, unsafe_allow_html=True)  # Display the text

    elif side == "Data":
        st.image("images/small_imgs_mel_01.jpg", width=700)
        #st.write("<span style=\"font-size:20px\">**Task**</span>", unsafe_allow_html=True)
        #st.write("- <span style=\"font-size:18px\">Melanoma vs Not-Melanoma</span>", unsafe_allow_html=True)
        st.write("<span style=\"font-size:20px\">**Dataset**</span>", unsafe_allow_html=True)
        st.write("- <span style=\"font-size:18px\">Kaggle dataset from the original **HAM10000** (Human Against Machine with 10,000 Training images) dataset.</span>", unsafe_allow_html=True)
        st.write("📊 Source: [Kaggle Melanoma Dataset](https://www.kaggle.com/datasets/drscarlat/melanoma)")
        st.write("\n")
        st.write("\n")
        st.write("<span style=\"font-size:20px\">**Data Preparation**</span>", unsafe_allow_html=True)
        st.write("- <span style=\"font-size:18px\">Data augmentation for balancing the data</span>\n"
                 "- <span style=\"font-size:20px\">Reshaping of images to **224x224 pixels** for **CNN processing**, normalized</span>", unsafe_allow_html=True)


    elif side == "Prediction Model":
        st.write("Content for Model")

def horizontal_tabs(default_tabs=[], default_active_tab=0):
    selected_tab = st.session_state.get('selected_tab', default_tabs[default_active_tab])

    if not default_tabs:
        return None

    col1, col2, col3 = st.columns(3)

    with col1:
        active_tab_1 = st.button("Problem", key="Problem", help="Click to select tab")
        if active_tab_1:
            selected_tab = "Problem"

    with col2:
        active_tab_2 = st.button("Data", key="Data", help="Click to select tab")
        if active_tab_2:
            selected_tab = "Data"

    with col3:
        active_tab_3 = st.button("Prediction Model", key="Prediction Model", help="Click to select tab")
        if active_tab_3:
            selected_tab = "Prediction Model"

    st.session_state.selected_tab = selected_tab
    return selected_tab

tabs_list = ["Problem", "Data", "Prediction Model"]
active_tab = horizontal_tabs(tabs_list)

if active_tab:
    display_side_content(active_tab)
