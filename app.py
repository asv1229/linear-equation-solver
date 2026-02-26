import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

st.set_page_config(page_title="Linear Equation Solver", page_icon="📈")
st.title("🧮 Linear Equation Solver")

mode = st.sidebar.selectbox("Select Mode", ["Single Equation", "Simultaneous", "Trigonometry"])

if mode == "Single Equation":
    st.header("Solve $ax + b = c$")
    a = st.number_input("Value for a", value=1.0, key="a1")
    b = st.number_input("Value for b", value=0.0, key="b1")
    c = st.number_input("Value for c", value=0.0, key="c1")
    
    # We give this button a unique key
    if st.button("Solve Single", key="btn_single"):
        if a == 0:
            st.error("a cannot be zero!")
        else:
            x = (c - b) / a
            st.success(f"Result: $x = {round(x, 4)}$")

elif mode == "Simultaneous":
    st.header("Solve $ax + by = c$ and $dx + ey = f$")
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("a", value=1.0, key="a2")
        b = st.number_input("b", value=1.0, key="b2")
        c = st.number_input("c", value=1.0, key="c2")
    with col2:
        d = st.number_input("d", value=1.0, key="d2")
        e = st.number_input("e", value=-1.0, key="e2")
        f = st.number_input("f", value=1.0, key="f2")

    if st.button("Solve System", key="btn_sim"):
        D = (a * e) - (b * d)
        if D != 0:
            x_res = ((c * e) - (b * f)) / D
            y_res = ((a * f) - (c * d)) / D
            st.success(f"Results: $x = {round(x_res, 4)}$, $y = {round(y_res, 4)}$")

            # Graphing
            fig, ax = plt.subplots()
            x_vals = np.linspace(x_res - 10, x_res + 10, 400)
            
            if b != 0:
                y1 = (c - a * x_vals) / b
                ax.plot(x_vals, y1, label=f'{a}x + {b}y = {c}')
            if e != 0:
                y2 = (f - d * x_vals) / e
                ax.plot(x_vals, y2, label=f'{d}x + {e}y = {f}')

            ax.plot(x_res, y_res, 'ro') 
            ax.grid(True, linestyle='--')
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("Lines are parallel (no solution).")
elif mode == "Trigonometry":
    st.header("Solve trigonometirc functions")
    trigfunc = st.selectbox("Choose function", ["sine", "cosine", "tangent", "inverse sine", "inverse cosine", "inverse tangent"])
    value = st.number_input("Value for function", value = 0.0, key = "value")
    if trigfunc == "sine":
        trigresult = math.sin(math.radians(value))
        st.success(f"Result: $x = {round(value, 4)}$")
    elif trigfunc == "cosine":
        trigresult = math.cos(math.radians(value))
        st.success(f"Result: $x = {round(value, 4)}$")
    elif trigfunc == "tangent":
        trigresult = math.tan(math.radians(value))
        st.success(f"Result: $x = {round(value, 4)}$")


