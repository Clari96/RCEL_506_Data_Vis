import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide")

years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
wnba_rev = [95, 120, 145, 170, 195, 220, 300]
nba_sh = [45, 60, 70, 85, 95, 110, 145]
act_pay = [18, 19, 20, 21, 22, 23, 24]

fig = go.Figure()

# WNBA Revenue (Grey Bar)
fig.add_trace(
    go.Bar(
        x=years,
        y=wnba_rev,
        name="How much money the W.N.B.A. makes",
        marker_color="#e0e0e0",
        width=0.6,
        hovertemplate="%{y} million<extra></extra>",
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
        hovertemplate="%{y} million<extra></extra>",
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
        hovertemplate="%{y} million<extra></extra>",
    )
)

# Overlay y formato del layout
fig.update_layout(
    barmode="overlay",
    title=dict(
        text="W.N.B.A. Players’ Compensation",
        x=0.5,
        xanchor="center",
        xref="plot",
        font=dict(size=28),
    ),
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
