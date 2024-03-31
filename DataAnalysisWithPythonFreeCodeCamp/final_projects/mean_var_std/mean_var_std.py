import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    np_array = np.array(list).reshape(3,3)

    mean_ax0 = np_array.mean(axis=0)
    mean_ax1 = np_array.mean(axis=1)
    mean = np_array.mean()

    variance_ax0 = np_array.var(axis=0)
    variance_ax1 = np_array.var(axis=1)
    variance = np_array.var()

    standard_deviation_ax0 = np_array.std(axis=0)
    standard_deviation_ax1 = np_array.std(axis=1)
    standard_deviation = np_array.std()

    max_ax0 = np_array.max(axis=0)
    max_ax1 = np_array.max(axis=1)
    max_ = np_array.max()

    min_ax0 = np_array.min(axis=0)
    min_ax1 = np_array.min(axis=1)
    min_ = np_array.min()

    sum_ax0 = np_array.sum(axis=0)
    sum_ax1 = np_array.sum(axis=1)
    sum_ = np_array.sum()



    calculations = {
        'mean': [mean_ax0.tolist(), mean_ax1.tolist(), mean.tolist()],
        'variance': [variance_ax0.tolist(), variance_ax1.tolist(), variance.tolist()],
        'standard deviation': [standard_deviation_ax0.tolist(),standard_deviation_ax1.tolist(), standard_deviation.tolist()],
        'max': [max_ax0.tolist(), max_ax1.tolist(), max_.tolist()],
        'min': [min_ax0.tolist(), min_ax1.tolist(), min_.tolist()],
        'sum': [sum_ax0.tolist(), sum_ax1.tolist(), sum_.tolist()]
    }
    

    return calculations
