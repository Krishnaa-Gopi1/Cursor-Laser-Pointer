import serial
import pyautogui
import time


PORT = 'COM9'          
BAUD_RATE = 9600       
UPDATE_DELAY = 0.01   


try:
    arduino = serial.Serial(PORT, BAUD_RATE)
    time.sleep(2)  
    print(f"Connected to Arduino on {PORT}")
except Exception as e:
    print(f"[ERROR] Could not connect to Arduino on {PORT}: {e}")
    exit()


screen_width, screen_height = pyautogui.size()

def scale(val, in_min, in_max, out_min, out_max):
    """Map val from screen range to servo angle range."""
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

print("Tracking mouse... (Ctrl+C to stop)")

try:
    while True:
        x, y = pyautogui.position()

        angle_x = scale(x, 0, screen_width, 0, 180)
        angle_y = scale(y, 0, screen_height, 0, 180)

        command = f"{angle_x},{angle_y}\n"
        arduino.write(command.encode())

        

        time.sleep(UPDATE_DELAY)
except KeyboardInterrupt:
    print("\n[INFO] Exiting...")
    arduino.close()
except Exception as e:
    print(f"[ERROR] {e}")
    arduino.close()
