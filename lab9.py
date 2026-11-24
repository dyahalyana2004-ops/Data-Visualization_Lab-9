"""
Lab 9: Design Principles and Chartjunk
Complete Streamlit app with Cluttered vs Improved comparison + Assignment modifications.

Assignment changes applied:
1. Branch names/values changed (still fictional, clearly stated)
2. Title adjusted to describe intended message
3. Added source & author note at bottom
4. Added option to show 6 categories (to test readability)
5. Removed another unnecessary visual element in Improved version (left spine)
6. Kept zero baseline, value labels, accent color, horizontal grid only
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------------
# Page config
# ---------------------------------------------------------------
st.set_page_config(page_title="Lab 9 | Chart Design", layout="wide")

# ---------------------------------------------------------------
# Data (MODIFIED per assignment - fictional practice values)
# Original: North/South/East/West = 96,99,98,100
# New: 6 branches to test readability (assignment step 3)
# ---------------------------------------------------------------
data = pd.DataFrame({
    "Branch": ["North", "South", "East", "West", "Central", "Coastal"],
    "Sales": [96, 99, 98, 100, 97, 101],  # fictional practice values
})

# Author name for attribution (assignment step 3)
AUTHOR_NAME = "Dyah Alyana Sulaksono"

# ---------------------------------------------------------------
# UI
# ---------------------------------------------------------------
st.title("Designing a Clearer Bar Chart")
st.markdown(
    "**Lab 9 – Design Principles and Chartjunk**  \n"
    "Compare a *cluttered* chart (truncated axis, heavy decoration) "
    "with an *improved* chart (zero baseline, clear labels, one accent color)."
)

version = st.radio(
    "Choose a chart",
    ["Cluttered", "Improved"],
    horizontal=True,
)

show_six = st.checkbox(
    "Show all 6 categories (test readability)", value=True,
    help="Uncheck to show only the original 4 branches.",
)

# Allow filtering back to 4 categories (assignment: test readability)
plot_data = data if show_six else data.head(4)

# ---------------------------------------------------------------
# Figure
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.8))

if version == "Cluttered":
    # --- Cluttered version: truncated axis + decoration ---
    bars = ax.bar(
        plot_data["Branch"],
        plot_data["Sales"],
        color=["#8FB9A8", "#D8B365", "#B2ABD2", "#5E3C99", "#F4A582", "#66C2A5"],
        edgecolor="black",
        linewidth=1.2,
    )
    ax.set_ylim(95, 102)                     # truncated axis (misleading)
    ax.set_facecolor("#E8E8E8")              # heavy background
    ax.grid(True, which="both", color="white", linewidth=2)  # excessive grid
    ax.set_title("SALES PERFORMANCE!!", fontsize=15, fontweight="bold")
    # Extra chartjunk: shadow-like border, 3D-ish frame
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)
    ax.tick_params(axis="x", rotation=25)    # angled labels (bad readability)

else:
    # --- Improved version: zero baseline + clear labels + one accent ---
    bars = ax.bar(plot_data["Branch"], plot_data["Sales"], color="#4C78A8")

    # Highlight the highest value with one accent color
    max_idx = plot_data["Sales"].idxmax()
    bars[list(plot_data.index).index(max_idx)].set_color("#E07A3F")

    ax.set_ylim(0, 110)                      # zero baseline
    ax.set_yticks(range(0, 101, 20))         # natural increments
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=10)
    ax.set_title(
        "Coastal branch recorded the highest sales",
        fontsize=14, fontweight="bold",
    )
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.7)
    ax.set_axisbelow(True)

    # Remove non-data decoration (top, right, AND left spines)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)     # extra removal (assignment step 2)
    ax.tick_params(axis="y", length=0)       # clean tick marks
    ax.set_ylabel("Sales (units)")

# ---------------------------------------------------------------
# Source & author note (assignment step 3)
# ---------------------------------------------------------------
fig.text(
    0.01, 0.01,
    f"Data: fictional practice values (2026) | Chart: {AUTHOR_NAME}",
    fontsize=8, color="#555555", ha="left",
)

fig.tight_layout(rect=[0, 0.03, 1, 1])
st.pyplot(fig, clear_figure=True)

# Caption changes with version
if version == "Cluttered":
    st.caption(
        "⚠️ Cluttered: truncated axis (starts at 95) exaggerates differences "
        "between values that actually range only 96–101. Heavy grid, angled labels, "
        "and multi-color bars distract from the data."
    )
else:
    st.caption(
        "✅ Improved: zero baseline keeps bar lengths proportional. "
        "Natural ticks, value labels, one accent color, light horizontal grid, "
        "and minimal spines support accurate reading."
    )

# ---------------------------------------------------------------
# Design standards checklist (for the critique/submission)
# ---------------------------------------------------------------
with st.expander("📋 Ten Design Standards checklist (click to expand)"):
    st.markdown(
        """
        | Standard | Cluttered | Improved |
        |---|---|---|
        | Chart format | Web (ok) | Web (ok) |
        | Color | Too many, not meaningful | Sparing, one accent |
        | Text & labels | Shouty title, no units | Descriptive title, y-label with units |
        | Readability | Angled x-labels | Horizontal, legible |
        | Scales | Truncated (95–102) ❌ | Zero baseline ✅ |
        | Data integrity | Exaggerates differences ❌ | Proportional ✅ |
        | Chartjunk | Heavy grid, borders, background | Minimal |
        | Data density | 6 bars (readable) | 6 bars (readable) |
        | Data richness | Values hidden | Value labels shown |
        | Attribution | None | Source + author note |
        """
    )
