import streamlit as st

st.header("Contacts")

# Add the team members' names vertically with narrow line spacing and centered
team_members = (
    "<div style='line-height: 1.3; display: flex; align-items: center;'>"
    "<span style='font-size: 20px; color: black; font-family: Calibri; font-weight: bold;'>"
    "Jihyeong LEE"
    "</span>"
    "<a href='mailto:lee.jihyeong.426@gmail.com'>"
    "<img src='https://img.shields.io/badge/-lee.jihyeong.426@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white' alt='Mail Badge' style='margin-left: 10px;'>"
    "</a>"
    "</div>"
)

# Render the team members
st.markdown(team_members, unsafe_allow_html=True)


team_members = (
    "<div style='line-height: 1.3; display: flex; align-items: center;'>"
    "<span style='font-size: 20px; color: black; font-family: Calibri; font-weight: bold;'>"
    "Julijana STEIMLE"
    "</span>"
    "<a href='mailto:jn.steimle@gmail.com'>"
    "<img src='https://img.shields.io/badge/-jn.steimle@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white' alt='Mail Badge' style='margin-left: 10px;'>"
    "</a>"
    "</div>"
)

# Render the team members
st.markdown(team_members, unsafe_allow_html=True)


team_members = (
    "<div style='line-height: 1.3; display: flex; align-items: center;'>"
    "<span style='font-size: 20px; color: black; font-family: Calibri; font-weight: bold;'>"
    "Liridone ZHUGOLLI"
    "</span>"
    "<a href='mailto:liridona.zhugolli@gmail.com'>"
    "<img src='https://img.shields.io/badge/-liridona.zhugolli@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white' alt='Mail Badge' style='margin-left: 10px;'>"
    "</a>"
    "</div>"
)

# Render the team members
st.markdown(team_members, unsafe_allow_html=True)


team_members = (
    "<div style='line-height: 1.3; display: flex; align-items: center;'>"
    "<span style='font-size: 20px; color: black; font-family: Calibri; font-weight: bold;'>"
    "Loredana HOREZEANU"
    "</span>"
    "<a href='mailto:horezeanu1h@gmail.com'>"
    "<img src='https://img.shields.io/badge/-horezeanu1h@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white' alt='Mail Badge' style='margin-left: 10px;'>"
    "</a>"
    "</div>"
)

# Render the team members
st.markdown(team_members, unsafe_allow_html=True)

# Add a spacer for layout
st.write("")# Add a spacer for layout
st.write("")

# 뒷부분을 Githuh URL 로 바꾸기
import streamlit as st

github_url = "https://github.com/liridonezhk/scan_your_skin"
github_shields_url = f"https://img.shields.io/github/stars/{github_url.split('/')[-2]}/{github_url.split('/')[-1]}?style=social"

st.markdown(f"Click to endorse: <a href='{github_url}'><img src='{github_shields_url}' alt='GitHub Repo stars' style='color:black'></a>", unsafe_allow_html=True)
