#!/usr/bin/env python

import rospy
from moveit_commander import MoveGroupCommander
from actionlib_msgs.msg import GoalStatusArray

if __name__ == '__main__':
    rospy.init_node('move_to_start')
    rospy.wait_for_message('move_group/status', GoalStatusArray)
    # rospy.logwarn(GoalStatusArray.status_list[0].goal_id)
    # print GoalStatusArray
    commander = MoveGroupCommander('panda_arm')
    commander.set_named_target('ready')
    # rospy.logwarn(commander.goal_id)
    commander.go()

    # rospy.Rate(2).sleep()
    # commander.set_named_target('home')
    # commander.go()
