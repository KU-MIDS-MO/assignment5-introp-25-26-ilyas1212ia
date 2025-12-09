def approx_real_root(coeffs, interval):

    c0 = coeffs[0]
    c1 = coeffs[1]
    c2 = coeffs[2]
    c3 = coeffs[3]
    def poly(x):
        return c0 + c1*x + c2*(x**2) + c3*(x**3)
    a = interval[0]
    b = interval[1]
    
    fa = poly(a)
    fb = poly(b)
    
    while (b - a) > 1e-9:
        mid = (a + b) / 2.0
        fm = poly(mid)
        
        if fa * fm <= 0:
            b = mid
            fb = fm
        else:
            a = mid
            fa = fm
    return (a + b) / 2.0
        