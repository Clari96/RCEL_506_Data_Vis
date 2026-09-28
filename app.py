import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("W.N.B.A. Players’ Compensation", loc='center', fontsize=16, pad=15)
ax.set_ylabel("ANNUAL REVENUE", loc='top', rotation=0)
