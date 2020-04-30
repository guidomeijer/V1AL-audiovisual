# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:16:49 2020

@author: Guido
"""

from os.path import join, split
import pandas as pd
import numpy as np
from glob import glob
from scipy.io import loadmat

# Settings
TRIAL_METRIC = 'max'  # max, mean or median
WINDOW = 0.5  # s after trial onset to take

# Set paths
DATA_PATH = 'G:\\UvA\\Datasets\\Starecase'
SAVE_PATH = 'G:\\UvA\\Datasets\\Starecase_processed'

# Get all MAT files
files = glob(join(DATA_PATH, '*.mat'))

# Which data to pull out
variables = ['Response', 'TrialNumber', 'StimType', 'Visual', 'Orientation', 'Audio', 'Lick']

# Loop over files
for i, file in enumerate(files):
    print('Processing dataset %d of %d' % (i + 1, len(files)))
    
    # Load in dF/F data
    loaded_data = loadmat(file, squeeze_me=True)
    dfof = loaded_data['StareCase']['dFoF'].item()
    sampling_freq = loaded_data['StareCase']['SamplingFreq'].item()
    neuron_ids = loaded_data['StareCase']['NeuronID'].item()
    
    # Extract other variables and put into pandas dataframe
    stim_df = pd.DataFrame()
    for j, var in enumerate(variables):
        stim_df[var] = loaded_data['StareCase'][var].item()
        
    # Create dataframe with the fluorescence responses per trial for every neuron and another one
    # with the properties of that trial (visual contrast, hit/miss, etc)
    neuron_df = pd.DataFrame(columns=neuron_ids)
    trial_df = pd.DataFrame(columns=variables)
    trial_start = np.array([i for i, x in enumerate(np.diff(stim_df['TrialNumber']) > 0) if x]) + 1
    for j, im_frame in enumerate(trial_start):
        if TRIAL_METRIC == 'max':
            neuron_df.loc[j, neuron_ids] = np.max(
                            dfof[im_frame:im_frame + int(WINDOW * sampling_freq), :], axis=0)
        elif TRIAL_METRIC == 'mean':
            neuron_df.loc[j, neuron_ids] = np.mean(
                            dfof[im_frame:im_frame + int(WINDOW * sampling_freq), :], axis=0)
        elif TRIAL_METRIC == 'median':
            neuron_df.loc[j, neuron_ids] = np.median(
                            dfof[im_frame:im_frame + int(WINDOW * sampling_freq), :], axis=0)
        trial_df.loc[j, variables] = stim_df.loc[im_frame, :]
        lick = (stim_df.loc[im_frame : im_frame + int(sampling_freq), 'Lick'] == 1).values
        if sum(lick == True) > 0:
            trial_df.loc[j, 'RT'] = [i for i, x in enumerate(lick) if x][0] / sampling_freq
    trial_df = trial_df.drop('Lick', axis=1)
            
    # Convert to floats
    neuron_df = neuron_df.astype(float)
    trial_df = trial_df.astype(float)
    stim_df = stim_df.astype(float)
    
    # Put dF/F matrix into dataframe
    dfof_df = pd.DataFrame(data=dfof, columns=neuron_ids)
    dfof_df = dfof_df.astype(float)
    
    # Save as CSV
    neuron_df.to_csv(join(SAVE_PATH, split(file)[1][-11:-4] + '_trial_dfof.csv'), index=False)
    trial_df.to_csv(join(SAVE_PATH, split(file)[1][-11:-4] + '_trial_stim.csv'), index=False)
    dfof_df.to_csv(join(SAVE_PATH, split(file)[1][-11:-4] + '_trace_dfof.csv'), index=False)
    stim_df.to_csv(join(SAVE_PATH, split(file)[1][-11:-4] + '_trace_stim.csv'), index=False)
        
        
        
    
        