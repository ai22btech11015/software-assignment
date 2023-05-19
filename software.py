import os
import random
import pygame

def play_audio_files(directory):
    # Get a list of all audio files in the directory
    audio_files = [f for f in os.listdir(directory) if f.endswith('.mp3') or f.endswith('.wav')]
    
    # Randomize the order of the audio files
    random.shuffle(audio_files)
    
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Iterate over the audio files and play them
    for file in audio_files:
        # Construct the full path to the audio file
        file_path = os.path.join(directory, file)
        
        # Load the audio file
        pygame.mixer.music.load(file_path)
        
        # Play the audio file
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            continue
    
    # Quit the pygame mixer
    pygame.mixer.quit()

# Specify the directory where the audio files are located
audio_directory = 'playlist'

# Call the function to play the audio files
play_audio_files(audio_directory)
