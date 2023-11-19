#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from quaternion.msg import lidar 

obstacle_distances=0
obstacle_count=0
end_angle=0
start_angle=0
obstacle_avg_dist=0 

def scan_callback(scan_data):
    global obstacle_count, obstacle_distances,obstacle_avg_dist, start_angle, end_angle

    # print(len(scan_data.ranges))

    for i, distance in enumerate(scan_data.ranges):
        
        if distance < 2.0:
            if obstacle_count == 0:
                obstacle_start_index = i
            obstacle_count += 1
            obstacle_distances += distance

        elif obstacle_count > 0:

            obstacle_avg_dist = obstacle_distances / obstacle_count
            start_angle = scan_data.angle_min + obstacle_start_index * scan_data.angle_increment
            end_angle = scan_data.angle_min + (i - 1) * scan_data.angle_increment
      
            pub=rospy.Publisher('/obstacle_info', lidar, queue_size=10)
            data=lidar()
            data.number= obstacle_count
            data.distance= obstacle_avg_dist
            data.size_sa= start_angle
            data.size_ea= end_angle
            pub.publish(data)
            print(data)
        
            obstacle_count = 0
            obstacle_distances = 0.0

        elif distance > 2:
            pass

def sub():
    rospy.init_node('obstacle_detector_node', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    
if __name__== '__main__':
    sub()
    rospy.spin()