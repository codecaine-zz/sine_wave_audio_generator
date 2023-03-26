import numpy as np
import simpleaudio as sa

# Define the sampling frequency and duration of the notes
sampling_freq = 44100
duration = 0.5

# Define the frequency of the notes (in Hz)
notes_freq = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}


# Define a function to generate a sine wave at a given frequency and duration
def generate_sine_wave(frequency, duration):
    num_samples = int(duration * sampling_freq)
    time_array = np.arange(num_samples) / sampling_freq
    samples = np.sin(2 * np.pi * frequency * time_array)
    return samples


# Define the notes to be played in the melody
notes = ['C4', 'E4', 'G4', 'C5']

# Generate the sine wave for each note and combine them into a single audio signal
audio_signal = np.array([])
for note in notes:
    frequency = notes_freq[note]
    note_wave = generate_sine_wave(frequency, duration)
    audio_signal = np.concatenate((audio_signal, note_wave))

# Convert the audio signal to a format that can be played by the sound card
audio_signal = audio_signal * (2 ** 15 - 1) / np.max(np.abs(audio_signal))
audio_signal = audio_signal.astype(np.int16)

# Play the audio signal using the simpleaudio library
play_obj = sa.play_buffer(audio_signal, 1, 2, sampling_freq)

# Wait for the sound to finish playing
play_obj.wait_done()
