import numpy as np


def inv_fun(param):
    param = max(0, param)
    alpha = np.random.uniform()
    if alpha < (np.exp(-param)) / (2 * (param + np.exp(-param))):
        return np.log(2 * alpha * (param + np.exp(-param)))
    elif alpha <= (2 * param + np.exp(-param)) / (2 * (param + np.exp(-param))):
        return 2 * alpha * (param + np.exp(-param)) - np.exp(-param) - param
    else:
        return -np.log(2 * param + 2 * np.exp(-param) - 2 * alpha * (param + np.exp(-param)))


def decomposition(param):
    param = max(0, param)
    t = np.random.uniform()
    if t < (np.exp(-param)) / (2 * (param + np.exp(-param))):
        return -param - 1 / (2 * (param + np.exp(-param))) * (-np.log(np.random.uniform()))
    elif t <= (2 * param + np.exp(-param)) / (2 * (param + np.exp(-param))):
        return 2 * param * np.random.uniform() - param
    else:
        return param + 1 / (2 * (param + np.exp(-param))) * (-np.log(np.random.uniform()))
