import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data(raw_file):
    df = pd.read_csv(raw_file, encoding='ISO-8859-1')
    return df

st.title("Spotify data viz playground")

raw_data = st.file_uploader("Upload CSV file")

if raw_data is None:
    st.warning("Please upload a file")
    st.stop()

df = load_data(raw_data)

with st.expander("Data preview"):
    st.dataframe(df.head(15))

st.header("Part 1: Visualize plots", divider="violet")

############################################################################
# Streamlit native charts

st.subheader("Streamlit native chart", divider="gray")
st.scatter_chart(
    df,
    x = 'streams',
    y = 'in_spotify_playlists',
    color = 'mode',
    size = 'in_apple_playlists'
)

############################################################################
# Altair

st.subheader("Altair", divider="gray")

############################################################################
# Plotly Express

st.subheader("Plotly Express", divider="gray")

plotly_fig = px.scatter(
    df,
    x = 'streams',
    y = 'in_spotify_playlists',
    color = 'mode',
    size = 'in_apple_playlists'
)

st.plotly_chart(plotly_fig)

############################################################################
# Seaborn

st.subheader("Seaborn", divider="gray")

# f = sns.pairplot(df, vars=["bpm", "streams", ])

############################################################################
# Matplotlib

st.subheader("Matplotlib", divider="gray")

fig, ax = plt.subplots(figsize=(12,8))
df["streams"].plot(ax=ax)

st.pyplot(fig.figure)

############################################################################

st.header("Part 2: Layout plots", divider="violet")

############################################################################
# Sidebar: put the file upload in the sidebar

# side_fig = st.plotly_chart(plotly_fig)

with st.sidebar:
    st.plotly_chart(plotly_fig)

st.sidebar.plotly_chart(plotly_fig)

############################################################################
# Tabs: take plots into tabs. Show both notations.

col1, col2 = st.tabs(["Col1","Col2"])

with col1:
    st.scatter_chart(
        df,
        x='streams',
        y='in_spotify_playlists',
        color='mode',
        size='in_apple_playlists'
    )

with col2:
    st.scatter_chart(
        df,
        x='streams',
        y='in_spotify_playlists',
        color='mode',
        size='in_apple_playlists'
    )

############################################################################
# Columns: take plots into columns. Show both notations.

# c1, c2 = st.columns(2)
c1, c2 = st.columns((1,2))

with c1:
    st.scatter_chart(
        df,
        x='streams',
        y='in_spotify_playlists',
        color='mode',
        size='in_apple_playlists'
    )

with c2:
    st.scatter_chart(
        df,
        x='streams',
        y='in_spotify_playlists',
        color='mode',
        size='in_apple_playlists'
    )