import cv2 

def main():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("camera is not open")
        return
    while True:
        ret, frame=cap.read()
        if not ret or cv2.waitKey(1) & 0xff==ord("q"):
            break
        cv2.imshow("camera",frame)
    cv2.release() 
    cv2.destroyAllWindows()

if __name__ =="__main__":
   main()
 