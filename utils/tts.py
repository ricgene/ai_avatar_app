import pyttsx3

def text_to_speech(text, save_path=None):
    engine = pyttsx3.init()
    engine.say(text)
    
    if save_path:
        engine.save_to_file(text, save_path)
    
    engine.runAndWait()
