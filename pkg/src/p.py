#!/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
rospy.init_node("turtlee")
xgoal=rospy.get_param("x_goal")
ygoal=rospy.get_param("y_goal")
beta= rospy.get_param("B") 
phi= rospy.get_param("P") 
pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
x=0
y =0
angl=0
velmsg=Twist()
posemsg=Pose()
def callback_func (posemsg) -> None:
     global x
     global y , angl
     x =posemsg.x
     y=posemsg.y
     angl=posemsg.theta
rate=rospy.Rate(1)
sub=rospy.Subscriber("/turtle1/pose",Pose,callback_func)
while (True) :
    dist=math.sqrt(((xgoal-x)**2)+((ygoal-y)**2))
    #beta=0.5
    #phi=4.0
    linVel=beta*dist
    angVel=phi*( math.atan2(ygoal-y,xgoal-x) - angl)
    velmsg.linear.x=linVel
    velmsg.angular.z=angVel
    pub.publish(velmsg)
  
    if (dist<=0.01):
        break    

