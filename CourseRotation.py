import streamlit as st

# Initialize state for each course and semester if not already initialized
required_courses = ['FIN 354', 'FIN 355', 'FIN 358', 'FIN 359', 'FIN 450W']
for course in required_courses:
    if f"{course}_fall" not in st.session_state:
        st.session_state[f"{course}_fall"] = 'In-person'
    if f"{course}_winter" not in st.session_state:
        st.session_state[f"{course}_winter"] = 'In-person'

# Title and Intro
st.title('Course Rotation Schedule')

# Academic Year Dropdown
st.selectbox('Select Academic Year:', ['2023-2024', '2024-2025', '2025-2026'])

# Required Courses
st.subheader('Required Courses')
for course in required_courses:
    # Fall semester dropdown
    fall_option = st.selectbox(
        f"{course} (Fall):", ['In-person', 'Fully Online'], key=f"{course}_fall"
    )
    
    # Winter semester dropdown with conditional options
    winter_options = ['In-person', 'Fully Online'] if fall_option == 'In-person' else ['In-person']
    winter_option = st.selectbox(
        f"{course} (Winter):", options=winter_options, key=f"{course}_winter"
    )

# Notes Section
st.text_area('Notes:', '')

# Validate and Submit Button
if st.button('Submit'):
    # Validation logic here
    st.write('Submitted Successfully')
