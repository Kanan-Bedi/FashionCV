import streamlit as st
import mediapipe as mp
import cv2
def page2():  
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose()
        
        # Load the clothing image
        clothing_image = cv2.imread("2.png", cv2.IMREAD_UNCHANGED)
        
        st.title("Clothing Try-On")
        
        # Initialize webcam capture
        cap = cv2.VideoCapture(0)  # 0 for the default webcam
        
        for i in range (0,2):
            # Read a frame from the webcam
            ret, frame = cap.read()
        
            if not ret:
                st.error("Failed to capture frame")
                break
        
            # Convert the frame to RGB (MediaPipe requires RGB images)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
            # Detect landmarks on the frame
            results = pose.process(frame_rgb)
        
            # Check if landmarks are detected
            if results.pose_landmarks:
                # Extract landmarks of interest
                lm_left_shoulder_x = int(results.pose_landmarks.landmark[11].x * frame.shape[1])
                lm_left_shoulder_y = int(results.pose_landmarks.landmark[11].y * frame.shape[0])
                lm_right_shoulder_x = int(results.pose_landmarks.landmark[12].x * frame.shape[1])
                lm_right_shoulder_y = int(results.pose_landmarks.landmark[12].y * frame.shape[0])
                lm_left_hip_x = int(results.pose_landmarks.landmark[23].x * frame.shape[1])
                lm_left_hip_y = int(results.pose_landmarks.landmark[23].y * frame.shape[0])
                lm_right_hip_x = int(results.pose_landmarks.landmark[24].x * frame.shape[1])
                lm_right_hip_y = int(results.pose_landmarks.landmark[24].y * frame.shape[0])
        
                # Calculate the midpoint between the left and right shoulder
                mid_shoulder_x = (lm_left_shoulder_x + lm_right_shoulder_x) // 2
                mid_shoulder_y = (lm_left_shoulder_y + lm_right_shoulder_y) // 2
        
                # Calculate the width and height of the torso area (between shoulders and hips)
                desired_width = abs(lm_right_shoulder_x - lm_left_shoulder_x)
                desired_height = abs(lm_right_hip_y - lm_left_shoulder_y)
        
                # Calculate the aspect ratio of the clothing image
                clothing_aspect_ratio = clothing_image.shape[1] / clothing_image.shape[0]
        
                # Calculate the desired width based on the aspect ratio
                desired_clothing_width = int(desired_height * clothing_aspect_ratio)
        
                # Resize clothing image to match the desired height and preserve aspect ratio
                clothing_image_resized = cv2.resize(clothing_image, (desired_clothing_width, desired_height))
        
                # Calculate the position to align the clothing image with the midpoint between shoulders
                x_offset = mid_shoulder_x - (desired_clothing_width // 2)
                y_offset = mid_shoulder_y
        
                # Ensure the region where clothing will be overlaid has correct dimensions
                height, width, _ = frame.shape
                max_y = min(y_offset + clothing_image_resized.shape[0], height)
                max_x = min(x_offset + clothing_image_resized.shape[1], width)
        
                # Overlay the clothing on the frame
                for c in range(0, 3):
                    frame[y_offset:max_y, x_offset:max_x, c] = \
                        frame[y_offset:max_y, x_offset:max_x, c] * \
                        (1 - clothing_image_resized[:max_y - y_offset, :max_x - x_offset, 3] / 255.0) + \
                        clothing_image_resized[:max_y - y_offset, :max_x - x_offset, c] * \
                        (clothing_image_resized[:max_y - y_offset, :max_x - x_offset, 3] / 255.0)
        
            # Display the result
            st.image(frame, channels="BGR", use_column_width=True)
        
            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
              