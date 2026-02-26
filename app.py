import streamlit as st

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
