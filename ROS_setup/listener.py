#!/usr/bin/env python
# -- coding:UTF-8 
import rospy
from std_msgs.msg import String

def callback(data):
    # rospy.loginfo() 將內容顯示於終端機上，類似 print
    rospy.loginfo(rospy.get_caller_id()+'I heard %s', data.data)

def listener():
    # 建立一節點名稱 'listener'
    # anonymous=True : 於名稱後加上亂碼，防止重複命名同名稱
    rospy.init_node('listener', anonymous=True) 
    
     # 建立一訂閱者，主題(Topic)為'chatter'，格式 String， 內容函式 callback
    rospy.Subscriber('chatter', String, callback)
    
    # 使程式不斷執行
    rospy.spin()
    
if __name__ =='__main__':
    listener()