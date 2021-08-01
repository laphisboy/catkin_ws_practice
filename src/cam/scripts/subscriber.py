#!/usr/bin/env python

import rospy
import cv2 

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


rospy.init_node("webcam_sub", anonymous=True)

bridge = CvBridge()

def callback(data):
    try: cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)


while not rospy.is_shutdown():

    rospy.Subscriber("webcam_image", Image, callback)
    rospy.spin()

cv2.destroyAllWindows()
