import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))
years, y_ticks = [2019, 2020, 2021, 2022, 2023, 2024, 2025], [0, 50, 100, 150, 200, 250, 300]
wnba_rev, nba_sh, act_pay = [95, 120, 145, 170, 195, 220, 300], [45, 60, 70, 85, 95, 110, 145], [18, 19, 20, 21, 22, 23, 24]
ax.set_title("W.N.B.A. Players’ Compensation", loc='center', fontsize=16, pad=15)
ax.set_ylabel("ANNUAL REVENUE", loc='top', rotation=0)
ax.set_xlim(2018.5, 2025.5); ax.set_ylim(0, 305)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_xticks(years); ax.set_yticks(y_ticks)
ax.set_yticklabels(['0', '50 mil.', '100 mil.', '150 mil.', '200 mil.', '250 mil.', '$300 million'])

ax.bar(years, wnba_rev, width=0.6, color='#e0e0e0')
ax.bar(years, nba_sh, width=0.4, color='#9eb3ff')
ax.bar(years, act_pay, width=0.18, color='#4d52a4')

ax.plot(2026.3, 270, marker='s', color='#e0e0e0', markersize=12, clip_on=False)
ax.text(2026.5, 270, "How much money the W.N.B.A. makes", color='#777777', va='center', fontsize=8)
ax.plot(2026.3, 230, marker='s', color='#9eb3ff', markersize=12, clip_on=False)
ax.text(2026.5, 230, "Money the players would share,\nif they were paid like N.B.A. players", color='#6072c4', va='center', fontsize=8)
ax.plot(2026.3, 190, marker='s', color='#4d52a4', markersize=12, clip_on=False)
ax.text(2026.5, 190, "Money that W.N.B.A.\nplayers actually make", color='#2c2f63', va='center', fontsize=8)

st.pyplot(fig)
