# Virtual Try-On with OpenCV and MediaPipe

## Project Description
This project demonstrates a virtual try-on application that uses OpenCV and MediaPipe to superimpose clothing images on a live webcam feed. The application detects human poses through the webcam, identifies key landmarks, and overlays the selected clothing image in real-time.

## Features
- Real-time pose detection using MediaPipe.
- Overlay of clothing images on detected torso area.
- Dynamic resizing and positioning of clothing images to fit the user.
- Interactive interface allowing users to change clothing images during execution.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/virtual-try-on.git
    cd virtual-try-on
    ```
2. Install required Python packages:
    ```bash
    pip install opencv-python mediapipe
    ```

## Notes
- Ensure that the clothing images have a transparent background to achieve a realistic overlay effect.
- The application relies on accurate detection of key landmarks; proper lighting and positioning can improve detection accuracy.
- The `cv2.waitKey(1)` function allows the application to listen for key presses without interrupting the main loop.

## Contributing
Feel free to submit issues, fork the repository, and send pull requests to contribute to this project.

## Acknowledgements
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)

---

Feel free to modify and enhance this project to suit your needs. Happy coding!
