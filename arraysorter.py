import numpy

# Defines the amount of rows and columns
rows = 100      # <---- CHANGE THIS
columns = 100    # <---- CHANGE THIS

formula = "x + y * i"

def main():
    adone, a, newlist, tmp = [], [], [], []
    # Creates first row
    tmp = [formula.replace("y", str(round(i * 0.01, 2))) for i in range(0, rows + 1)]
    # Duplicates the row but fills in y correctly
    for i in range(0, columns + 1):
        a.append(tmp)
    adone = [[u.replace("x", str(round((p - 1) * 0.01, 2))) for p, u in enumerate(a[i], 1)] for i in range(0, columns + 1)]
    return adone

# Starts the program
if __name__ == '__main__':
    adone = main()
    data = numpy.array([adone])
    print(data)





