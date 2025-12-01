import numpy as np

def fit_linear(x_values, y_values):
    """
    Fits a straight line: y = mx + c
    """
    x = np.array(x_values)
    y = np.array(y_values)

    slope, intercept = np.polyfit(x, y, 1)

    equation_text = f"y = {slope:.2f}x + {intercept:.2f}"

    return {
        "slope": slope,
        "intercept": intercept,
        "equation": equation_text
    }

def fit_polynomial(x_values, y_values, degree):
    """
    Fits a polynomial of a specific degree.
    """
    x = np.array(x_values)
    y = np.array(y_values)

    # Calculate coefficients
    coefficients = np.polyfit(x, y, degree)

    # Build the equation string
    equation_parts = []
    for i, coeff in enumerate(coefficients):
        power = degree - i
        if power > 1:
            term = f"{coeff:.2f}x^{power}"
        elif power == 1:
            term = f"{coeff:.2f}x"
        else:
            term = f"{coeff:.2f}"
        equation_parts.append(term)
    
    equation_text = " + ".join(equation_parts)
    equation_text = equation_text.replace("+ -", "- ") # Clean up signs

    return {
        "coefficients": coefficients.tolist(), 
        "equation": f"y = {equation_text}"
    }

# --- TEST AREA ---
if __name__ == "__main__":
    # Test Data: A perfect parabola y = x^2
    test_x = [1, 2, 3, 4, 5]
    test_y = [1, 4, 9, 16, 25] 

    print("--- Testing Linear (Will be bad) ---")
    print(fit_linear(test_x, test_y))
    
    print("\n--- Testing Polynomial Degree 2 (Should be perfect) ---")
    print(fit_polynomial(test_x, test_y, 2))