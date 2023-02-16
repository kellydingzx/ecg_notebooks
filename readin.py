import pip

try:
    import wfdb
except ModuleNotFoundError:
    pip.main(['install', "wfdb"])
    import wfdb

import numpy as np

def get_data(datapath, leads, start_samp, end_samp):
    signal, rest = wfdb.rdsamp(datapath, sampfrom=start_samp, sampto=end_samp, 
                                channel_names = leads)
    annots = wfdb.rdann(datapath, 'atr', sampfrom=start_samp, sampto=end_samp)
    return signal, annots.sample 

