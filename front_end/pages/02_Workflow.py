import streamlit as st
import os

# Title
highlighted_text_title = (
    "<span style='font-size: 40px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

# Function to get the absolute path of the image file
def get_image_path(image_name):
    # Specify the correct directory path
    directory_path = "/mount/src/scan_your_skin/front_end/images/"
    # Construct the full path to the image
    image_path = os.path.join(directory_path, image_name)
    return image_path

# Function to display content for the first subpage
def subpage1():
    def display_side_content(side):
        if side == "Data":
            st.markdown("<span style=\"font-size:20px; color:gray;\">**Dataset**</span>", unsafe_allow_html=True)            
            image_path = get_image_path('workflow_data.png')
            st.image(image_path, width=1000)
            st.markdown("- <span style=\"font-size:18px; color:gray;\">Kaggle dataset from the original **HAM10000** (Human Against Machine with 10,000 Training images) dataset.</span>", unsafe_allow_html=True)
            
        elif side == "Preprocessing":
            st.markdown("<span style=\"font-size:20px; color: gray;\">**Dataset Clustering**</span>", unsafe_allow_html=True)
            st.markdown("- <span style=\"font-size:18px; color: gray;\">Data augmentation for balancing the data</span>\n"
                        "- <span style=\"font-size:20px; color: gray;\">Reshaping of images to **224x224 pixels** for **CNN processing**, normalized</span>", unsafe_allow_html=True)
            image_path = get_image_path('data_new.png')
            st.image(image_path, width=1000)

        elif side == "Process":
            st.markdown("<span style=\"font-size:20px; color: gray;\">**From data to prediction**</span>", unsafe_allow_html=True)
            image_path = get_image_path('process_new.png')
            st.image(image_path, width=1200)

        elif side == "Kernels":
            st.markdown("<span style=\"font-size:20px; color: gray;\">**What happens in the black box**</span>", unsafe_allow_html=True)
            image_path = get_image_path('feature_extraction.png')
            st.image(image_path, width=1000)

        elif side == "Prediction Model":
            st.markdown("""
                - <span style="font-size:25px; color: gray;">Learning Curves and Performance Metrics</span>
                """, unsafe_allow_html=True)
            image_path = get_image_path('learning_curves.png')
            st.image(image_path, width=1000)
    
    
    def horizontal_tabs(default_tabs=[], default_active_tab=0):
        selected_tab = st.session_state.get('selected_tab', default_tabs[default_active_tab])

        if not default_tabs:
            return None

        cols = st.columns(len(default_tabs))
        for index, tab_name in enumerate(default_tabs):
            with cols[index]:
                if st.button(tab_name, key=tab_name):
                    selected_tab = tab_name

        st.session_state.selected_tab = selected_tab
        return selected_tab

    tabs_list = ["Data", "Preprocessing", "Process", "Kernels", "Prediction Model"]
    active_tab = horizontal_tabs(tabs_list)

    if active_tab:
        display_side_content(active_tab)



