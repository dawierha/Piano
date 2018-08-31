import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
#from os import os

# presume file already converted to wav.
#file = os.path.join(temp_folder, file_name)

rate, aud_data = wav.read('./Resources/speech_example1.wav')

# wav file is mono.
print(aud_data[:])
channel_1 = aud_data[:]

fourier = np.fft.fft(channel_1)

plt.figure(1)
plt.plot(fourier)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()
