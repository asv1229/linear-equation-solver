import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sp

st.set_page_config(page_title="Linear Equation Solver", page_icon="📈")
st.title("Math Solver")

mode = st.sidebar.selectbox("Select Mode", ["Single Equation", "Simultaneous", "Trigonometry", "Quadratics", "Calculus"])

if mode == "Single Equation":
    st.header("Solve $ax + b = c$")
    a = st.number_input("Value for a", value=0.0, key="a1")
    b = st.number_input("Value for b", value=0.0, key="b1")
    c = st.number_input("Value for c", value=0.0, key="c1")
    
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
        a = st.number_input("a", value=0.0, key="a2")
        b = st.number_input("b", value=0.0, key="b2")
        c = st.number_input("c", value=1.0, key="c2")
    with col2:
        d = st.number_input("d", value=0.0, key="d2")
        e = st.number_input("e", value=0.0, key="e2")
        f = st.number_input("f", value=0.0, key="f2")

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
    st.header("Solve trigonometric functions")
    trigfunc = st.selectbox("Choose function", ["sine", "cosine", "tangent", "inverse sine", "inverse cosine", "inverse tangent"])
    value = st.number_input("Value for function", value = 0.0, key = "value")
    if st.button("Solve", key="btn_trig"):
        if trigfunc == "sine":
            trigresult = math.sin(math.radians(value))
            st.success(f"Result: $x = {round(trigresult, 4)}$")
        elif trigfunc == "cosine":
            trigresult = math.cos(math.radians(value))
            st.success(f"Result: $x = {round(trigresult, 4)}$")
        elif trigfunc == "tangent":
            trigresult = math.tan(math.radians(value))
            st.success(f"Result: $x = {round(trigresult, 4)}$")
        elif trigfunc == "inverse sine":
            if -1 <= value <= 1:
                trigresult_rad = math.asin(value)
                trigresult_deg = math.degrees(trigresult_rad)
                st.success(f"Result: $\\arcsin({value}) = {round(trigresult_deg, 4)}^\circ$")
            else:
                st.error("Input for Inverse Sine must be between -1 and 1")

    elif trigfunc == "inverse cosine":
        if -1 <= value <= 1:
            trigresult_rad = math.acos(value)
            trigresult_deg = math.degrees(trigresult_rad)
            st.success(f"Result: $\\arccos({value}) = {round(trigresult_deg, 4)}^\circ$")
        else:
            st.error("Input for Inverse Cosine must be between -1 and 1")

    elif trigfunc == "inverse tangent":
        trigresult_rad = math.atan(value)
        trigresult_deg = math.degrees(trigresult_rad)
        st.success(f"Result: $\\arctan({value}) = {round(trigresult_deg, 4)}^\circ$")


elif mode == "Quadratics":
    st.header("Solve $ax^2 + bx + c = 0$")
    a = st.number_input("Value for a", value=0.0, key="quad_a") 
    b = st.number_input("Value for b", value=0.0, key="quad_b")
    c = st.number_input("Value for c", value=0.0, key="quad_c")

    if a == 0:
        st.warning("If $a=0$, this is a linear equation, not a quadratic!")
    else:
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            st.error("No real solutions (the roots are imaginary).")
        else:
            sqrt_disc = discriminant**0.5
            sol1 = (-b + sqrt_disc) / (2*a)
            sol2 = (-b - sqrt_disc) / (2*a)
        if st.button("Solve", key="btn_quadratic"):
            if discriminant == 0:
                st.success(f"There is one repeated root: $x = {round(sol1, 4)}$")
            else:
                st.success(f"The roots are: $x_1 = {round(sol1, 4)}$ and $x_2 = {round(sol2, 4)}$")



if mode == "Calculus":
    st.header("Calculus Solver")

    # Instructions for the user
    st.info("Note: Use * for multiplication (3*x) and ** for powers (x**2)")

    user_input = st.text_input("Enter your function of x:", value="x**2 + 5*x").strip()

    if user_input:
        try:
            x = sp.symbols('x')
        
            expr = sp.sympify(user_input, locals={'x': x})
        
            st.write("---")
        
            # DERIVATIVE
            deriv = sp.diff(expr, x)
            st.subheader("The Derivative ($f'(x)$)")
            st.latex(r"f'(x) = " + sp.latex(deriv))
        
            # INTEGRAL
            integ = sp.integrate(expr, x)
            st.subheader("The Integral ($\int f(x) dx$)")
            st.latex(r"\int f(x) \, dx = " + sp.latex(integ) + r" + C")
            t.write("---")
            st.subheader("Definite Integral (Area under Curve)")

            col_a, col_b = st.columns(2)
            with col_a:
                lower_limit = st.number_input("Lower limit (a)", value=0.0)
            with col_b:
                upper_limit = st.number_input("Upper limit (b)", value=1.0)

            if st.button("Calculate Area"):
                area = sp.integrate(expr, (x, lower_limit, upper_limit))
                st.latex(rf"\int_{{{lower_limit}}}^{{{upper_limit}}} ({sp.latex(expr)}) \, dx = {sp.latex(area)} \approx {float(area):.4f}")
        
        except Exception as e:
            st.error(f"Math Error: Could not parse '{user_input}'. Check your syntax!")











