import time
import sys # to access the system
import cv2

match input("What is being held up to the camera?: "):
    case "glass":
        glassbin = cv2.imread("Images\glassbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Yellow, 'Glass' Bin", glassbin)
        cv2.setWindowProperty("Please place your waste in the Yellow, 'Glass' Bin", cv2.WND_PROP_TOPMOST, 1)
    case "plastic":
        plasticbin = cv2.imread("Images\plasticbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Blue, 'Plastic' Bin", plasticbin)
        cv2.setWindowProperty("Please place your waste in the Blue, 'Plastic' Bin", cv2.WND_PROP_TOPMOST, 1)
    case "metal":
        metalbin = cv2.imread("Images\metalbin.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Please place your waste in the Red, 'Metal' Bin", metalbin)
        cv2.setWindowProperty("Please place your waste in the Red, 'Metal' Bin", cv2.WND_PROP_TOPMOST, 1)
    case _:
        print("Input not recognized!")

cv2.waitKey(1)
time.sleep(5)
cv2.destroyAllWindows()