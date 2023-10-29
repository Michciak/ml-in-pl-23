import streamlit as st

# Create a title, header, and subheader
st.title(f'Title')
st.write(f'# Header') # st.header
st.write(f'## Subheader') #st.subheader

# Play with Markdown
st.markdown("""
<span style='color: blue;'>**Markdown**</span> _example_ text

 - some text for example

more text ofr example

$a + a^2$

:red[balloon] for you :balloon:

""", unsafe_allow_html=True) #this argument allows you to use your html/css code in md

# Add a Divider
st.divider()

st.markdown("""
:blue[balloon] for you :balloon:
""")

# Create a button
clicked = st.button("button")

st.button("button2")

st.write(clicked) # state changes to false after true only when another button is clicked

# Add an action to your button - like balloons or snow
if clicked:
    st.balloons()

# Add a slider that prints slider value
v = st.slider("Choose number", -100, 1000, 0, 10)

st.write(f'number is {v}')

# Create an updateable placeholder
placeholder = st.empty()

# Lets try to make a clicker counter
increment = st.button("increment me :balloon:")

# Use the session state
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if increment:
    st.session_state["counter"] += 1

placeholder.write(f'My counter {st.session_state["counter"]}')

# Recreate the button and assign the action
