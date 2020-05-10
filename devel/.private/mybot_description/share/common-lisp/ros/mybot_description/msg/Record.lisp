; Auto-generated. Do not edit!


(cl:in-package mybot_description-msg)


;//! \htmlinclude Record.msg.html

(cl:defclass <Record> (roslisp-msg-protocol:ros-message)
  ((time
    :reader time
    :initarg :time
    :type cl:float
    :initform 0.0)
   (input
    :reader input
    :initarg :input
    :type cl:float
    :initform 0.0)
   (output
    :reader output
    :initarg :output
    :type cl:float
    :initform 0.0))
)

(cl:defclass Record (<Record>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Record>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Record)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mybot_description-msg:<Record> is deprecated: use mybot_description-msg:Record instead.")))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <Record>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:time-val is deprecated.  Use mybot_description-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'input-val :lambda-list '(m))
(cl:defmethod input-val ((m <Record>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:input-val is deprecated.  Use mybot_description-msg:input instead.")
  (input m))

(cl:ensure-generic-function 'output-val :lambda-list '(m))
(cl:defmethod output-val ((m <Record>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mybot_description-msg:output-val is deprecated.  Use mybot_description-msg:output instead.")
  (output m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Record>) ostream)
  "Serializes a message object of type '<Record>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'input))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'output))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Record>) istream)
  "Deserializes a message object of type '<Record>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'input) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'output) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Record>)))
  "Returns string type for a message object of type '<Record>"
  "mybot_description/Record")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Record)))
  "Returns string type for a message object of type 'Record"
  "mybot_description/Record")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Record>)))
  "Returns md5sum for a message object of type '<Record>"
  "b9c15b4326735ca7166c3d905ae5b1de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Record)))
  "Returns md5sum for a message object of type 'Record"
  "b9c15b4326735ca7166c3d905ae5b1de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Record>)))
  "Returns full string definition for message of type '<Record>"
  (cl:format cl:nil "~%float64 time~%float64 input~%float64 output~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Record)))
  "Returns full string definition for message of type 'Record"
  (cl:format cl:nil "~%float64 time~%float64 input~%float64 output~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Record>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Record>))
  "Converts a ROS message object to a list"
  (cl:list 'Record
    (cl:cons ':time (time msg))
    (cl:cons ':input (input msg))
    (cl:cons ':output (output msg))
))
