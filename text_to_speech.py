import pyttsx3, os

# voices I know about for gender guessing
voice_map = {
    "zira": "female",
    "hazel": "female",
    "eva": "female",
    "aria": "female",
    "david": "male",
    "mark": "male",
    "george": "male"
}

def list_voices(engine):
    vlist = engine.getProperty('voices')
    print("\n--- Available Voices ---")
    for i, v in enumerate(vlist):
        print(f"{i}: {v.name} ({v.languages}) - {v.id}")
    return vlist

def get_voice_by_gender(voices, gender):
    g = gender.lower()
    for i, v in enumerate(voices):
        name = v.name.lower()
        vid = v.id.lower()
        # check in my voice_map first
        for key, val in voice_map.items():
            if key in name or key in vid:
                if val == g:
                    return i
        # if not found, fall back to crude check
        if g in name or g in vid:
            return i
    return None

def tts_from_file(engine, infile, outfile, rate=150, vol=1.0, v_index=None):
    if not os.path.exists(infile):
        print(f"File '{infile}' not found.")
        return
    
    text = open(infile, "r", encoding="utf-8").read()
    if not text.strip():
        print("Text file is empty.")
        return

    engine.setProperty('rate', rate)
    engine.setProperty('volume', vol)

    voices = engine.getProperty('voices')
    if v_index is not None and 0 <= v_index < len(voices):
        engine.setProperty('voice', voices[v_index].id)
        print(f"Voice: {voices[v_index].name}")
    else:
        print("Using default voice.")

    engine.save_to_file(text, outfile)
    engine.runAndWait()
    print(f"Done! Saved as {outfile}")

if __name__ == "__main__":
    print("== Text 2 Speech ==")
    eng = pyttsx3.init()
    all_voices = list_voices(eng)

    g = input("\nMale or Female voice? (press enter to skip): ").strip().lower()
    voice_choice = None

    if g in ["male", "female"]:
        voice_choice = get_voice_by_gender(all_voices, g)
        if voice_choice is not None:
            print(f"Selected {g} voice: {all_voices[voice_choice].name}")
        else:
            print(f"No {g} voice found. Pick from the list instead.")
            try:
                voice_choice = int(input("Voice index? (enter for default): ") or -1)
            except:
                voice_choice = None
    else:
        try:
            voice_choice = int(input("Voice index? (enter for default): ") or -1)
        except:
            voice_choice = None

    r = int(input("Rate (default 150): ") or 150)
    v = float(input("Volume 0.0-1.0 (default 1.0): ") or 1.0)

    tts_from_file(eng, "text.txt", "output.wav", r, v,
        voice_choice if voice_choice is not None and voice_choice >= 0 else None)
    eng.stop()
    print("Exiting...") 