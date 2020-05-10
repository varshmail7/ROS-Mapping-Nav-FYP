; Auto-generated. Do not edit!


(cl:in-package mybot_description-msg)


;//! \htmlinclude NavigateGoal.msg.html

(cl:defclass <NavigateGoal> (roslisp-msg-protocol:ros-message)
  ((goal_pose
    :reader goal_pose
    :initarg :goal_pose
    :type mybot_description-msg:MapPoint
    :initform (cl:make-instance 'mybot_description-msg:MapPoint)))
)

(cl:defclass NavigateGoal (<NavigateGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NavigateGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NavigateGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mybot_description-msg:<NavigateGoal> is deprecated: use mybot_description-msg:NavigateGoal instead.")))

(cl:ensure-generic-function 'goal_pose-val :lambda-list '(m))
(cl:defmethod goal_pose-val ((m <NavigateGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:goal_pose-val is deprecated.  Use mybot_description-msg:goal_pose instead.")
  (goal_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NavigateGoal>) ostream)
  "Serializes a message object of type '<NavigateGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NavigateGoal>) istream)
  "Deserializes a message object of type '<NavigateGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NavigateGoal>)))
  "Returns string type for a message object of type '<NavigateGoal>"
  "mybot_description/NavigateGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NavigateGoal)))
  "Returns string type for a message object of type 'NavigateGoal"
  "mybot_description/NavigateGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NavigateGoal>)))
  "Returns md5sum for a message object of type '<NavigateGoal>"
  "0907cf9164e93d95a21a0ade9222beb7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NavigateGoal)))
  "Returns md5sum for a message object of type 'NavigateGoal"
  "0907cf9164e93d95a21a0ade9222beb7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NavigateGoal>)))
  "Returns full string definition for message of type '<NavigateGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%mybot_description/MapPoint goal_pose~%~%================================================================================~%MSG: mybot_description/MapPoint~%# Message file for nodes in map~%~%uint8 mapPointID~%geometry_msgs/Point position~%float64 angleOfApproach~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NavigateGoal)))
  "Returns full string definition for message of type 'NavigateGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%mybot_description/MapPoint goal_pose~%~%================================================================================~%MSG: mybot_description/MapPoint~%# Message file for nodes in map~%~%uint8 mapPointID~%geometry_msgs/Point position~%float64 angleOfApproach~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NavigateGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NavigateGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'NavigateGoal
    (cl:cons ':goal_pose (goal_pose msg))
))
