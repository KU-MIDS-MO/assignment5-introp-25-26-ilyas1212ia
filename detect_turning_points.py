import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    difference = []
    for i in range(len(signal) - 1):
        difference.append(signal[i+1] - signal[i])
    turning_point = []
    for i in range(len(difference) - 1):
        if difference[i] * difference[i+1] < 0:
            turning_point.append(i+1)
    turning_point = np.array(turning_point, dtype=int)
    plt.plot(signal, label="signal")
    for i in turning_point:
        plt.scatter(i, signal[i], color='red')
    plt.title("turnign points in singal")
    plt.xlabel("index")
    plt.ylabel("value")
    plt.savefig(filename)
    plt.show()
    return turning_point
