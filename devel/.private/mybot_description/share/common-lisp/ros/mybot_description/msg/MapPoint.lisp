; Auto-generated. Do not edit!


(cl:in-package mybot_description-msg)


;//! \htmlinclude MapPoint.msg.html

(cl:defclass <MapPoint> (roslisp-msg-protocol:ros-message)
  ((mapPointID
    :reader mapPointID
    :initarg :mapPointID
    :type cl:fixnum
    :initform 0)
   (position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (angleOfApproach
    :reader angleOfApproach
    :initarg :angleOfApproach
    :type cl:float
    :initform 0.0))
)

(cl:defclass MapPoint (<MapPoint>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MapPoint>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MapPoint)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mybot_description-msg:<MapPoint> is deprecated: use mybot_description-msg:MapPoint instead.")))

(cl:ensure-generic-function 'mapPointID-val :lambda-list '(m))
(cl:defmethod mapPointID-val ((m <MapPoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:mapPointID-val is deprecated.  Use mybot_description-msg:mapPointID instead.")
  (mapPointID m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <MapPoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:position-val is deprecated.  Use mybot_description-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'angleOfApproach-val :lambda-list '(m))
(cl:defmethod angleOfApproach-val ((m <MapPoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:angleOfApproach-val is deprecated.  Use mybot_description-msg:angleOfApproach instead.")
  (angleOfApproach m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MapPoint>) ostream)
  "Serializes a message object of type '<MapPoint>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mapPointID)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angleOfApproach))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MapPoint>) istream)
  "Deserializes a message object of type '<MapPoint>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mapPointID)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angleOfApproach) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MapPoint>)))
  "Returns string type for a message object of type '<MapPoint>"
  "mybot_description/MapPoint")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MapPoint)))
  "Returns string type for a message object of type 'MapPoint"
  "mybot_description/MapPoint")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MapPoint>)))
  "Returns md5sum for a message object of type '<MapPoint>"
  "25d6001ca9760cc13d10b9eb4e3a92e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MapPoint)))
  "Returns md5sum for a message object of type 'MapPoint"
  "25d6001ca9760cc13d10b9eb4e3a92e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MapPoint>)))
  "Returns full string definition for message of type '<MapPoint>"
  (cl:format cl:nil "# Message file for nodes in map~%~%uint8 mapPointID~%geometry_msgs/Point position~%float64 angleOfApproach~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MapPoint)))
  "Returns full string definition for message of type 'MapPoint"
  (cl:format cl:nil "# Message file for nodes in map~%~%uint8 mapPointID~%geometry_msgs/Point position~%float64 angleOfApproach~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MapPoint>))
  (cl:+ 0
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MapPoint>))
  "Converts a ROS message object to a list"
  (cl:list 'MapPoint
    (cl:cons ':mapPointID (mapPointID msg))
    (cl:cons ':position (position msg))
    (cl:cons ':angleOfApproach (angleOfApproach msg))
))
