from styx_msgs.msg import TrafficLight
import numpy as np
import cv2


class TLClassifier(object):
    def __init__(self):
        #TODO load classifier

        self.num_pixels = 50
        
        self.lower_red = np.array([80,  80,  170], dtype = "uint8")
        self.upper_red = np.array([120, 120, 255], dtype = "uint8")

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        color = TrafficLight.UNKNOWN

        mask = cv2.inRange(image, self.lower_red, self.upper_red)
        color_detection = cv2.countNonZero(mask)

        if color_detection > self.num_pixels:
            color = TrafficLight.RED

        return color
