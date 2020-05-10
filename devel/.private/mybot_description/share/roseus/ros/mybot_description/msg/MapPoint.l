;; Auto-generated. Do not edit!


(when (boundp 'mybot_description::MapPoint)
  (if (not (find-package "MYBOT_DESCRIPTION"))
    (make-package "MYBOT_DESCRIPTION"))
  (shadow 'MapPoint (find-package "MYBOT_DESCRIPTION")))
(unless (find-package "MYBOT_DESCRIPTION::MAPPOINT")
  (make-package "MYBOT_DESCRIPTION::MAPPOINT"))

(in-package "ROS")
;;//! \htmlinclude MapPoint.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass mybot_description::MapPoint
  :super ros::object
  :slots (_mapPointID _position _angleOfApproach ))

(defmethod mybot_description::MapPoint
  (:init
   (&key
    ((:mapPointID __mapPointID) 0)
    ((:position __position) (instance geometry_msgs::Point :init))
    ((:angleOfApproach __angleOfApproach) 0.0)
    )
   (send-super :init)
   (setq _mapPointID (round __mapPointID))
   (setq _position __position)
   (setq _angleOfApproach (float __angleOfApproach))
   self)
  (:mapPointID
   (&optional __mapPointID)
   (if __mapPointID (setq _mapPointID __mapPointID)) _mapPointID)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:angleOfApproach
   (&optional __angleOfApproach)
   (if __angleOfApproach (setq _angleOfApproach __angleOfApproach)) _angleOfApproach)
  (:serialization-length
   ()
   (+
    ;; uint8 _mapPointID
    1
    ;; geometry_msgs/Point _position
    (send _position :serialization-length)
    ;; float64 _angleOfApproach
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _mapPointID
       (write-byte _mapPointID s)
     ;; geometry_msgs/Point _position
       (send _position :serialize s)
     ;; float64 _angleOfApproach
       (sys::poke _angleOfApproach (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _mapPointID
     (setq _mapPointID (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; geometry_msgs/Point _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; float64 _angleOfApproach
     (setq _angleOfApproach (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mybot_description::MapPoint :md5sum-) "25d6001ca9760cc13d10b9eb4e3a92e8")
(setf (get mybot_description::MapPoint :datatype-) "mybot_description/MapPoint")
(setf (get mybot_description::MapPoint :definition-)
      "# Message file for nodes in map

uint8 mapPointID
geometry_msgs/Point position
float64 angleOfApproach

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :mybot_description/MapPoint "25d6001ca9760cc13d10b9eb4e3a92e8")


