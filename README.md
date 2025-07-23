# Cursor-Laser-Pointer

Control **two micro servos** using your **mouse cursor**!  
The **X** and **Y** screen positions are translated into angles (0–180°) and sent to an **Arduino Uno** via Serial.

This can be used for:

- Laser pointer turrets
- Camera gimbals
- Servo-based XY drawing arms
- Eye-tracking experiments, etc.

---

## 🧰 Requirements

### Hardware:

- Arduino Uno (or compatible)
- 2x Micro Servos (e.g., SG90)
- USB cable (for serial communication)
- Jumper wires + breadboard
- (Optional) External 5V power for servo

### Software:

- Arduino IDE
- Python 3.x
- VS Code (recommended for Python)
- Virtual Environment (`venv`)

---

## 🧠 How It Works

1. Python reads your mouse cursor position using `pyautogui`.
2. X and Y screen coordinates are scaled to **0–180**.
3. The values are sent to the Arduino over USB Serial.
4. The Arduino reads them and moves each servo accordingly.

---

## 🚀 Getting Started

### 1. 🧠 Upload Arduino Code

1. Open `arduino/servo_control.ino` in Arduino IDE.
2. Select board: **Arduino Uno**
3. Select correct **Port** (e.g., COM9).
4. Upload the code.

### 2. 🐍 Run Python Mouse Tracker

#### Setup (first time only):

```bash
cd python
python -m venv venv
venv\Scripts\activate         # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
```

#### Run:

```bash
python mouse_tracker.py
```

> Make sure `PORT = 'COMx'` in `mouse_tracker.py` matches your Arduino's port.

---

## 🛠️ Wiring

| Servo | Arduino Pin         |
| ----- | ------------------- |
| X     | D9                  |
| Y     | D10                 |
| VCC   | 5V (or external 5V) |
| GND   | GND                 |

---

## 📦 Python Dependencies

```
pyserial
pyautogui
```

Install via:

```bash
pip install -r requirements.txt
```

---
