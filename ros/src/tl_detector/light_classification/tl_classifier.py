from styx_msgs.msg import TrafficLight
import numpy as np
import cv2


class TLClassifier(object):
    def __init__(self):
        #TODO load classifier

        self.num_pixels = 25
        
        self.lower_red = np.array([0,  0, 100], dtype = "uint8")
        self.upper_red = np.array([50, 56, 255], dtype = "uint8")

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
        num_red_pixels = cv2.countNonZero(mask)

        if num_red_pixels > self.num_pixels:
            color = TrafficLight.RED

        return color
