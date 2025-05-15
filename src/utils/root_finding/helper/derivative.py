"""src/utils/root_finding/helper/derivative.py"""


def derivative(lst):
    """Returns a list of derivative coefficients from a polynomial input."""

    f_prime = []
    degree = len(lst) - 1  # Highest power

    for i, coeff in enumerate(lst):
        power = degree - i
        if power == 0:
            continue  # Skip constant term (no derivative)
        coeff_prime = coeff * power
        f_prime.append(coeff_prime)

    return f_prime
