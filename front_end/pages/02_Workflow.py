import streamlit as st
import requests
from PIL import Image
# Title
highlighted_text_title = (
    "<span style='font-size: 30px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

def subpage1():
    def display_side_content(side):
        if side == "Data":
            st.image("images/small_imgs_mel_01.jpg", width=700)
            st.write("<span style=\"font-size:20px\">**Dataset**</span>", unsafe_allow_html=True)
            st.write("- <span style=\"font-size:18px\">Kaggle dataset from the original **HAM10000** (Human Against Machine with 10,000 Training images) dataset.</span>", unsafe_allow_html=True)
            st.write("📊 Source: [Kaggle Melanoma Dataset](https://www.kaggle.com/datasets/drscarlat/melanoma)")


        elif side == "Preprocessing":
            #st.write("<span style=\"font-size:20px\">**Data Preparation**</span>", unsafe_allow_html=True)
            st.write("- <span style=\"font-size:18px\">Data augmentation for balancing the data</span>\n"
                    "- <span style=\"font-size:20px\">Reshaping of images to **224x224 pixels** for **CNN processing**, normalized</span>", unsafe_allow_html=True)
            #st.write("/")
            st.image("images/training_sets.png", use_column_width=True)

        elif side == "Process":
            st.write("<span style=\"font-size:20px\">**From data to prediction**</span>", unsafe_allow_html=True)
            st.image("images/process_DIAGRAM_01.png", width=(800))

        elif side == "Kernels":
            st.write("<span style=\"font-size:20px\">**what happens in the black box**</span>", unsafe_allow_html=True)
            st.image("images/kernels_01.png", width=(800))

    def horizontal_tabs(default_tabs=[], default_active_tab=0):
        selected_tab = st.session_state.get('selected_tab', default_tabs[default_active_tab])

        if not default_tabs:
            return None

        col1, col2, col3, col4= st.columns(4)

        with col1:
            active_tab_1 = st.button("Data", key="Data", help="Click to select tab")
            if active_tab_1:
                selected_tab = "Data"

        with col2:
            active_tab_2 = st.button("Preprocessing", key="Preprocessing", help="Click to select tab")
            if active_tab_2:
                selected_tab = "Preprocessing"

        with col3:
            active_tab_3 = st.button("Process", key="Process", help="Click to select tab")
            if active_tab_3:
                selected_tab = "Process"

        with col4:
            active_tab_4 = st.button("Kernels", key="Kernels", help="Click to select tab")
            if active_tab_4:
                selected_tab = "Kernels"

        st.session_state.selected_tab = selected_tab
        return selected_tab

    tabs_list = ["Data", "Preprocessing", "Process", "Kernels"]
    active_tab = horizontal_tabs(tabs_list)

    if active_tab:
        display_side_content(active_tab)




# Define function to display subpage 2 content
def subpage2():
    st.header("Prediction Model")
    st.image("images/liri_1.png", width=1000)
    st.image("images/liri_2.png", width=1000)

# Create sidebar navigation menu
subpage = st.sidebar.radio("Workflow", ["Data", "Prediction Model"])

# Display content based on selected subpage
if subpage == "Data":
    subpage1()
elif subpage == "Prediction Model":
    subpage2()
