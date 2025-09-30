# 🚗 Dr. Driving Gesture Control with Python

Control **Dr. Driving** using **hand gestures** detected from your camera.  
This project uses **Python + OpenCV + MediaPipe** for gesture recognition, and sends the controls to the game using either:

- **ADB (Android Debug Bridge)** → for playing on a real phone  
- **PyAutoGUI** → for playing on an emulator (BlueStacks, Nox, LDPlayer, etc.)  

---

## 📖 Description

This project turns your hand into a **virtual controller** for Dr. Driving.  
You can **accelerate, brake, and steer** just by showing gestures to your camera.  

### Example Gesture Controls:
- ✊ **Fist** → Brake  
- ☝️ **One Finger (Index)** → Accelerate  
- ✌️ **Two Fingers** → Steer Left  
- 🤟 **Three Fingers** → Steer Right  
- 🖐 **Open palm (all fingers)** → Reverse

---

## 📦 Requirements

- Python 3.8+  
- A webcam (for gesture detection)  
- [ADB installed](https://developer.android.com/studio/releases/platform-tools) (for phone setup)  
- Dr. Driving installed on your phone or emulator  

Install dependencies:
```bash
pip install opencv-python mediapipe pyautogui
