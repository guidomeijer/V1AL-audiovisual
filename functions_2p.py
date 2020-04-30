# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:14:32 2020

@author: Guido
"""

from os.path import join
import pandas as pd  


def data_path():
    path = 'G:\\UvA\\Datasets\\Starecase_processed'
    return path


def use_subjects(area):
    if area == 'V1':
        subjects = ['M032', 'M038', 'M041', 'M042', 'M046', 'M048']
    elif area == 'AL':
        subjects = ['M038', 'M041', 'M042', 'M043', 'M048', 'P022']
    return subjects


def load_trial_data(area):
    path = data_path()
    subjects = use_subjects(area)  
    dfof_dict = dict()
    stim_dict = dict()
    for i, subject in enumerate(subjects):
        dfof_df = pd.read_csv(join(path, '%s_%s_trial_dfof.csv' % (subject, area)))
        dfof_dict[subject] = dfof_df
        stim_df = pd.read_csv(join(path, '%s_%s_trial_stim.csv' % (subject, area)))
        stim_dict[subject] = stim_df
    return dfof_dict, stim_dict