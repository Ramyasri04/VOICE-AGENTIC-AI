import pandas as pd
from datetime import datetime
import os

FILE_PATH = "data/conversations.csv"

def save_conversation(user_text, ai_response, intent):

    os.makedirs("data", exist_ok=True)

    data = {
        "timestamp": [datetime.now()],
        "user_text": [user_text],
        "ai_response": [ai_response],
        "intent": [intent]
    }

    df = pd.DataFrame(data)

    if os.path.exists(FILE_PATH):

        df.to_csv(
            FILE_PATH,
            mode='a',
            header=False,
            index=False
        )

    else:
        df.to_csv(FILE_PATH, index=False)
