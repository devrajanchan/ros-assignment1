
#! /usr/bin/python
import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y


def main():
    rospy.init_node("noderad")
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()


if __name__ == '__main__':
    main()
