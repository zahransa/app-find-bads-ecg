

import os
import mne
import json
from mne.preprocessing import ICA

import matplotlib.pyplot as plt

#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



with open('config.json') as config_json:
    config = json.load(config_json)

data_file = config['fif']
raw = mne.io.read_raw_fif(data_file, verbose=False)

fname = config['ica']
ica=mne.preprocessing.read_ica(fname, verbose=None)


ecg_indices, ecg_scores = ica.find_bads_ecg(inst=raw, ch_name=None, threshold=config['threshold'],
              start=None, stop=None, l_freq=config['l_freq'], h_freq=config['h_freq'],
              method=config['method'], reject_by_annotation=config['reject_by_annotation'],
              measure=config['measure'])

ica.exclude = ecg_indices
ica.save('out_dir/ica.fif',overwrite=True)


plt.figure(1)
ica.plot_components()
plt.savefig(os.path.join('out_figs','ica.png'))

# build product.json dictionary for brainlife message
product = {}
product['brainlife'] = []
product['brainlife'].append({'type': 'info', "msg": "here are the excluded nodes: "+', '.join([ str(f) for f in ecg_indices ])})

# save product.json
with open('product.json','w') as prod_f:
    json.dump(product,prod_f)
