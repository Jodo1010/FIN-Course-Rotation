import streamlit as st

# Initialize state for each required course and semester if not already initialized
required_courses = ['FIN 354', 'FIN 355', 'FIN 358', 'FIN 359', 'FIN 450W']
restricted_electives_fall = ['FIN 451', 'FIN 456']
restricted_electives_winter = ['FIN 453', 'FIN 455', 'FIN 457']
required_graduate_courses = ['FIN 502', 'FIN 620']
required_core = ['FIN 350']

for course in required_courses + required_graduate_courses:
    if f"{course}_fall" not in st.session_state:
        st.session_state[f"{course}_fall"] = 'In-person'
    if f"{course}_winter" not in st.session_state:
        st.session_state[f"{course}_winter"] = 'In-person'

    
# Title and Intro
st.title('FIN Course Offering & Modality Schedules')

# Academic Year Dropdown
st.selectbox('Select Academic Year:', ['2023-2024', '2024-2025', '2025-2026'])

# Legend Key
# st.write('### Legend Key')
st.markdown("""
- **In-person**: 
  - Face-to-Face
  - Hybrid (Face-to-Face & Fully Online) 
- **Fully Online**:
  - Online Asynchronous
  - Online Synchronous
  - Online Hybrid (Asynchronous & Synchronous) 
""")

st.markdown("""
<span style='color: #046A38;'>To access the approved modality rotation, click the button below:</span>
""", unsafe_allow_html=True)

with open('Course-Modality-Matrix.pdf', 'rb') as f:
    pdf_bytes = f.read()

st.download_button(
    label="Course Modality Policy",
    data=pdf_bytes,
    file_name='Course-Modality-Matrix.pdf',
    mime='application/pdf',
    key='download-button'
)

# Update button to refresh options based on Winter selections
# if st.button('Update Fall Options Based on Winter Selections'): #I commented out the 'Update' button. 
for course in required_courses + required_graduate_courses:
    if st.session_state[f"{course}_winter"] == 'Fully Online':
        st.session_state[f"{course}_fall"] = 'In-person'

# ------------------------------- Required Core -- FIN 350 
st.subheader('Required Core Course')

# Insert additional text
st.write("At least 5 to 10 sections of FIN 350 will offered in each of the Fall and Winter semesters.")
st.markdown("""
- At least 50% of the FIN 350 sections in each semester are in-person. 
""")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Fall</strong></div>", unsafe_allow_html=True)
    for course in required_core:
        st.markdown(f"<div style='text-align: center'>{course}: In-Person and Fully Online</div>", unsafe_allow_html=True)
        
with col2:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Winter</strong></div>", unsafe_allow_html=True)

    for course in required_core:
        st.markdown(f"<div style='text-align: center'>{course}: In-Person and Fully Online</div>", unsafe_allow_html=True)

# -------------------------------- Required Courses
st.subheader('Required Undergraduate Courses')

# Insert additional text
st.write("All of the FIN required courses are offered in the Fall and Winter semester in multiple modalities throughout the academic year (in-person and fully online). ")
st.markdown("""
- Use the dropdown menus below to adjust a semester's modality for each course to determine the modality options for the same course in either semester.
- The dropdown menus will self-adjust if an unallowed sequence of modalities is selected e.g., selecting a fully online Required course in both the Fall and Winter semester. 
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Fall</strong></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Winter</strong></div>", unsafe_allow_html=True)

for course in required_courses:
    col1, col2 = st.columns(2)

    # Update Fall options if Winter option is selected before Fall
    if st.session_state[f"{course}_winter"] == 'Fully Online':
        st.session_state[f"{course}_fall"] = 'In-person'

    # Fall semester dropdown in the left column
    with col1:
        fall_option = st.selectbox(f"**{course}:**", ['In-person', 'Fully Online'], key=f"{course}_fall")

    # Display Winter semester options in the right column based on Fall selection
    with col2:
        winter_options = ['In-person', 'Fully Online'] if fall_option == 'In-person' else ['In-person']
        winter_option = st.selectbox(f"**{course}:**", winter_options, key=f"{course}_winter")



# --------------------------- Required Graduate Courses
st.subheader('Required Graduate Courses')

# Insert additional text
st.write("All of the FIN required graduate courses are offered in the Fall and Winter semester in multiple modalities throughout the academic year (in-person and fully online). ")
st.markdown("""
- Use the dropdown menus below to adjust a semester's modality for each course to determine the modality options for the same course in either semester.
- The dropdown menus will self-adjust if an unallowed sequence of modalities is selected e.g., selecting a fully online Required course in both the Fall and Winter semester. 
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Fall</strong></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Winter</strong></div>", unsafe_allow_html=True)

for course in required_graduate_courses:
    col1, col2 = st.columns(2)

    # Update Fall options if Winter option is selected before Fall
    if st.session_state[f"{course}_winter"] == 'Fully Online':
        st.session_state[f"{course}_fall"] = 'In-person'

    # Fall semester dropdown in the left column
    with col1:
        fall_option = st.selectbox(f"**{course}:**", ['In-person', 'Fully Online'], key=f"{course}_fall")

    # Display Winter semester options in the right column based on Fall selection
    with col2:
        winter_options = ['In-person', 'Fully Online'] if fall_option == 'In-person' else ['In-person']
        winter_option = st.selectbox(f"**{course}:**", winter_options, key=f"{course}_winter")



# ------------------------------- Restricted Electives
st.subheader('Restricted Undergraduate Electives')

# Insert additional text
st.write("All of the FIN restricted electives are offered at least one time in the academic year and in any modality.  Below is the list of restricted courses that will be offered in the academic year, by semester.")
st.markdown("""
- The majority of the FIN restricted electives are offered in-person.
""")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Fall</strong></div>", unsafe_allow_html=True)
    for course in restricted_electives_fall:
        st.markdown(f"<div style='text-align: center'>{course}: In-Person or Fully Online</div>", unsafe_allow_html=True)
        
with col2:
    st.markdown("<div style='text-align: center'><span style='color: #046A38;'><strong>Winter</strong></div>", unsafe_allow_html=True)

    for course in restricted_electives_winter:
        st.markdown(f"<div style='text-align: center'>{course}: In-Person or Fully Online</div>", unsafe_allow_html=True)








# # ------------------------------- Notes Section
# st.text_area('Notes:', '')

# # Validate and Submit Button
# if st.button('Submit'):
#     st.write('Submitted Successfully')
