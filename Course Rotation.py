import streamlit as st

# Initialize lists for courses
required_courses = ['FIN 354', 'FIN 355', 'FIN 358', 'FIN 359', 'FIN 450W']
restricted_electives_fall = ['FIN 451', 'FIN 456']
restricted_electives_winter = ['FIN 453', 'FIN 455', 'FIN 457']

# Title and Intro
st.title('Course Rotation Schedule')

# Academic Year Dropdown
academic_year = st.selectbox('Select Academic Year:', ['2023-2024', '2024-2025', '2025-2026'])

# Required Courses
st.subheader('Required Courses')
required_course_modality_fall = {course: st.selectbox(f"{course} (Fall):", ['In-person', 'Fully Online']) for course in required_courses}
required_course_modality_winter = {course: st.selectbox(f"{course} (Winter):", ['In-person', 'Fully Online']) for course in required_courses}

# Restricted Electives
st.subheader('Restricted Electives (Fall)')
restricted_elective_modality_fall = {course: st.selectbox(f"{course} (Fall):", ['In-person', 'Fully Online']) for course in restricted_electives_fall}

st.subheader('Restricted Electives (Winter)')
restricted_elective_modality_winter = {course: st.selectbox(f"{course} (Winter):", ['In-person', 'Fully Online']) for course in restricted_electives_winter}

# Notes Section
notes = st.text_area('Notes:', '')

# Validate and Submit Button
if st.button('Submit'):
    # Validation logic here
    st.write('Submitted Successfully')
