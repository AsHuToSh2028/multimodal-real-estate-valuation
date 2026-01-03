import os
import time
import requests
import pandas as pd
from tqdm import tqdm

# -----------------------------
# CONFIG
# -----------------------------
API_KEY = "AIzaSyBqFmkCiJzjJ3BaW9XxaDjIB2rBoH7zkRI"
OUT_DIR = "google_images"

ZOOM = 19
IMG_SIZE = "512x512"
MAPTYPE = "satellite"
RATE_LIMIT = 5


# -----------------------------
# Helper: Download 1 Image
# -----------------------------
def fetch_image(lat, lon, save_path):
    url = (
        "https://maps.googleapis.com/maps/api/staticmap?"
        f"center={lat},{lon}"
        f"&zoom={ZOOM}"
        f"&size={IMG_SIZE}"
        f"&maptype={MAPTYPE}"
        f"&key={API_KEY}"
    )

    try:
        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            return True
        else:
            print("HTTP", r.status_code, "=>", lat, lon)
            return False

    except Exception as e:
        print("ERROR fetching image:", e)
        return False


# -----------------------------
# Main Download Loop
# -----------------------------
def download_all(df):
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Total images to download:", len(df))

    for _, row in tqdm(df.iterrows(), total=len(df)):
        img_file = f"{int(row['id'])}.png"
        save_path = os.path.join(OUT_DIR, img_file)

        if os.path.exists(save_path):
            continue

        fetch_image(row["lat"], row["long"], save_path)
        time.sleep(1 / RATE_LIMIT)

    print("All downloads complete ✔")


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "train.csv")

    df = pd.read_csv(csv_path)
    df = df[['id', 'lat', 'long']]

    download_all(df)
