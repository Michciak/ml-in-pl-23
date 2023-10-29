import pandas as pd
import streamlit as st

st.title("Widgets Playground")

st.header("Part 1: Experimenting", divider="violet")

############################################################################
# Set the options and the questions

seasons = ["Spring", "Summer", "Autumn", "Winter"]
question = "What's your favourite season?"

############################################################################

st.subheader("Radio", divider="gray")
st.caption("You can only pick one")

selected_radio = st.radio(label=question, options=seasons)

st.write(f"My favourite season is **{selected_radio}**.")

############################################################################

st.subheader("Dropdown / selectbox", divider="gray")
st.caption("You can only pick one")

selected_dropdown = st.selectbox(label=question, options=seasons)
st.write(f"My favourite season is **{selected_dropdown}**.")

############################################################################

st.subheader("Multiselect", divider="gray")
st.caption("You can pick many")

multiselect = st.multiselect(label=question, options=seasons)
st.write(f"My favourite seasons are **{multiselect}**.")

############################################################################

st.subheader("Checkbox", divider="gray")

activated_multiproc = st.checkbox("Do you want to active multiprocessing?")

activated_multiproc

############################################################################

st.subheader("Toggle", divider="gray")

activated_multiproc = st.toggle("Do you want to active multiprocessing?",
                                key = 'auc') # default key is label, streamlit can't track 2 same key variables

activated_multiproc

############################################################################

st.subheader("Slider", divider="gray")

st.write(st.slider("Slider", 0,100,(20,30),10))

############################################################################

st.subheader("Select Slider", divider="gray")

advance_lvl = st.write(st.select_slider("Question", ['can`t', 'beginner', 'can a little', 'semi-advanced', 'advanced']))
############################################################################

st.subheader("Text Input", divider="gray")

text = st.text_input("put there some text")
st.write(f"""
***{text}***
""")

############################################################################

st.subheader("Number Input", divider="gray")

st.write(st.number_input("number of questions?", step = 1))

############################################################################

st.subheader("Date Input", divider="gray")

# st.help(st.date_input)
st.date_input("Select date", format = 'DD/MM/YYYY')
############################################################################

# st.stop() # Comment when you are ready to start this exercise

st.header("Part 2: Putting it together", divider="violet")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()
df = pd.read_csv(raw_data, encoding='ISO-8859-1')

############################################################################
# Make the following script Streamlit-interactive
# 1. Show dataframe only when toggle is on
# 2. Use a multiselect to hide selected columns
# 3. Use a slider to select rows where streams > X 

preview_data = st.toggle("Preview data")

if preview_data:
    all_columns = df.columns.values.tolist()
    hide_columns = st.multiselect('Columns to hide',all_columns)
    stream_threshold = st.slider("threshold", 1000000000)
    df = df.loc[
        df["streams"] > stream_threshold,
        [col for col in all_columns if col not in hide_columns]
    ]
    st.dataframe(df)
    st.download_button(
        label="Download data as CSV",
        data= df.to_csv(),
        file_name='edited_df.csv',
        mime='text/csv',
    )
