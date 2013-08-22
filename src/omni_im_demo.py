#!/usr/bin/env python

import rospy
from interactive_markers.interactive_marker_server import *

server = None

def processMarkerFeedback(feedback):
    server.applyChanges()
    return

def makeControl(w, x, y, z, name, mode):
    control = InteractiveMarkerControl()
    control.orientation.w = w
    control.orientation.x = x
    control.orientation.y = y
    control.orientation.z = z
    control.name = name
    control.interaction_mode = mode
    return control

def makeMarker(name, x):
    # create an interactive marker for our server                                               
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = '/world'
    int_marker.name = name
    int_marker.pose.position.x = x
    int_marker.description = "Omni IM Demo"
    int_marker.scale = 0.1

    # create a grey box marker
    box_marker = Marker()
    box_marker.type = Marker.CUBE
    box_marker.scale.x = 0.045
    box_marker.scale.y = 0.045
    box_marker.scale.z = 0.045
    box_marker.color.r = 0.0
    box_marker.color.g = 0.5
    box_marker.color.b = 0.5
    box_marker.color.a = 1.0

    control = InteractiveMarkerControl()
    control.always_visible = True
    control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE_3D
    control.markers.append(box_marker)
    int_marker.controls.append(control)

    control = makeControl(1, 1, 0, 0, 'rotate_x', InteractiveMarkerControl.ROTATE_AXIS)
    int_marker.controls.append(control)

    control = makeControl(1, 1, 0, 0, 'move_x', InteractiveMarkerControl.MOVE_AXIS)
    int_marker.controls.append(control)

    control = makeControl(1, 0, 1, 0, 'rotate_z', InteractiveMarkerControl.ROTATE_AXIS)
    int_marker.controls.append(control)

    control = makeControl(1, 0, 1, 0, 'move_z', InteractiveMarkerControl.MOVE_AXIS)
    int_marker.controls.append(control)

    control = makeControl(1, 0, 0, 1, 'rotate_y', InteractiveMarkerControl.ROTATE_AXIS)
    int_marker.controls.append(control)

    control = makeControl(1, 0, 0, 1, 'move_y', InteractiveMarkerControl.MOVE_AXIS)
    int_marker.controls.append(control)

    server.insert(int_marker, processMarkerFeedback)

if __name__=='__main__':
    rospy.init_node('omni_im_demo')

    server = InteractiveMarkerServer('omni_im_demo')
    makeMarker('omni_im_demo_1', -0.3)
    makeMarker('omni_im_demo_2', 0.3)
    server.applyChanges()
    rospy.spin()
