# Newton's Method Root Finder (Planning Document)

This document outlines the structure, logic, and design thinking behind building a reusable Newton's Method root-finding function in Python.

---

## 🧠 Purpose

Develop a general-purpose function that applies Newton’s Method to find a root of a **polynomial equation of any order**, given:
- An initial guess (`x0`)
- A list of coefficients in descending order (`[a_n, ..., a_1, a_0]`)

---

## 🔧 Function Inputs

| Parameter | Type    | Description |
|----------:|:--------|:------------|
| `x0`      | `float` | Initial guess for the root |
| `coeffs`  | `list`  | Polynomial coefficients from highest to lowest degree |

Optional parameters to add later:
- `tolerance` (`float`): Stopping threshold for convergence (e.g., `1e-6`)
- `max_iter` (`int`): Maximum number of iterations before giving up (e.g., 100)

---

## 🔩 Internal Logic Breakdown

### 1. **Evaluate the Polynomial**
You’ll need to evaluate the polynomial \( f(x) \) at a given `x` using the input `coeffs` list.

Example:  
Input `coeffs = [3, 0, -2, 1]`  
Represents:  
\( f(x) = 3x^3 + 0x^2 - 2x + 1 \)

Use a helper function to loop through the list and compute the result.

---

### 2. **Compute the Derivative**
To apply Newton’s Method, you need \( f'(x) \).  
Build a **new coefficient list** by applying the power rule.

For example:  
If `coeffs = [3, 0, -2, 1]` (for \( f(x) = 3x^3 + 0x^2 - 2x + 1 \))  
Then the derivative is \( f'(x) = 9x^2 - 2 \), which becomes:  
`[9, 0, -2]`

This is also evaluated using the same helper logic.

---

### 3. **Iterative Newton’s Method Loop**

Update rule:
```python
x_new = x_old - f(x_old) / f_prime(x_old)
