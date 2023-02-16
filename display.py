import pip
import os

try:
    import wfdb
except ModuleNotFoundError:
    pip.main(['install', "wfdb"])
    import wfdb

import numpy as np
import matplotlib.pyplot as plt 

def wfdb_display_from_path(file_path, leads, start_samp, end_samp):
    record = wfdb.rdrecord(file_path, sampfrom=start_samp, sampto=end_samp, channels= leads)
    figure_title = os.path.basename(file_path)
    wfdb.plot_wfdb(record=record, title=figure_title)
    

def np_display(samples):
    plt.plot(samples)

def np_mark_peaks(plt, samples, peaks, title):
    plt.plot(samples)
    for peak in peaks:
        plt.axvline(x = peak, color = 'r')
    plt.title.set_text(title)

def compare_plot(signal1, signal2):
    plt.plot(signal1)
    plt.plot(signal2, color = 'r')
    plt.show()
