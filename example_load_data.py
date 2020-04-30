# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:00:13 2020

@author: Guido
"""

from functions_2p import load_trial_data
import numpy as np

# Use our loading function to load in data as a dictionary containing dataframes
dfof_dict, stim_dict = load_trial_data('V1')

# Get a list of subject names by getting the keys of the dictionary
subject_names = dfof_dict.keys()

# Loop over subjects, by using enumerate every iteration of the for loop you get a counter i 
# and the name of that list entry
for i, subject in enumerate(subject_names):
    
    # Get the dataframes containing the data for this subject from the dictionary
    dfof_df = dfof_dict[subject]
    stim_df = stim_dict[subject]
    
    # The number of trials is the first dimension of the dataframe
    n_trials = dfof_df.shape[0]
    
    # The neurons are in the second dimension
    n_neurons = dfof_df.shape[1]
    
    # Print this
    print('\nSubject %s has %d trials and %d neurons' % (subject, n_trials, n_neurons))
    
    # Print the median reaction time
    median_rt = stim_df['RT'].median()
    print('The median reaction time is %.2f seconds' % median_rt)
    
    # Print the mean dF/F response for high (100%) and low (0.5 - 12%)  contrast visual stimuli
    high_dfof = dfof_df.loc[stim_df['StimType'] == 11, :].mean()
    low_dfof = dfof_df.loc[((stim_df['StimType'] == 1)
                            & (stim_df['Visual'] > 0.5)
                            & (stim_df['Visual'] < 12)), :].mean()
    print('Mean dF/F response to 100%% contrast visual stimuli: %.2f dF/F' % np.mean(high_dfof))
    print('Mean dF/F response to low contrast visual stimuli: %.2f dF/F' % np.mean(low_dfof))
    
