import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide")

fig, ax = plt.subplots(figsize=(64, 48))
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
y_ticks= [0, 50, 100, 150, 200, 250, 300]
wnba_rev = [95, 120, 145, 170, 195, 220, 300]
nba_sh = [45, 60, 70, 85, 95, 110, 145]
act_pay = [18, 19, 20, 21, 22, 23, 24]

ax.set_title("W.N.B.A. Players’ Compensation", loc='center', fontsize=120, pad=50)
ax.set_ylabel("ANNUAL REVENUE", loc='top', rotation=0, fontsize=90)
ax.set_xlim(2018.5, 2025.5); ax.set_ylim(0, 305)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.set_xticks(years); ax.set_yticks(y_ticks)
ax.set_yticklabels(['0', '50 million', '100 million', '150 million', '200 million', '250 million', '$300 million'],fontsize=90)
ax.tick_params(axis="x", labelsize=90, pad=30)

ax.bar(years, wnba_rev, width=0.6, color='#e0e0e0')
ax.bar(years, nba_sh, width=0.4, color='#9eb3ff')
ax.bar(years, act_pay, width=0.18, color='#4d52a4')

ax.plot(2026.3, 270, marker='s', color='#e0e0e0', markersize=96, clip_on=False)
ax.text(2026.5, 270, "How much money the W.N.B.A. makes", color='#777777', va='center', fontsize=64)
ax.plot(2026.3, 230, marker='s', color='#9eb3ff', markersize=96, clip_on=False)
ax.text(2026.5, 230, "Money the players would share,\nif they were paid like N.B.A. players", color='#6072c4', va='center', fontsize=64)
ax.plot(2026.3, 190, marker='s', color='#4d52a4', markersize=96, clip_on=False)
ax.text(2026.5, 190, "Money that W.N.B.A.\nplayers actually make", color='#2c2f63', va='center', fontsize=64)

fig = go.Figure()
# WNBA Revenue (Grey Bar)
fig.add_trace(
    go.Bar(
        x=years,
        y=wnba_rev,
        name="How much money the W.N.B.A. makes",
        marker_color="#e0e0e0",
        width=0.6,
        hovertemplate="%{y} mil.<extra></extra>",
    )
)

# NBA Scale Share (Light Blue Bar)
fig.add_trace(
    go.Bar(
        x=years,
        y=nba_sh,
        name="Money the players would share, if paid like N.B.A. players",
        marker_color="#9eb3ff",
        width=0.4,
        hovertemplate="%{y} mil.<extra></extra>",
    )
)

# Actual Player Pay (Dark Blue Bar)
fig.add_trace(
    go.Bar(
        x=years,
        y=act_pay,
        name="Money that W.N.B.A. players actually make",
        marker_color="#4d52a4",
        width=0.18,
        hovertemplate="%{y} mil.<extra></extra>",
    )
)

# Overlay bars and format layout
fig.update_layout(
    barmode="overlay",
    title=dict(text="W.N.B.A. Players’ Compensation", x=0.5, font=dict(size=28)),
    xaxis=dict(tickmode="linear", tickfont=dict(size=18)),
    yaxis=dict(
        title="ANNUAL REVENUE",
        tickvals=[0, 50, 100, 150, 200, 250, 300],
        ticktext=[
            "0",
            "50 million",
            "100 million",
            "150 million",
            "200 million",
            "250 million",
            "$300 million",
        ],
        tickfont=dict(size=18),
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=True,
)

left_margin, center_col, right_margin = st.columns([1, 8, 1])
with center_col:
  st.plotly_chart(fig, use_container_width=True)
