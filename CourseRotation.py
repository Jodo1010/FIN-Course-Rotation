import streamlit as st

# Initialize state for each required course and semester if not already initialized
required_courses = ['FIN 354', 'FIN 355', 'FIN 358', 'FIN 359', 'FIN 450W']
restricted_electives_fall = ['FIN 451', 'FIN 456']
restricted_electives_winter = ['FIN 453', 'FIN 455', 'FIN 457']
required_graduate_courses = ['FIN 502', 'FIN 620']

for course in required_courses:
    if f"{course}_fall" not in st.session_state:
        st.session_state[f"{course}_fall"] = 'In-person'
    if f"{course}_winter" not in st.session_state:
        st.session_state[f"{course}_winter"] = 'In-person'

# Initialize state for each required graduate course and semester if not already initialized

for course in required_graduate_courses:
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

# Insert additional text
st.write("All of the FIN required courses are offered in the Fall and Winter semester in multiple modalities throughout the academic year (in-person and fully online). ")
st.write("Adjust the Fall semester modality for each course to determine the modality options for the same course in the Winter semester.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Fall**")
with col2:
    st.markdown("<div style='text-align: right'><strong>Winter</strong></div>", unsafe_allow_html=True)

for course in required_courses:
    col1, col2 = st.columns(2)

    # Fall semester dropdown in the left column
    with col1:
        fall_option = st.selectbox(f"**{course}:**", ['In-person', 'Fully Online'], key=f"{course}_fall")

    # Display Winter semester options in the right column based on Fall selection
    with col2:
        st.markdown(f"<div style='text-align: right'><strong>{course}:<strong></div>", unsafe_allow_html=True)
        winter_options = 'In-person, Fully Online' if fall_option == 'In-person' else 'In-person'
        st.markdown(f"<div style='text-align: right'>{winter_options}</div>", unsafe_allow_html=True)

# Restricted Electives
st.subheader('Restricted Electives')

# Insert additional text
st.write("All of the FIN restricted electives are offered at least one time in the academic year and in any modality given the majority of the FIN restricted electives are offered in-person. Below is the list of restricted courses that will be offered in the Fall and Winter semester.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Fall**")
    for course in restricted_electives_fall:
        st.markdown(f"<div style='text-align: left'>{course}: In-Person or Fully Online</div>", unsafe_allow_html=True)
        
with col2:
    st.markdown("<div style='text-align: right'><strong>Winter</strong></div>", unsafe_allow_html=True)

    for course in restricted_electives_winter:
        st.markdown(f"<div style='text-align: right'>{course}: In-Person or Fully Online</div>", unsafe_allow_html=True)

# Required Graduate Courses
st.subheader('Required Graduate Courses')
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div style='text-align: left'><strong>Fall</strong></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: right'><strong>Winter</strong></div>", unsafe_allow_html=True)

for course in required_graduate_courses:
    col1, col2 = st.columns(2)

    # Fall semester dropdown in the left column
    with col1:
        fall_option = st.selectbox(f"**{course}:**", ['In-person', 'Fully Online'], key=f"{course}_fall")

    # Display Winter semester options in the right column based on Fall selection
    with col2:
        st.markdown(f"<div style='text-align: right'>**{course}:**</div>", unsafe_allow_html=True)
        winter_options = 'In-person, Fully Online' if fall_option == 'In-person' else 'In-person'
        st.markdown(f"<div style='text-align: right'>**{winter_options}**</div>", unsafe_allow_html=True)


# Notes Section
st.text_area('Notes:', '')

# Validate and Submit Button
if st.button('Submit'):
    st.write('Submitted Successfully')
