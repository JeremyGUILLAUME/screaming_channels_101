import numpy as np
import argparse
import json
import os, sys
import time

import uhd
import sca.USRP as usrp
import sca.PCA10040 as pca10040
import sca.data as data


## ARGUMENTS:
parser = argparse.ArgumentParser()
parser.add_argument("--parameters_file", "-p", help="Select the file with parameters", default="config.txt")
args = parser.parse_args()
## END ARGUMENTS


## PARAMETERS:
parameters_file = str(args.parameters_file)
try:	parameters = json.load(open(parameters_file, "r"))
except:	
    print(" Could not open parameters file: %s !"%parameters_file) 
    sys.exit()
data_directory     	= parameters["collection"]["data_directory"]

USRP_address  		= parameters["collection"]["USRP_address"]
sampling_rate 		= parameters["collection"]["sampling_rate"]
target_freq   		= parameters["collection"]["target_freq"]
implementation		= parameters["collection"]["implementation"]
## END PARAMETERS


if not os.path.exists(data_directory): 
    print("Directory: %s does not exist !"%data_directory )
    sys.exit()

#Configure setup: SDR and Board
drop_start=50e-3 #Time for the SDR to start the collection properly
collection_time = 1 #1 second
num_samps = int( (drop_start + collection_time) * sampling_rate)

if USRP_address != "": 	usrp_ = uhd.usrp.MultiUSRP("addr="+USRP_address)
else: 			usrp_ = uhd.usrp.MultiUSRP()
SDR     = usrp.usrp_init(usrp_, target_freq, sampling_rate)
BOARD 	= pca10040.init_PCA10040(time_div = 1000000, power=0, plot_=True)


if not os.path.exists(data_directory+"PATTERNs/"): os.makedirs(data_directory+"PATTERNs/")


plaintexts, key = data.create_static_data(1)
pca10040.send_PCA10040_param(BOARD, 'K', key)
pca10040.send_PCA10040_param(BOARD, 'P', plaintexts[0])

while True:
    usrp.usrp_start(SDR)
    time.sleep(drop_start)
    BOARD.write(str(implementation).encode())
    time.sleep(collection_time)
    usrp.usrp_stop(SDR)

    rawTrace = usrp.usrp_get_data(SDR, num_samps, int(drop_start * sampling_rate) )
    break

np.save(data_directory+"PATTERNs/RawTrace_%d.npy"%target_freq, rawTrace)

pca10040.close_PCA10040(BOARD)













