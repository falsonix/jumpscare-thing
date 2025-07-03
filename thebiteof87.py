import sys
import os
import shutil
import subprocess
import tempfile
import random
import time
import threading
import json

DEFAULT_CONFIG = {
    "chance_per_second": 0.0001,
    "check_interval": 1,
    "jumpscare_video": "jumpscare.mp4",
    "ffplay_path": "ffplay.exe"
}

def resource_path(filename):
    """ Get absolute path to bundled resource """
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

def extract_to_temp(files):
    temp_dir = tempfile.mkdtemp(prefix="usbprank_")
    for f in files:
        src = resource_path(f)
        dst = os.path.join(temp_dir, f)
        shutil.copy2(src, dst)
    return temp_dir

def load_config(config_path):
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load config: {e}")
        return DEFAULT_CONFIG

def play_jumpscare(ffplay_path, video_path):
    try:
        subprocess.Popen([
            ffplay_path,
            "-autoexit",
            "-fs",
            "-loglevel", "quiet",
            video_path
        ])
    except Exception as e:
        print(f"Error playing video: {e}")

def run_loop(temp_dir, config_file="jumpscare_config.json"):
    config = load_config(os.path.join(temp_dir, config_file))
    chance = config.get("chance_per_second", 0.0001)
    interval = config.get("check_interval", 1)
    video = os.path.join(temp_dir, config.get("jumpscare_video", "jumpscare.mp4"))
    ffplay = os.path.join(temp_dir, config.get("ffplay_path", "ffplay.exe"))

    while True:
        if random.random() < chance:
            play_jumpscare(ffplay, video)
        time.sleep(interval)

def main():
    required_files = ["ffplay.exe", "jumpscare.mp4", "jumpscare_config.json"]
    temp_dir = extract_to_temp(required_files)

    threading.Thread(target=run_loop, args=(temp_dir,), daemon=True).start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
