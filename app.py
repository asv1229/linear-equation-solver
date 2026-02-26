import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sp
import pandas as pd
from scipy import stats


st.set_page_config(layout="wide")
st.set_page_config(page_title="A Math Solver", page_icon="➕")
st.title("Math Solver")

mode = st.sidebar.selectbox("Select Mode", ["Single Equation", "Simultaneous", "Trigonometry", "Quadratics", "Calculus", "Statistics", "Unit Conversion"])

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
    value = st.number_input("Value (Degrees for sin/cos/tan, Ratio for inverse)", value = 0.0, key = "value")
    
    if st.button("Solve", key="btn_trig"):
        # 1. Standard Trig
        if trigfunc == "sine":
            result = math.sin(math.radians(value))
            st.success(f"Result: {round(result, 4)}")
            
        elif trigfunc == "cosine":
            result = math.cos(math.radians(value))
            st.success(f"Result: {round(result, 4)}")
            
        elif trigfunc == "tangent":
            result = math.tan(math.radians(value))
            st.success(f"Result: {round(result, 4)}")

        # 2. Inverse Trig (Outputting Degrees)
        elif trigfunc == "inverse sine":
            if -1 <= value <= 1:
                result_deg = math.degrees(math.asin(value))
                st.success(f"Result: {round(result_deg, 4)}°")
            else:
                st.error("Input for Inverse Sine must be between -1 and 1")

        elif trigfunc == "inverse cosine":
            if -1 <= value <= 1:
                result_deg = math.degrees(math.acos(value))
                st.success(f"Result: {round(result_deg, 4)}°")
            else:
                st.error("Input for Inverse Cosine must be between -1 and 1")

        elif trigfunc == "inverse tangent":
            result_deg = math.degrees(math.atan(value))
            st.success(f"Result: {round(result_deg, 4)}°")
       
        


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



elif mode == "Calculus":
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
        except Exception as e:
            st.error(f"Math Error: Could not parse '{user_input}'. Check your syntax!")




elif mode == "Statistics":
    st.header("Statistics Dashboard")
    st.write("Enter your data points separated by commas.")

    raw_data = st.text_area("Data Points:", value="0, 0")

    if raw_data:
        try:
            data_list = [float(x.strip()) for x in raw_data.split(",") if x.strip()]

            if st.button("Sort", key = "btn_stats"):
                if len(data_list) > 0:
                    mean_val = np.mean(data_list)
                    median_val = np.median(data_list)
                    std_val = np.std(data_list)
                    min_val = np.min(data_list)
                    max_val = np.max(data_list)
                
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Mean (Average)", f"{mean_val:.2f}")
                    col2.metric("Median", f"{median_val:.2f}")
                    col3.metric("Std. Deviation", f"{std_val:.2f}")

                    col4, col5, col6 = st.columns(3)
                    col4.metric("Minimum", f"{min_val}")
                    col5.metric("Maximum", f"{max_val}")
                    col6.metric("Total Count", len(data_list))

                    st.subheader("Data Distribution")
                    chart_data = pd.DataFrame(data_list, columns=['Value'])
                    st.bar_chart(chart_data['Value'].value_counts().sort_index())
                else:
                    st.warning("Please enter at least one number.")

        except ValueError:
                    st.error("Check your input! Make sure you only use numbers and commas.")
elif mode == "Unit Conversion":
    st.header("Unit Conversions")
    unit = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Data"])

    if unit == "Length":
        length_units = {
            "Meters": 1.0, "Kilometers": 1000.0, "Centimeters": 0.01,
            "Millimeters": 0.001, "Miles": 1609.34, "Yards": 0.9144,
            "Feet": 0.3048, "Inches": 0.0254
        }
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From:", list(length_units.keys()))
            input_value = st.number_input("Enter Value:", value=1.0, key="len_in")
        with col2:
            to_unit = st.selectbox("To:", list(length_units.keys()))
        
        if st.button("Convert", key="btn_len"):
            result = (input_value * length_units[from_unit]) / length_units[to_unit]
            st.success(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")

    elif unit == "Weight":
        weight_units = {
            "Kilograms": 1000.0, "Grams": 1.0, "Metric Ton": 1000000.0,
            "Dram": 1.772, "Ounce": 28.35, "Pound": 453.59,
            "Stone": 6350.29, "Troy Ounce": 31.10, "Tola": 11.66
        }
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From:", list(weight_units.keys()))
            input_value = st.number_input("Enter value", value=1.0, key="wt_in")
        with col2:
            to_unit = st.selectbox("To:", list(weight_units.keys())) 
        if st.button("Convert", key="btn_wt"):
            result = (input_value * weight_units[from_unit]) / weight_units[to_unit]
            st.success(f"### {input_value} {from_unit} = {result:.4f} {to_unit}")

    elif unit == "Temperature":
        temp_options = ["Celsius", "Fahrenheit", "Kelvin"]
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From:", temp_options)
            input_value = st.number_input("Enter value", value=0.0, key="temp_in")
        with col2:
            to_unit = st.selectbox("To:", temp_options)

        if st.button("Convert", key="btn_temp"):
            if from_unit == "Celsius":
                celsius = input_value
            elif from_unit == "Fahrenheit":
                celsius = (input_value - 32) * 5/9
            else: # Kelvin
                celsius = input_value - 273.15
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            else: # Kelvin
                result = celsius + 273.15
            
            st.success(f"### {input_value} {from_unit} = {result:.2f} {to_unit}")

    elif unit == "Data":
        data_units = {
            "Megabyte": 1.0,
            "Bit": 0.000000125,
            "Nibble": 0.0000005,
            "Byte": 0.000001,
            "Kilobyte": 0.001,
            "Gigabyte": 1000,
            "Terabyte": 1000000,
            "Petabyte": 1000000000,
            "Exabyte": 1000000000000,
            "Zettabyte":1000000000000,
            "Yottabyte": 1000000000000000000
        }
            
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From:", list(data_units.keys()))
            input_value = st.number_input("Enter value", value = 1.0, key="data_in")
        with col2:
            to_unit = st.selectbox("To:", list(data_units.keys()))
        if st.button("Convert", key="btn_data"):
            result = (input_value * data_units[from_unit]) / data_units[to_unit]
            st.success(f"### {input_value} {from_unit} = {result:.2f} {to_unit}")


