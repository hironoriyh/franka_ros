#!/usr/bin/env python
import moveit_commander
# from moveit_commander import MoveGroupCommander

import rospy
import geometry_msgs.msg


def main():
	rospy.init_node("moveit_test")
	r = rospy.Rate(10) # 10hz

	robot = moveit_commander.RobotCommander()
	group = moveit_commander.MoveGroupCommander('panda_arm')
	group.clear_pose_targets()
	# rospy.Subscriber("chatter", String, callback)
	group.set_max_velocity_scaling_factor(1.0)
	group.set_max_acceleration_scaling_factor(1.0)

	cnt = 0
	# while not rospy.is_shutdown():
	while cnt <3:
		cnt = cnt +1
		# r.sleep()

		joints = group.get_current_joint_values()
		print (joints[2], group.get_name())
		joints[2] = joints[2] + 0.5
		group.set_joint_value_target(joints)
		group.go()

		# rospy.Rate(0.5).sleep()

		joints[2] = joints[2] - 0.5
		group.set_joint_value_target(joints)
		group.go()



if __name__ == '__main__':
	# try:
    main()
	# except rospy.ROSInterruptException:
	# 	pass
