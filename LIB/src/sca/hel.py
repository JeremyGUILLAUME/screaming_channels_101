# FROM:
# Giovanni Camurati
# camurati@eurecom.fr

import os
import ctypes
import numpy as np


#lib = ctypes.CDLL("/home/user/Documents/SCA/LIB/src/sca/libhel.so")
lib = ctypes.CDLL(os.path.dirname(__file__) + "/libhel.so")


def bruteforce(scores, pt1, pt2, ct1, ct2, merge, bins, bit_bound_start,
        bit_bound_end):

    # conversion to be sure about types
    scores = np.array(scores).flatten()
    scores = np.nan_to_num(scores)
    scores_p = ctypes.c_void_p(scores.ctypes.data)
    
    pt1 = np.array(pt1, dtype=ctypes.c_ubyte)
    pt2 = np.array(pt2, dtype=ctypes.c_ubyte)
    ct1 = np.array(ct1, dtype=ctypes.c_ubyte)
    ct2 = np.array(ct2, dtype=ctypes.c_ubyte)
 
    merge_value = np.zeros((1), dtype=ctypes.c_int)
    merge_value = merge
    nb_bins = np.zeros((1), dtype=ctypes.c_int)
    nb_bins = bins
    start = np.zeros((1), dtype=ctypes.c_int)
    start = bit_bound_start
    end = np.zeros((1), dtype=ctypes.c_int)
    end = bit_bound_end

    found = np.zeros((1), dtype=ctypes.c_int)

    # call to the library function
    lib.bruteforce(scores_p, pt1.ctypes, pt2.ctypes, ct1.ctypes,
            ct2.ctypes, found.ctypes, merge_value,
            nb_bins, start, end)

    return found

def rank(scores, knownkey, merge, bins):

    # conversion to be sure about types
    scores = np.array(scores).flatten()
    scores = np.nan_to_num(scores)
    scores_p = ctypes.c_void_p(scores.ctypes.data)
    
    knownkey = np.array(knownkey, dtype=ctypes.c_ubyte)
    merge_value = np.zeros((1), dtype=ctypes.c_int)
    merge_value = merge
    nb_bins = np.zeros((1), dtype=ctypes.c_int)
    nb_bins = bins

    rank_min = np.zeros((1), dtype=ctypes.c_double)
    rank_rounded = np.zeros((1), dtype=ctypes.c_double)
    rank_max = np.zeros((1), dtype=ctypes.c_double)
    time_rank = np.zeros((1), dtype=ctypes.c_double)

    # call to the library function
    lib.rank(scores_p, knownkey.ctypes, merge_value,
            nb_bins, rank_min.ctypes, rank_rounded.ctypes, rank_max.ctypes,
            time_rank.ctypes)

    return rank_min, rank_rounded, rank_max, time_rank

def example():
    # example mainly taken from ../hel_lib/main_example.cpp
    from example_data import scores, pt1, pt2, ct1, ct2
   
    merge = 2
    bins = 512
    bit_bound_start = 0

    for bit_bound_end in [10, 30]:
        print("")
        print("TRYING BRUTEFORCE UP TO RANK 2**%d"%bit_bound_end)
        found = bruteforce(scores, pt1, pt2, ct1, ct2, merge,
                bins, bit_bound_start, bit_bound_end)

        if found:
            print("KEY FOUND!")
        else:
            print("KEY NOT FOUND...")
            print("Let's try with a higher rank")

if __name__ == "__main__":
    example()
    
