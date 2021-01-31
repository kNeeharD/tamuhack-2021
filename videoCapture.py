import cv2 as ocv
import dlib
import time
from random import randrange

def utime():
    return round(time.time() * 1000)


video_feed = ocv.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

reset_time = utime()
last_scan_time = utime()
current_people = 0



people_through_security = 0
cycle = 0

def scanned_boarding_pass():
    global people_through_security
    people_through_security += 1

while True:
    if cycle == 6: # every thirty seconds
        processing_rate = people_through_security * 2
        people_through_security = 0
        cycle = 0
        estimated_wait_mins = current_people / processing_rate if processing_rate != 0 else 100000
        ##SEND POST with this number
        print('est wait -> %.3f' % estimated_wait_mins) # debug output
    print(current_people) # debug output
    if utime() - reset_time > 5000: # every 5 seconds
        reset_time = utime()
        current_people = 0
        cycle += 1
        ### this code simulates security processing rates ###
        ### in application, the boarding pass scanner at the start of the security area should trigger the scanned_boarding_pass function ###
        for i in range(0, randrange(10) % randrange(10)):
            scanned_boarding_pass()
    ret, frame = video_feed.read()
    frame = ocv.flip(frame, 1)
    gray = ocv.cvtColor(frame, ocv.COLOR_BGR2GRAY)
    faces = detector(gray)
    crowd_count = len(faces)
    current_people = max(current_people, crowd_count)


video_feed.release()
ocv.destroyAllWindows()
