#!/usr/bin/env python
# -- coding:UTF-8 
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+'I heard %s' % data.data)

if __name__ =='__main__':
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('chat', String, callback)
    
    # 使程式不斷執行
    rospy.spin()