# V1AL-audiovisual
Response: Tx1 vector with hit or miss indication per trial (1 = hit, 0 = miss, -1 = ITI)
TrialNumber: Tx1 vector with trial numbers
StimType: Tx1 vector with stimulus types (0 = blank, 1 = visual, 2 = audio, 3 = audio-visual, 11 = full contrast visual, 22 = full amplitude audio, 33 = full audio-visual, -1 = ITI).
Visual: Tx1 vector with visual contrast in percentage
Audio: Tx1 vector with auditory amplitude in dB
Lick: Tx1 vector indicating when a lick was detected per imaging frame (0 = no lick detected, 1 = lick detected)
NeuronID: 1xN vector with neuron ID's (neurons were excluded if they were not present in all imaging sessions)
SamplingFreq: double indicating the sampling frequency of the two-photon scanner
