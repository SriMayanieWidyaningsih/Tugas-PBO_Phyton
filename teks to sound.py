from tkinter import Tk, Label, Entry, Button
from gtts import gTTS
from playsound import playsound

def convert_to_speech():
    text = entry_text.get()
    language = 'id'  # You can change the language code as needed

    # Create gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio file
    tts.save("output.mp3")

    # Play the saved audio file
    playsound("output.mp3")

# Create the main window
root = Tk()
root.title("Text-to-Speech Converter")

# Create widgets
label_instruction = Label(root, text="Enter text to convert:")
entry_text = Entry(root, width=50)
button_convert = Button(root, text="Convert to Speech", command=convert_to_speech)

# Place widgets on the window
label_instruction.pack(pady=10)
entry_text.pack(pady=10)
button_convert.pack(pady=10)

# Start the GUI event loop
root.mainloop()
