def sum_abs_digits(num):
    digits_str = str(abs(num))
    total = sum(int(d) for d in digits_str)
    
    return total
