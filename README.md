
# 🔊 Advanced Offline Text-to-Speech with Voice Gender Selection (Python)

[![Stars](https://img.shields.io/github/stars/Prasad-Arugollu/-Advanced-Offline-Text-to-Speech-with-Voice-Gender-Selection-Python?style=social)](https://github.com/Prasad-Arugollu/-Advanced-Offline-Text-to-Speech-with-Voice-Gender-Selection-Python)

A Python-based offline Text-to-Speech converter using `pyttsx3`. Select male or female voices, adjust rate and volume, and convert text files into high-quality spoken audio in WAV format.

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How to Use](#-how-to-use)
- [Project Structure](#-project-structure)


## ✨ Features

- 🗣️ **Offline Text-to-Speech:** Converts text to speech without an internet connection.
- 👨‍🦰 **Voice Gender Selection:** Choose between male and female voices.
- ⚙️ **Adjustable Rate:** Customize the speech rate.
- 🔊 **Adjustable Volume:** Control the output volume.
- 💾 **WAV Output:** Saves the converted audio to a WAV file.
- 🔢 **Voice Selection by Index:** Option to select voices by their index.

## 🛠️ Tech Stack

- Python
- pyttsx3

## ⚙️ Installation

1.  Ensure you have Python installed on your system.
2.  Install the `pyttsx3` library using pip:

    ```bash
    pip install pyttsx3
    ```

## 💻 Usage

1.  Place the text you want to convert into `text.txt`.
2.  Run the `text_to_speech.py` script:

    ```bash
    python text_to_speech.py
    ```

3.  Follow the prompts to select a voice gender, speech rate, and volume. If you skip voice gender, you can input the voice index directly.
4.  The converted audio will be saved as `output.wav` in the same directory.

### Example

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is a test.")
engine.runAndWait()
```

## 📝 How to Use

This project can be used in various real-world scenarios, such as:

- **Accessibility:** Converting written content into spoken words for individuals with visual impairments.
- **Education:** Creating audio versions of textbooks and learning materials.
- **Automation:** Integrating text-to-speech functionality into automated systems and scripts for notifications or voice prompts.
- **Content Creation:** Generating voiceovers for videos or podcasts.

**Example Scenario:**

Imagine you have a large text file (`text.txt`) containing a document that you want to listen to while commuting. You can use this script to convert the text into an audio file (`output.wav`) and listen to it on your phone.

1.  **Prepare the text file:** Make sure your content is saved in `text.txt`.
2.  **Run the script:** Execute `python text_to_speech.py` in your terminal.
3.  **Follow the prompts:** Choose a voice gender (e.g., `male` or `female`), adjust the rate (default is 150), and set the volume (default is 1.0). You can also select a voice by index if you know the index number of your preferred voice.
4.  **Listen to the output:** Once the script finishes, you'll find `output.wav` in the same directory. You can then transfer this file to your mobile device or any media player and listen to the converted text.

## 📂 Project Structure

```
.
├── README.md
├── text.txt
└── text_to_speech.py
```

-   `README.md`: This file (project documentation).
-   `text.txt`: Input text file for conversion.
-   `text_to_speech.py`: Python script for text-to-speech conversion.



---

<p align="center">
    Developed by <a href="https://github.com/Prasad-Arugollu" target="_blank">Prasad Arugollu</a> - Find more awesome projects on my <a href="https://github.com/Prasad-Arugollu" target="_blank">GitHub</a>!
</p>

