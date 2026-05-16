import pandas as pd
import os

NOTE_FILE = "data/notes.csv"

def save_note(note):

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame({
        "note": [note]
    })

    if os.path.exists(NOTE_FILE):

        df.to_csv(
            NOTE_FILE,
            mode='a',
            header=False,
            index=False
        )

    else:
        df.to_csv(NOTE_FILE, index=False)
