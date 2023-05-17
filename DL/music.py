import numpy as np
from scipy.io import wavfile

import numpy as np

def get_piano_notes():   
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 440 #Frequency of Note A4
    keys = np.array([x+str(y) for y in range(0,9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end+1]
    
    note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0 # stop
    return note_freqs

note_freqs = get_piano_notes()

def get_music_notes(notes, duration, sample_rate=44100, amplitude=4096):
    music_out = np.array([])
    for note in notes:
        frequency = note_freqs[note]
        t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
        wave = amplitude*np.sin(2*np.pi*frequency*t)
        music_out = np.concatenate([music_out, wave])
    return music_out

notes = ['C4','D4','E4','F4','G4','A4','B4','C5']

sine_wave = get_music_notes(notes, duration=.5, amplitude=3048 )
wavfile.write('liveNotes.wav', rate=44100, data=sine_wave.astype(np.int16)) 
