import streamlit as st

# Define the highlighted title
highlighted_text_title = (
    "<div style='text-align: center;'>"
    "<span style='font-size: 50px; color: gray; font-family: Calibri;'>"
    "<b>SCAN YOUR SKIN</b>"
    "</span>"
    "</div>"
)
# Render the title
st.markdown(highlighted_text_title, unsafe_allow_html=True)

# Add a spacer for layout
st.write("")

# Add the image
st.image("images/welcome.jpg", use_column_width=True)



# Add the team members' names vertically with narrow line spacing and centered
team_members = (
    "<div style='text-align: center; line-height: 1.3;'>"
    "<span style='font-size: 20px; color: gray; font-family: Calibri; font-weight: bold;'>"
    "Jihyeong LEE<br>"
    "Julijana STEIMLE<br>"
    "Liridone ZHUGOLLI<br>"
    "Loredana HOREZEANU"
    "</span>"
    "</div>"
)
# Render the team members
st.markdown(team_members, unsafe_allow_html=True)

# Add a spacer for layout
st.write("")
