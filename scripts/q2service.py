#!/usr/bin/env python
from __future__ import print_function

from assignment_package.srv import q2, q2Response
import rospy


def handle_q2service(req):
    xintermediate = []
    yintermediate = []
    t = 0
    while(t < 10):
        print("Returning [%s+%s*%s , %s+%s*%s ]" %
              (req.x, req.vx, t, req.y, req.vy, t))
        response = q2Response()

        (xintermediate).append(req.x+req.vx*t)
        (yintermediate).append(req.y+req.vy*t)
        t = t+1
    response.xi = xintermediate
    response.yi = yintermediate
    print(response.xi)
    print(response.yi)
    return response.xi, response.yi


def calc_inter_server():
    rospy.init_node('service_node')
    s = rospy.Service('service', q2, handle_q2service)
    print("Ready to give intermediate co-ordinates")
    rospy.spin()


if __name__ == "__main__":
    calc_inter_server()
