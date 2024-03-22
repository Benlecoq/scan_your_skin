import streamlit as st

st.header("Contacts")

# Define a list of team members with their names and email addresses
team_members = [
    {"name": "Jihyeong LEE", "email": "lee.jihyeong.426@gmail.com"},
    {"name": "Julijana STEIMLE", "email": "jn.steimle@gmail.com"},
    {"name": "Liridone ZHUGOLLI", "email": "liridona.zhugolli@gmail.com"},
    {"name": "Loredana HOREZEANU", "email": "horezeanu1h@gmail.com"},
]

# Iterate over the team members to render their contact information
for member in team_members:
    team_member_html = (
        f"<div style='line-height: 1.3; display: flex; align-items: center;'>"
        f"<span style='font-size: 20px; color: black; font-family: Calibri; font-weight: bold;'>"
        f"{member['name']}"
        f"</span>"
        f"<a href='mailto:{member['email']}'>"
        f"<img src='https://img.shields.io/badge/-{member['email']}-c14438?style=flat-square&logo=Gmail&logoColor=white' alt='Mail Badge' style='margin-left: 10px;'>"
        f"</a>"
        f"</div>"
    )
    st.markdown(team_member_html, unsafe_allow_html=True)

# Add a spacer for layout
st.write("")

# GitHub URL
github_url = "https://github.com/liridonezhk/scan_your_skin"
github_user_repo = "/".join(github_url.split('/')[-2:])
github_shields_url = f"https://img.shields.io/github/stars/{github_user_repo}?style=social"

st.markdown(f"Click to endorse: <a href='{github_url}'><img src='{github_shields_url}' alt='GitHub Repo stars' style='margin-left: 10px;'></a>", unsafe_allow_html=True)

# Add a spacer for layout
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Function to get the absolute path of the image file
def get_image_path(image_name):
    # Specify the correct directory path
    directory_path = "/mount/src/scan_your_skin/front_end/images/"
    # Construct the full path to the image
    image_path = os.path.join(directory_path, image_name)
    return image_path


image_path = os.path.join(current_dir, "images", "QR_code.png")
st.image(image_path)