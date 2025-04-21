import sys
from reduced_form import reduceFunct, printReduced


def calculate1():


def calculate2():


def main(argv):
    if len(argv) != 2:
        print("need 2 args")
        return 1
    reducedf = reduceFunct(argv[1])
    ret = printReduced(reducedf)
    if (ret > 0):
        print(f"Polynomial degree: {ret}")

    if ret == 1:
        calculate1(reducedf)
    elif ret == 2:
        calculate2(reducedf)
    elif ret > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    


if __name__ == "__main__":
    main(sys.argv)
