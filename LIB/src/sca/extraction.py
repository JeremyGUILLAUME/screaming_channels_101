import numpy as np

import sca.extract_methods as extract_methods
import sca.preprocess as preprocess


def extract_trace(data, signal_length, extract_method, sampling_rate=5e6, time_div=500, pattern=None, 
                  corr_min=0.6, bandpass_lower=1.85e6, bandpass_upper=1.95e6, lowpass_freq=5e3):

    if extract_method == "virtual_trigger":
        starts, traces = extract_methods.virtual_trigger(data, signal_length, sampling_rate, time_div)

    elif extract_method == "pattern_recognition":
        starts, traces = extract_methods.pattern_recognition(data, pattern, signal_length, sampling_rate, corr_min, time_div)

    elif extract_method == "freqComp_trigger":
        starts, traces = extract_methods.freqComp_trigger(data, signal_length, sampling_rate, corr_min, time_div, bandpass_lower, bandpass_upper, lowpass_freq, pattern)

    else:
        print("Wrong extration method name")
        return -1

    trace = np.average(traces, axis=0)
    trace = preprocess.normalize_trace(trace)

    return trace
