# Code from akey7's "numpy_array_to_wav_file.py" at
# https://gist.github.com/akey7/725b2b7b68482525fff6620cb8cf05d4

import numpy as np
from scipy.io.wavfile import write

# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 440.0

# Duration
duration_s = 5.0

# NumpPy magic
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

# Write the .wav file
write('first_sine_wave.wav', sps, waveform_integers)
