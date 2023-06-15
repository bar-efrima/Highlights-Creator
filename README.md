 # Highlights-Creator
I created a Python program that extracts important moments from a sports game video using audio and keywords. 
It analyzes volume peaks, recognizes exciting words through speech recognition, and prints timestamps. 
Additionally, it generates GIFs of those moments.

# Project Description:

In this project, I developed a program to extract 'important' frames from a soccer game video using only the audio. 
The main idea behind this approach is that during significant moments in a soccer game, such as goals or remarkable plays, the crowd and 
commentators generate a lot of noise, resulting in a quick increase and subsequent return to 'normal' volume levels.

To begin, I implemented a program called "soccer.py" that operates on a given video file, assuming the filename is "soccer_game.mp4" and 
it is placed in the root of the project folder. The first step is to extract the audio from the video file.

Next, the program analyzes the audio by identifying areas of 'peaks' in volume. These peaks correspond to moments when the volume significantly rises 
and subsequently decreases. The definition of a 'peak' and the numeric constants used for this analysis can be adjusted within the program. 
It might require multiple iterations and discussions with the program to fine-tune these parameters effectively.

After extracting the 'peak' timestamps, the program utilizes speech recognition to convert the audio to text. 
The entire text transcription of the video is printed to the console for debugging purposes. 
Then, the program searches for specific exciting words such as 'wow,' 'unbelievable,' and 'stunning.' To facilitate this,
I asked the program to compile a list of such words, which I stored in a text file and utilized in the code.

The program identifies the timestamps of each exciting word within the audio file and adds them to the list of 'important' game moments.
Finally, the program prints the timestamps of these 'important' game moments to the console, with each timestamp on a separate line.

In additon, I added a feature which saves all the 'important' frames as a single animated gif, using the imageio library. 
This feature provides a visual representation of the key moments in the soccer game.

Overall, my program successfully extracts the 'important' frames from a soccer game video using audio analysis and speech recognition. 
The combination of volume peaks and exciting word detection allows for a comprehensive identification of significant moments in the game,
enhancing the viewing experience for soccer enthusiasts.
