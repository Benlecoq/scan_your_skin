import streamlit as st
from PIL import Image

# Sidebar
st.sidebar.markdown('''
## <span style="font-size: 14px;">Jihyeong LEE</span><br><span style="font-size: 14px;">Julijana STEIMLE</span><br><span style="font-size: 14px;">Liridone ZHUGOLLI</span><br><span style="font-size: 14px;">Loredana HOREZEANU</span>
''', unsafe_allow_html=True)


# Title
highlighted_text_title = (
    "<span style='font-size: 40px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

def display_side_content(side):
    if side == "About":
        st.image("images/about_1.jpg", width = 500)  # Display the image

        # st.write("<span style=\"font-size:20px\">**Melanoma**</span>", unsafe_allow_html=True)

        st.markdown("""
        - <span style="font-size:larger">most invasive skin cancer with the highest risk of death</span>
        - <span style="font-size:larger">grows fast and can spread to any organ</span>
        - <span style="font-size:larger">high survival rate with early diagnosis but diminishes fast as melanoma progresses</span>
        """, unsafe_allow_html=True)  # Display the text

    elif side == "Motivation":

        st.image("images/survival_rate.png", width=700)  # Display the image
        # st.write("<span style=\"font-size:20px\">**Melanoma**</span>", unsafe_allow_html=True)

        st.markdown("""
        - <span style="font-size:larger">Accuracy rate of diagnosis: about 60% (up to 89% with dermoscopy)</span>
        - <span style="font-size:larger">Still challenging to diagnose early melanoma</span>
        - <span style="font-size:larger">Using computer-aided methods can improve diagnostic accuracy and increase survival rate of patients</span>
            """, unsafe_allow_html=True)  # Display the text



def horizontal_tabs(default_tabs=[], default_active_tab=0):
    selected_tab = st.session_state.get('selected_tab', default_tabs[default_active_tab])

    if not default_tabs:
        return None

    col1, col2, col3 = st.columns(3)

    with col1:
        active_tab_1 = st.button("About", key="About", help="Click to select tab")
        if active_tab_1:
            selected_tab = "About"

    with col2:
        active_tab_2 = st.button("Motivation", key="Motivation", help="Click to select tab")
        if active_tab_2:
            selected_tab = "Motivation"

    st.session_state.selected_tab = selected_tab
    return selected_tab

tabs_list = ["About", "Motivation"]
active_tab = horizontal_tabs(tabs_list)

if active_tab:
    display_side_content(active_tab)