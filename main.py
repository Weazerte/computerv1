import sys
from reduced_form import reduceFunct, printReduced
import copy

# Δ=b2−4ac
# x1=−b−√Δ−−2a
#  et x2=−b+√Δ−−2a

def calculateDelta(a, b, c):
    return round((float(b) * float(b)) - (4 * float(a) * float(c)), 6)

    

def sqrt(x):
    return x**0.5


def calculate2(reducedf):
    a = float(reducedf[2])  # X^2 coefficient
    b = float(reducedf[1])  # X^1 coefficient
    c = float(reducedf[0])  # X^0 coefficient

    delta = calculateDelta(a, b, c)

    if delta > 0:
        x1 = round(((-1 * b) - sqrt(delta)) / (2 * a), 6)
        x2 = round(((-1 * b) + sqrt(delta)) / (2 * a), 6)
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = round((-b) / (2 * a), 6)
        print("Discriminant is zero, the solution is:")
        print(f"x = {x}")
    else:
        real_part = round((-b) / (2 * a), 6)
        imag_part = round(sqrt(abs(delta)) / (2 * a), 6)
        print("Discriminant is negative, the two complex solutions are:")
        print(f"{real_part} - {imag_part}i")
        print(f"{real_part} + {imag_part}i")



def main(argv):
    if len(argv) != 2:
        print("need 2 args")
        return 1
    reducedf = reduceFunct(argv[1])

    ret = printReduced(copy.copy(reducedf))

    if (ret > 0):
        print(f"Polynomial degree: {ret}")

    if ret <= 2:
        calculate2(reducedf)
    elif ret > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    


if __name__ == "__main__":
    main(sys.argv)
