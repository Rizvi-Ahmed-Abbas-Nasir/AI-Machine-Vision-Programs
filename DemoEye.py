import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mash = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# face_mash = mp.solutions.face_mesh.FaceMesh() this will capture the whole face
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    # frame = cv2.flip(frame, 1) this will filp the frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mash.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        # for landmark in landmarks[]: this will capture the whole face
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y)
            print(x, y)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            diff = left[0].y - left[1].y
            if diff < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)


    cv2.imshow('Eye Controlled Mouse ', frame)
    cv2.waitKey(1)