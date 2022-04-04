#!/usr/bin/python

import rospy
from std_msgs.msg import String


def radiuspub():
    message_pub = rospy.Publisher("/radius", String, queue_size=10)
    rospy.init_node("noderadpub")
    msg1 = String()
    msg1.data = "5"
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        message_pub.publish(msg1)
        print(msg1)
        rate.sleep()


if __name__ == '__main__':
    try:
        radiuspub()
    except rospy.ROSInterruptException:
        pass
