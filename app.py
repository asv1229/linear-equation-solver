import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title="Linear Equation Solver", page_icon="📈")

st.title("🧮 Linear Equation Solver")
st.write("Solve $ax + b = c$ or simultaneous equations.")

# Choose Mode
mode = st.sidebar.selectbox("Select Mode", ["Single Equation", "Simultaneous"])

if mode == "Single Equation":
    st.header("Solve $ax + b = c$")
    a = st.number_input("Value for a", value=1.0)
    b = st.number_input("Value for b", value=0.0)
    c = st.number_input("Value for c", value=0.0)
    
    if st.button("Solve"):
        if a == 0:
            st.error("a cannot be zero!")
        else:
            x = (c - b) / a
            st.success(f"Result: $x = {x}$")

else:
    st.header("Solve $ax + by = c$ and $dx + ey = f$")
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=1.0)
        c = st.number_input("c", value=1.0)
    with col2:
        d = st.number_input("d", value=1.0)
        e = st.number_input("e", value=-1.0)
        f = st.number_input("f", value=1.0)

    if st.button("Solve System"):
        D = (a * e) - (b * d)
        if D != 0:
            x = ((c * e) - (b * f)) / D
            y = ((a * f) - (c * d)) / D
            st.success(f"Results: $x = {x}$, $y = {y}$")
        else:
            st.warning("Lines are parallel (no solution).")

if st.button("Solve System"):
    D = (a * e) - (b * d)
    if D != 0:
        x_res = ((c * e) - (b * f)) / D
        y_res = ((a * f) - (c * d)) / D
        st.success(f"Results: $x = {x_res}$, $y = {y_res}$")

        # --- GRAPHING LOGIC ---
        fig, ax = plt.subplots()
        
        # Create a range for x around the solution
        x_vals = np.linspace(x_res - 10, x_res + 10, 400)
        
        # Rearrange equations for y: y = (c - ax) / b
        # We handle the case where b or e might be 0 (vertical lines)
        if b != 0:
            y1 = (c - a * x_vals) / b
            ax.plot(x_vals, y1, label=f'{a}x + {b}y = {c}')
        else:
            ax.axvline(x=c/a, label=f'{a}x = {c}', color='blue')

        if e != 0:
            y2 = (f - d * x_vals) / e
            ax.plot(x_vals, y2, label=f'{d}x + {e}y = {f}')
        else:
            ax.axvline(x=f/d, label=f'{d}x = {f}', color='orange')

        # Mark the intersection
        ax.plot(x_res, y_res, 'ro') 
        ax.annotate(f'({round(x_res, 2)}, {round(y_res, 2)})', (x_res, y_res), xytext=(5, 5), textcoords='offset points')

        ax.axhline(0, color='black',linewidth=0.5)
        ax.axvline(0, color='black',linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        
        # Show the plot in Streamlit
        st.pyplot(fig)
