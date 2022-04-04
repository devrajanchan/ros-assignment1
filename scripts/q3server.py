#!/usr/bin/env python

from __future__ import print_function

from assignment_package.srv import q3, q3Response

import rospy

linear_velocity = 0.1


def handle_req(req):
    print("Returning [%s/%s]" % (linear_velocity, req.radius))
    resp2 = q3Response()
    resp2.angular_velocity = linear_velocity/req.radius
    return resp2.angular_velocity


def calc_plot():
    rospy.init_node('service_ang_vel_node')
    s = rospy.Service('service_ang_vel', q3, handle_req)
    print("Ready to give angular velocity")
    rospy.spin()


if __name__ == "__main__":
    calc_plot()
