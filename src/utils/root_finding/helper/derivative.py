"""src/utils/root_finding/helper/derivative.py"""

def derivative(lst):
    """Returns a list of coefficients based on the input function coefficients."""

    f_prime =[]
    order = len(lst) - 1

    for power in lst:
        coeff_prime = power * order
        order -= 1
        power -= 1
        f_prime.append(coeff_prime)
    return f_prime
