def main():
    # Title
    st.title("Basic Web Calculator")

    # Input fields
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Operation selection
    operation = st.selectbox(
        "Choose operation",
        ["Add", "Subtract", "Multiply", "Divide", "Sin()", "Log()", "Ln()"]
    )

    # Calculate
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Sin()":
            result = sine(num1)
        elif operation == "Log()":
            result = log10_value(num1)
        elif operation == "Ln()":
            result = natural_log(num1)
        else:
            result = "Invalid operation"

        st.subheader(f"Result: {result}")


if __name__ == "__main__":
    main()
