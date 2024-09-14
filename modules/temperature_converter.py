def c_to_f(c):
    """Convert celcius to fahreheit and return result"""
    f = (c * 1.8) + 32
    
    return f

def f_to_c(f):
    """Convert fahreheit to celcius and return result"""
    c = (f - 32) / 1.8

    return c