"""

"""


import numpy as np
from scipy.io.wavfile import write
import soundfile as sf



def example_numpy_to_wav():
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

    print(waveform_integers.shape())



def wav_to_numpy(file):
    wav = sf.read(file)
    array = wav[0]

    return array
