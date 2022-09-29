

import os
import mne
import json
from mne.preprocessing import ICA

with open('config.json') as config_json:
    config = json.load(config_json)

data_file = config['fif']
raw = mne.io.read_raw_fif(data_file, verbose=False)

fname = config['fifi']
ica=mne.preprocessing.read_ica(fname, verbose=None)


ecg_indices, ecg_scores = ica.find_bads_ecg(inst=raw, ch_name=None, threshold=config['threshold'],
              start=None, stop=None, l_freq=config['l_freq'], h_freq=config['h_freq'],
              method=config['method'], reject_by_annotation=config['reject_by_annotation'],
              measure=config['measure'])

ica.exclude = ecg_indices
ica.save('out_dir/ica.fif',,overwrite=True)
