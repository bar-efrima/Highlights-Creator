# getting the volume peaks
import wave, json, os, librosa,imageio
from vosk import Model, KaldiRecognizer
import Word as custom_Word
from moviepy.editor import VideoFileClip
import pydub, cv2


# Define the input and output filenames
video_file = "soccer_game-short.mp4"
audio_file = "soccer_game-short.wav"
gif_file = "important_frames.gif"
gif_file_captions = "important_frames_captions.gif"  # directory to save frames with captions
""" Extract the audio from the video file"""

clip = VideoFileClip(video_file)
clip.audio.write_audiofile(audio_file)

""" Go over the audio and find areas of ‘peaks’ of volume and
and add the timestamp of each such ‘peak’ to the list of ‘important’ game moments"""

# Load the audio file
y, sr = librosa.load(audio_file)

# Calculate the RMS amplitude of the audio signal
rms = librosa.feature.rms(y=y)

# Find the time intervals where the RMS amplitude is above the threshold
threshold = 0.02
peaks = librosa.util.peak_pick(rms[0], pre_max=5, post_max=5, pre_avg=5, post_avg=5, wait=5, delta=threshold)

# Convert the peak indices to time intervals
times = librosa.frames_to_time(peaks, sr=sr)

# Create a list to store the important game moments
important_moments = []

# Append each peak timestamp to the list of important game moments
for t in times:
    important_moments.append(t)

# Print the important game moments - for debug only
# print(f"Important game moments in {os.path.basename(video_file)}:")
# for t in important_moments:
#     print(f" - {t:.2f} seconds")

"""Convert the audio to text using speech recognition"""

model_path = "vosk-model-en-us-0.22-lgraph"
audio_filename = "soccer_game-short.wav"

# Load the Vosk model
model = Model(model_path)

# Open the audio file and convert it to mono if needed
wf = wave.open(audio_filename, "rb")
if wf.getnchannels() == 1:
    audio_mono = wf.readframes(wf.getnframes())
else:
    audio_segment = pydub.AudioSegment.from_file(audio_filename)
    audio_mono = audio_segment.set_channels(1).raw_data

# Initialize the Kaldi recognizer
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# Recognize speech using the Vosk model
results = []
while True:
    data = audio_mono[:4800]
    audio_mono = audio_mono[4800:]
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)
part_result = json.loads(rec.FinalResult())
results.append(part_result)

"""Print the whole text of the video to console - for debug only"""

# Convert the list of JSON dictionaries to a list of custom Word objects
list_of_Words = []
for sentence in results:
    if len(sentence['result']) == 0:
        # Skip empty results
        continue
    for obj in sentence['result']:
        w = custom_Word.Word(obj)
        list_of_Words.append(w)

# Output the results to the screen - for debug
# for word in list_of_Words:
#     print(word.to_string())

#Close the audio file
wf.close()

"""Go over the text and search for exciting words from exiting_words.txt"""

# Define a function to convert frame index to time in seconds
def frame_to_time(frame_idx, sr):
    return frame_idx / sr

# Read the exciting words from exiting_words.txt
exciting_words = []
with open('exciting_words.txt', 'r') as f:
    exciting_words = f.read().splitlines()

# Loop through the list of Words and search for exciting words
for word in list_of_Words:
    if word.word.lower() in exciting_words:
        important_moments.append(word.start)
        # printing for debug only
        # print(
        #     f"Exciting word found: {word.word} (confidence: {word.conf * 100:.2f}%,timestamp:{word.start:.2f} seconds)")

"""Bonus: save all ‘important’ frames into a single animated gif(using imageio)"""

# Print the updated list of important game moments
print(f"Important game moments in {os.path.basename(video_file)} using volume peaks and speech recognition:")
for t in important_moments:
    print(f" - {t:.2f} seconds")

# Create a list to store the frames of the important moments
frames = []
for t in important_moments:
    # Extract the frame at the specified time
    frame = clip.get_frame(t)
    # Add the frame to the list
    frames.append(frame)

# Save the frames as an animated GIF
imageio.mimsave(gif_file, frames, duration=0.5)

# Print a message to indicate the GIF has been saved
print(f"Animated GIF saved to {os.path.abspath(gif_file)}")

"""Bonus 2: An option to include captions or subtitles in the animated GIF. 
This could be useful if the user wants to know in what moment the highlight happend"""

# Define a function to add a caption to a frame
def add_caption_to_frame(frame, caption):
    # Define font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (255, 255, 255)  # white
    thickness = 3

    # Add the caption to the frame
    cv2.putText(frame, caption, (10, 50), font, font_scale, font_color, thickness, cv2.LINE_AA)

    return frame

# Create a list to store the frames of the important moments with captions
captioned_frames = []

# Loop through the list of important game moments
for t in important_moments:
    # Extract the frame at the specified time
    frame = clip.get_frame(t)

    # Add a caption to the frame
    caption = f"Important moment at {t:.2f} seconds"
    frame_with_caption = add_caption_to_frame(frame, caption)

    # Add the frame to the list
    captioned_frames.append(frame_with_caption)

# Save the captioned frames as an animated GIF
imageio.mimsave(gif_file_captions, captioned_frames, duration=0.5)

# Print a message to indicate the GIF has been saved
print(f"Animated GIF with captions saved to {os.path.abspath(gif_file_captions)}")
