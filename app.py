import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))
years, y_ticks = [2019, 2020, 2021, 2022, 2023, 2024, 2025], [0, 50, 100, 150, 200, 250, 300]
wnba_rev, nba_sh, act_pay = [95, 120, 145, 170, 195, 220, 300], [45, 60, 70, 85, 95, 110, 145], [18, 19, 20, 21, 22, 23, 24]
ax.set_title("W.N.B.A. Players’ Compensation", loc='center', fontsize=16, pad=15)
ax.set_ylabel("ANNUAL REVENUE", loc='top', rotation=0)
ax.set_xlim(2018.5, 2029.5); ax.set_ylim(0, 300)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_xticks(years); ax.set_yticks(y_ticks)
ax.set_yticklabels(['0', '50 mil.', '100 mil.', '150 mil.', '200 mil.', '250 mil.', '$300 million'])

st.pyplot(fig)
