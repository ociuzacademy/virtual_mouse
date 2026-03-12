import cv2
import numpy as np
import handtracking_module as htm
import time
import pyautogui
import math

##########################################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 5
##########################################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    if not success:
        break
    
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger
        x2, y2 = lmList[12][1:] # Middle finger
        x0, y0 = lmList[4][1:]  # Thumb tip

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        
        # Draw the ROI (Region of Interest) rectangle
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4. Moving Mode: Only Index Finger is up
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            
            # 7. Move Mouse
            # Use pyautogui.moveTo with flipped x for natural movement
            pyautogui.moveTo(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Left Click Mode: Index and Thumb pinch
        if fingers[1] == 1:
            length_index, img, lineInfo_index = detector.findDistance(8, 4, img, draw=False)
            if length_index < 30:
                cv2.circle(img, (lineInfo_index[4], lineInfo_index[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
                time.sleep(0.1) # Small delay to prevent accidental multi-clicks

        # 9. Right Click Mode: Middle and Thumb pinch
        if fingers[2] == 1:
            length_middle, img, lineInfo_middle = detector.findDistance(12, 4, img, draw=False)
            if length_middle < 30:
                cv2.circle(img, (lineInfo_middle[4], lineInfo_middle[5]), 15, (0, 0, 255), cv2.FILLED)
                pyautogui.rightClick()
                time.sleep(0.1)

        # 10. Scrolling Mode: Index and Middle fingers both up
        if fingers[1] == 1 and fingers[2] == 1:
            # Check if thumb is AWAY to avoid confusing with clicks
            length_thumb_index, _, _ = detector.findDistance(8, 4, img, draw=False)
            if length_thumb_index > 40:
                # Find distance between index or middle to scroll (or just check tip movement)
                # For simplicity, we'll just scroll when both are up
                pyautogui.scroll(20) # Scroll up
                cv2.putText(img, "Scrolling", (wCam-150, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # 12. Display
    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
