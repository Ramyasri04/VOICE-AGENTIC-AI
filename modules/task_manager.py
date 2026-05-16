import pandas as pd
import os

TASK_FILE = "data/tasks.csv"

def add_task(task):

    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame({
        "task": [task]
    })

    if os.path.exists(TASK_FILE):

        df.to_csv(
            TASK_FILE,
            mode='a',
            header=False,
            index=False
        )

    else:
        df.to_csv(TASK_FILE, index=False)

def get_tasks():

    if not os.path.exists(TASK_FILE):
        return []

    df = pd.read_csv(TASK_FILE)

    return df["task"].tolist()
