#!/usr/bin/env python

from __future__ import print_function

from matplotlib import pyplot as plt

import sys
import rospy
from assignment_package.srv import *
import numpy as np


def getintermediatecoordinates(x, y, vx, vy):
    rospy.wait_for_service('service')
    try:
        intermediatecoordinates = rospy.ServiceProxy('service', q2)
        response = intermediatecoordinates(x, y, vx, vy)
        print(response.xi)
        return response.xi, response.yi
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [x y vx vy]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 5:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        vx = int(sys.argv[3])
        vy = int(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s %s %s %s" % (x, y, vx, vy))

    x_int = (x, y, getintermediatecoordinates(x, y, vx, vy)[0][1])
    y_int = (x, y, getintermediatecoordinates(x, y, vx, vy)[0][2])
    # print((x, y, getintermediatecoordinates(x, y, vx, vy)[1]))
    # print((x, y, getintermediatecoordinates(x, y, vx, vy)[0]))
    xpoints = np.array(x_int)
    ypoints = np.array(y_int)
    plt.rcParams["figure.autolayout"] = True
    plt.plot(xpoints, ypoints)
    plt.show()
