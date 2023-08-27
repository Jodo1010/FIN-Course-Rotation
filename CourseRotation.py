import streamlit as st

# Initialize state for each required course and semester if not already initialized
required_courses = ['FIN 354', 'FIN 355', 'FIN 358', 'FIN 359', 'FIN 450W']
restricted_electives_fall = ['FIN 451', 'FIN 456']
restricted_electives_winter = ['FIN 453', 'FIN 455', 'FIN 457']

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
col1, col2 = st.columns(2)
with col1:
    st.subheader('Fall')
with col2:
    st.subheader('Winter')

for course in required_courses:
    col1, col2 = st.columns(2)
    
    # Fall semester dropdown in the left column
    with col1:
        fall_option = st.selectbox(
            f"{course}:", ['In-person', 'Fully Online'], key=f"{course}_fall"
        )
    
    # Display Winter semester options in the right column based on Fall selection
    with col2:
        winter_options = 'In-person, Fully Online' if fall_option == 'In-person' else 'In-person'
        st.write(f"{course} options: {winter_options}")

# Restricted Electives
st.subheader('Restricted Electives')
col1, col2 = st.columns(2)

with col1:
    st.write("Fall")
    for course in restricted_electives_fall:
        st.text(f"{course}: In-Person or Fully Online")

with col2:
    st.write("Winter")
    for course in restricted_electives_winter:
        st.text(f"{course}: In-Person or Fully Online")

# Notes Section
st.text_area('Notes:', '')

# Validate and Submit Button
if st.button('Submit'):
    # Validation logic here
    st.write('Submitted Successfully')