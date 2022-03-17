#!/usr/bin/env python
import rospy
from std_msgs.msg import String

data2 = " "


def callback2(data):
    global data2
    data2 = data.data


def callback1(data):

    rospy.Subscriber("/world", String, callback2)
    print(data.data+data2)
# # def callback1(data):
#     rospy.loginfo(rospy.get_caller_id() + "%s", data.data)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/hello", String, callback1)

    rospy.spin()


if __name__ == '__main__':
    listener()
