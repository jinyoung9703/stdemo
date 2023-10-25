import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, penguins🐧',
                   page_icon='🐧')
st.sidebar.header('Hello, penguins!🐧')