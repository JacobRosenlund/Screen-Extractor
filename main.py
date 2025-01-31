# TODO
# - Intercept keystrokes and detect hotkeys
# - Screenshot
# - OCR extract text from screen
# - Save to txt file
# - Send keystrokes based on txt file

import keyboard
import easyocr
from PIL import ImageGrab

print("Setting up")

output_file = "write.txt"

print("Defining hotkeys")
# escape_keys = "shift+esc"
extract_keys = "alt+m"
write_keys = "alt+n"

print("Setting image bounds")
class image_bounds:
    x = 0
    y = 0
    width = 300
    height = 300

print("Configuring `easyocr`")
reader = easyocr.Reader(["en"])

def screenshot():
    screenshot = ImageGrab.grab(bbox = (image_bounds.x, image_bounds.y, image_bounds.width, image_bounds.height))
    screenshot.save("screenshot.png")
    screenshot.close()

def extract():
    print("Extracting")
    screenshot()
    result = reader.readtext("screenshot.png", detail = 0)

    output = ""
    for word in result:
        output = output + " " + word

    print("Result:\n" + output)
    with open(output_file, "w") as f:
        f.write(output)

def send_string(string):
    for letter in string:
        keyboard.send(letter)

def write():
    print("Writing")
    with open(output_file, "r") as f:
        send_string(f.read())


keyboard.add_hotkey(extract_keys, extract)
keyboard.add_hotkey(write_keys, write)

keyboard.wait()