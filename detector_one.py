#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from quaternion.msg import lidar 

# An obstacle detection module using 2D Lidar scans needs to be developed. 
# A rosbag containing a lidar scan topic is provided. 
# The environment contains one or more moving objects. 
# When objects are within the range of 2 metres, a ros message should be published as an output. 
# The message should contain the number of obstacles, the distances to the obstacles 
# (average distance in metres (d)) and the sizes of obstacles (in terms of start angle (SA), end angle (EA)).
#  Check the following figure for details:



obstacle_distances=0
obstacle_count=0
end_angle=0
start_angle=0
obstacle_avg_dist=0 

#what is ranges? what does it represent? means? is it an array of distances?  
# objects are moving 
# angle min and max are given in radians 
# seq im guessing is the message number
# stamp is timestamp?
# what is angle increment? angle between 2 consecutive laser beams
# wats scan time? how do uk we dont need it
# wats range min and max? ok so it cant detect obj closer than 25cm? ok those r edge cases
# now the array ranges in my head makes sense. this means its the length of the beams. 
# what are intensities?
# its essentially mapping out the region fr us
# lets take first 4 items in the array
# find out y for next 2 points. 

# [2.1640000343322754, 2.1600000858306885, 2.1559998989105225,  2.1600000858306885]
# 
# now how to get value of y with just angle? we know value of hypotenuse from array we know theta. 
# we need y which is perpendicular sin = opp/hyp = y/ 2.1600000858306885
# calculate sin theta = 0.00871439889  thats a ratio in meters
# 0.00871439889 = y/2.1600000858306885 => y = 2.1600000858306885 * 0.00871439889 = 0.01882310235 

# x= 2.1559998989105225 y= 2.1559998989105225* sin(0.00871439889*2)  = 

# y not? array item is hypotenuse ur right. i made a mistake in plotting
# we have to find x also but use cosine



# so the lidar is moving with angular increment, while objects are also moving, is there only 1 lazer per unit time being shot?
# need to assume that for simplicity whaat is 1 ms?
# we have starting angle 
# angle_min: -3.1241390705108643
# angle_max: 3.1415927410125732

# ok, if our distance which is basically our sample list is less than equal to 2, we send a message
# else we ignore
# code that if condition now


import math

def calculate_coordinates():

    sampleList = [2.1640000343322754, 2.1600000858306885, 2.1559998989105225,  2.1600000858306885]
    
    # for i, h in enumerate(sampleList): 
    #     opp= (math.sin(0.008714509196579456*i)) * h
    
    # calculate using for loop  i used wrong data structure- dict is wrong

# When objects are within the range of 2 metres, a ros message should be published as an output. THIS IS DONE
# The message should contain the number of obstacles, the distances to the obstacles # just count the number of times the if condition is true THIS IS DONE
# thats the number of obstacles, distances to each of the obstacles is just a subset of samplelist that are less than equal 2
# so store those hypotenuses in a new list

# (average distance in metres (d)) and the sizes of obstacles (in terms of start angle (SA), end angle (EA)). last one
# average is sum of lengths in distances/size of list

    coordinates_set = [] 
    distances=[]
    avg = 0
    angle_start =  -3.1241390705108643
    count = 0
    sum = 0
    angle_increment = 0.008714509196579456
                            
    # https://www.youtube.com/watch?v=Oal-aKJoC_U 

    for i, hypotenuse in enumerate(sampleList):
        if hypotenuse <= 2: 
            count=count+1 
            coordinates_set.append((math.cos(angle_increment*i)*hypotenuse,math.sin(angle_increment*i)*hypotenuse)) 
            distances.append(hypotenuse)
            print(coordinates_set)
            sum = sum + hypotenuse
            avg = sum / count 
     
            # is obstacle not a single point? how do uk which range value is referencing to that object 
            #if these are distances then what is this distance measured between? Between sensor and what part of the obstacle?

# header: 
#   seq: 1398
#   stamp: 
#     secs: 1652167184
#     nsecs: 189333170
#   frame_id: "base_laser"
# angle_min: -3.1241390705108643
# angle_max: 3.1415927410125732
# angle_increment: 0.008714509196579456
# time_increment: 0.0001814131683204323
# scan_time: 0.13043606281280518
# range_min: 0.25
# range_max: 12.0
#compare the scan_time and the time increment 
# each range array is from a single scan find out how many beams good thats the number of beams


        else:
            pass
    


# header: 
#   seq: 1398 
#   stamp: 
#     secs: 1652167184
#     nsecs: 189333170
#   frame_id: "base_laser"
# angle_min: -3.1241390705108643  
# angle_max: 3.1415927410125732
# angle_increment: 0.008714509196579456 <----- how do i k starting angle. Im assuming theta = 0 fr first value
# after that we increment with that value 👆
# time_increment: 0.0001814131683204323
# scan_time: 0.13043606281280518
# range_min: 0.25
# range_max: 12.0
# [2.1640000343322754, 2.1600000858306885, 2.1559998989105225,
#  2.1600000858306885, 2.1600000858306885, 2.1640000343322754]



# def scan_callback(scan_data):
#     global obstacle_count, obstacle_distances,obstacle_avg_dist, start_angle, end_angle

#     # print(len(scan_data.ranges))

#     for i, distance in enumerate(scan_data.ranges):
        
#         if distance < 2.0:
#             if obstacle_count == 0:
#                 obstacle_start_index = i
#             obstacle_count += 1
#             obstacle_distances += distance

#         elif obstacle_count > 0:

#             obstacle_avg_dist = obstacle_distances / obstacle_count
            
#             start_angle = scan_data.angle_min + obstacle_start_index * scan_data.angle_increment
#             end_angle = scan_data.angle_min + (i - 1) * scan_data.angle_increment
      
#             pub=rospy.Publisher('/obstacle_info', lidar, queue_size=10)
#             data=lidar()
#             data.number= obstacle_count
#             data.distance= obstacle_avg_dist
#             data.size_sa= start_angle
#             data.size_ea= end_angle
#             pub.publish(data)
#             print(data)
        
#             obstacle_count = 0
#             obstacle_distances = 0.0

#         elif distance > 2:
#             pass


# def sub():
#     rospy.init_node('obstacle_detector_node', anonymous=True)
#     rospy.Subscriber('/scan', LaserScan, scan_callback)
    
    
if __name__== '__main__':
    calculate_coordinates()
    # sub()
    # rospy.spin()