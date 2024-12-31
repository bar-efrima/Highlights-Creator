# **Highlights-Creator**

This project features a Python program that extracts key moments from sports game videos, specifically soccer, by analyzing audio cues and recognizing keywords. The program identifies timestamps of significant moments and generates GIFs to visually represent these highlights.

---

## **Project Overview**

The goal of this project is to extract 'important' frames from a soccer game video using audio analysis. Key assumptions are based on crowd noise and commentary volume spikes during pivotal moments like goals or remarkable plays. These moments are captured and processed to enhance the viewing experience for soccer fans.

---

## **Features**

### **1. Audio Analysis for Volume Peaks**
- Extracts audio from the video file.
- Identifies areas of significant volume spikes, representing exciting moments in the game.
- Volume peaks are analyzed by detecting quick rises and falls in volume.

### **2. Speech Recognition and Keyword Detection**
- Converts the audio to text using speech recognition.
- Searches for predefined exciting keywords such as "wow," "unbelievable," and "stunning."
- Reads the keywords from a text file for easy customization.

### **3. Timestamps of Important Moments**
- Combines volume peak analysis and keyword detection to generate a list of timestamps for significant moments.
- Prints these timestamps to the console, each on a new line.

### **4. GIF Creation for Key Moments**
- Uses the `imageio` library to extract frames corresponding to important moments.
- Creates a single animated GIF showcasing these moments for easy sharing and viewing.

---

## **How It Works**

1. **Input Video File**
   - Place the soccer game video file (`soccer_game.mp4`) in the project folder's root.

2. **Audio Extraction**
   - The program extracts audio from the video file as the first step in processing.

3. **Volume Peaks Analysis**
   - Identifies significant increases in audio volume as potential key moments.
   - Numeric constants for volume peak detection can be adjusted for better results.

4. **Speech-to-Text Conversion**
   - Converts the extracted audio to text for debugging and keyword detection.
   - Prints the full transcription to the console.

5. **Keyword Matching**
   - Searches the transcription for exciting words stored in a text file.
   - Matches are timestamped and added to the list of important moments.

6. **GIF Generation**
   - Extracts frames from the video at key timestamps.
   - Combines frames into a single animated GIF representing the highlights.

---

## **Dependencies**

- Python 3.8+
- Required Libraries:
  - `moviepy` (for video and audio processing)
  - `speech_recognition` (for speech-to-text conversion)
  - `imageio` (for GIF creation)

Install dependencies with:
```bash
pip install moviepy speechrecognition imageio
```

---

## **Running the Program**

1. Ensure the video file (`soccer_game.mp4`) is in the root of the project directory.
2. Run the program:
   ```bash
   python soccer.py
   ```
3. View the printed timestamps of significant moments in the console.
4. The program generates an animated GIF (`highlights.gif`) in the project directory, showcasing the key moments.

---

## **Customization**

- **Adjusting Volume Analysis**: Fine-tune the numeric constants in the code to better detect peaks based on your video’s audio characteristics.
- **Keyword List**: Modify the keywords by editing the text file containing exciting words.

---

## **Future Enhancements**

- Add support for multiple sports by customizing volume and keyword detection parameters.
- Incorporate machine learning to improve detection accuracy.
- Include a graphical user interface (GUI) for ease of use.
- Enable real-time processing for live games.

---

This program offers a streamlined way to identify and visualize exciting moments in soccer games, enhancing the experience for sports enthusiasts. Enjoy creating and sharing your game highlights!
