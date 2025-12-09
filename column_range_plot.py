import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    num_cols = A.shape[1]
    column_ranges = np.zeros(num_cols, dtype=float)
    
    for i in range(num_cols):
        col_max = A[:, i].max()
        col_min = A[:, i].min()
        column_ranges[i] = col_max - col_min
    plt.bar(range(num_cols), column_ranges)
    plt.xlabel("column index")
    plt.ylabel("range")
    plt.title("column ranges")
    
    plt.savefig(filename)
    plt.show()
    return column_ranges
