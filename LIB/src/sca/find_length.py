import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

import sca.preprocess as preprocess
import sca.compare_segments as compare_segments


def find_approximate_length(initial_measure): 
    length = len(initial_measure)
    initial_measure = preprocess.normalize_trace(initial_measure)
    half_measure = initial_measure[:int(length/2)]
    corr = signal.correlate(initial_measure, half_measure)[int(length/2) : -int(length/2)]
    return corr/int(length/2)



def find_precise_length(initial_measure, approximate_length, center, span, res, time_div, sampling_rate=5e6, method='distance'):
    range_offset = np.arange ( center-(span/2), center+(span/2), res )

    result = []
    if method=='distance':
        for offset in range_offset: result.append( compare_segments.dist_segments(initial_measure, approximate_length, offset, sampling_rate, time_div) )
        print(range_offset[np.argmin(result)])
    else:
        for offset in range_offset: result.append( compare_segments.corr_segments(initial_measure, approximate_length, offset, sampling_rate, time_div) )
        print(range_offset[np.argmax(result)])

    return range_offset, result
