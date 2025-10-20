import mpmath
mpmath.mp.dps = 10000000  # WARNING: need 100+ GB RAM
print(mpmath.mp.pi)