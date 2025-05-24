"""src/utils/root_finding/helper"""

# x^3 - x - 1
# 1, 0, -1, -2

def eval_func(coef, x):
    """Determines the powers of the function based on the numerical argument list"""
    func_eval_lst = []
    func_len = len(coef)
    for idx, num in enumerate(coef):
        power = func_len - 1 - idx  # This gives powers: 3,2,1,0 for a list of length 4
        func_eval_lst.append(num * x**power)
    results = sum(func_eval_lst)
    return results



