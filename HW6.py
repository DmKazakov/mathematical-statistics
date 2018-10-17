import scipy.stats as st
import numpy as np
import plotly as py
import plotly.graph_objs as go

VARIANCE = 1
MAX_N_VALUE = 1000
MIN_N_VALUE = 10
REPETITIONS_NUMBER = 400
GAMMA = 0.9

PPF1_NORM = st.norm.ppf((3 + GAMMA) / 4)
PPF2_NORM = st.norm.ppf((3 - GAMMA) / 4)


def eval_a_len(sample_set, ppf1_chi2, ppf2_chi2):
    qsum = np.sum([x ** 2 for x in sample_set])
    return qsum * (1 / ppf2_chi2 - 1 / ppf1_chi2)


def eval_b_len(sample_set):
    nmean = sample_set.size * (np.mean(sample_set) ** 2)
    return nmean * (1 / PPF2_NORM ** 2 - 1 / PPF1_NORM ** 2)


a_mean_lens = []
b_mean_lens = []

for n in range(MIN_N_VALUE, MAX_N_VALUE, 10):
    ppf1_chi2 = st.chi2.ppf((1 + GAMMA) / 2, n)
    ppf2_chi2 = st.chi2.ppf((1 - GAMMA) / 2, n)

    a_lens = []
    b_lens = []
    for k in range(REPETITIONS_NUMBER):
        sample_set = np.random.normal(0, VARIANCE, n)
        a_lens.append(eval_a_len(sample_set, ppf1_chi2, ppf2_chi2))
        b_lens.append(eval_b_len(sample_set))

    a_mean_lens.append(np.mean(a_lens))
    b_mean_lens.append(np.mean(b_lens))

layout = dict(title='',
              xaxis=dict(title='Sample set size'),
              yaxis=dict(title='Segment length'),
              )

a_trace = go.Scatter(
    x=[n for n in range(MIN_N_VALUE, MAX_N_VALUE, 10)],
    y=a_mean_lens
)

py.offline.plot(dict(data=[a_trace], layout=layout), filename='a')

b_trace = go.Scatter(
    x=[n for n in range(MIN_N_VALUE, MAX_N_VALUE, 10)],
    y=b_mean_lens
)
py.offline.plot(dict(data=[b_trace], layout=layout), filename='b')
