def Euclidean(x, y):
    """
    Assumes x < y 
    Returns gcd(x, y). For example gcd(5, 15) = 3, gcd(105, 224) = 7
    """
    if x > y:
        tmp = x 
        x = y 
        y = tmp 

    if x % y == 0:
        return y

    else:
        return Euclidean(y % x, x)

print(Euclidean(105, 224))