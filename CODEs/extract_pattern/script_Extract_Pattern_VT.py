import numpy as np
from matplotlib import pyplot as plt
import argparse
import json
import click
import os, sys

import sca.find_length as find_length
import sca.extraction as extraction
import sca.preprocess as preprocess



## ARGUMENTS:
parser = argparse.ArgumentParser()
parser.add_argument("--parameters_file", "-p", help="Select the file with parameters", default="config.txt")
parser.add_argument("--step", "-s", help="Select the step for finding length", default=1) #1: approximate; 2: precise; 3: segment with Virtual Trigger (VT)
parser.add_argument("--center" , help="", default=0)
parser.add_argument("--span" , help="", default=5e-6)
parser.add_argument("--res" , help="", default=1e-9)
parser.add_argument("--shift" , help="", default=0)
parser.add_argument("--time_div" , help="Enter the time diversity order of the collected traces", default=None)
args = parser.parse_args()
## END ARGUMENTS



## PARAMETERS:
parameters_file = str(args.parameters_file)
try:	parameters = json.load(open(parameters_file, "r"))
except:	
    print(" Could not open parameters file: %s !"%parameters_file)
    sys.exit() 
data_directory     	= parameters["collection"]["data_directory"]
time_div    		= parameters["collection"]["time_div"] 		if args.time_div == None else int(args.time_div)

sampling_rate 		= parameters["collection"]["sampling_rate"]
target_freq   		= parameters["collection"]["target_freq"]
CP_length     		= parameters["collection"]["CP_length"]
pattern_name  		= parameters["collection"]["pattern_name"]
## END PARAMETERS


if not os.path.exists(data_directory):
    print("Directory: %s does not exist !"%data_directory )
    sys.exit()


rawTrace = np.load(data_directory+"PATTERNs/RawTrace_%d.npy"%target_freq)


if int(args.step) == 1:
    corr = find_length.find_approximate_length(rawTrace)
    plt.plot(corr)
    plt.show()


if int(args.step) == 2:
    range_offset, result = find_length.find_precise_length(rawTrace, approximate_length=CP_length, center=float(args.center), 
                           span=float(args.span), res=float(args.res), time_div=time_div, sampling_rate=sampling_rate)
    plt.plot(range_offset, result)
    plt.show()


if int(args.step) == 3:
    trace = extraction.extract_trace(rawTrace, signal_length=CP_length, extract_method="virtual_trigger", sampling_rate=sampling_rate, time_div=1000)
    plt.plot(trace)
    plt.show()


if int(args.step) == 4:
    trace = extraction.extract_trace(rawTrace, signal_length=CP_length, extract_method="virtual_trigger", sampling_rate=sampling_rate, time_div=1000)
    trace = preprocess.shift_trace(trace, int(args.shift))
    np.save(data_directory+"PATTERNs/"+pattern_name+".npy", trace)
    plt.plot(trace)
    plt.show()





























