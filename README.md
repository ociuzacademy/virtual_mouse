# AI Virtual Mouse 🖱️

A sophisticated AI-powered Virtual Mouse that uses computer vision to control your computer's cursor through hand gestures. Built with OpenCV and MediaPipe, this project allows for a touchless interaction experience.

## ✨ Features

-   **Smooth Cursor Movement**: Control the mouse cursor using your index finger with real-time smoothening for a natural feel.
-   **Left Click**: Perform a left click by pinching your **Index Finger** and **Thumb** together.
-   **Right Click**: Perform a right click by pinching your **Middle Finger** and **Thumb** together.
-   **Scrolling**: Scroll up by holding both your **Index** and **Middle fingers** up (with the thumb away).
-   **Real-time Hand Tracking**: Powered by MediaPipe for high-accuracy landmark detection.
-   **Hand Boundary Visualization**: Visual feedback in the camera feed shows the active region and tracking landmarks.

## 🛠️ Technology Stack

-   **Python**: Core programming language.
-   **OpenCV**: For image processing and camera feed management.
-   **MediaPipe**: For high-fidelity hand landmark detection.
-   **PyAutoGUI**: For controlling mouse movements and clicks.
-   **NumPy**: For coordinate interpolation and mathematical operations.

## 🚀 Getting Started

### Prerequisites

-   Python 3.7+
-   A working Webcam

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ociuzacademy/virtual_mouse.git
    cd virtual_mouse
    ```

2.  **Install dependencies**:
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

## 📖 Usage

1.  Run the main script:
    ```bash
    python virtual_mouse.py
    ```
2.  **Gesture Guide**:
    *   **Move Mouse**: Point with your **Index Finger**.
    *   **Left Click**: Pinch **Index Finger** and **Thumb**.
    *   **Right Click**: Pinch **Middle Finger** and **Thumb**.
    *   **Scroll Up**: Hold **Index** and **Middle** fingers up.
3.  Press **'q'** to exit the application.

## 📁 Project Structure

-   `virtual_mouse.py`: The main application script.
-   `handtracking_module.py`: A custom module for hand detection and landmark positioning.
-   `.gitignore`: Properly configured to exclude system files and large documents.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information (if applicable).

---
*Developed by [Ociuz Academy](https://github.com/ociuzacademy)*
