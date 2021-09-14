#!/usr/bin/env python
# -- coding:UTF-8 
import rospy
from std_msgs.msg import String

def talker():
    # 建立一發布者，主題(Topic)為 'chatter'，格式 String， 內存 10 個字
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # 建立一節點名稱 'talker'
    # anonymous=True : 於名稱後加上亂碼，防止重複命名同名稱
    rospy.init_node('talker', anonymous=True) 
    
    # 設置頻率 10 Hz
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
    
        hello_str = 'hello world %s' % rospy.get_time()
        
        # 顯示於螢幕，等同 print
        rospy.loginfo(hello_str)
        
        # 發布(內容)
        pub.publish(hello_str)
        
        # 休眠一次頻率時間
        rate.sleep()
        
if __name__ =='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass