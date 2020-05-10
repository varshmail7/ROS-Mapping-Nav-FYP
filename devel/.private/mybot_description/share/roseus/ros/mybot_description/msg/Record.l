;; Auto-generated. Do not edit!


(when (boundp 'mybot_description::Record)
  (if (not (find-package "MYBOT_DESCRIPTION"))
    (make-package "MYBOT_DESCRIPTION"))
  (shadow 'Record (find-package "MYBOT_DESCRIPTION")))
(unless (find-package "MYBOT_DESCRIPTION::RECORD")
  (make-package "MYBOT_DESCRIPTION::RECORD"))

(in-package "ROS")
;;//! \htmlinclude Record.msg.html


(defclass mybot_description::Record
  :super ros::object
  :slots (_time _input _output ))

(defmethod mybot_description::Record
  (:init
   (&key
    ((:time __time) 0.0)
    ((:input __input) 0.0)
    ((:output __output) 0.0)
    )
   (send-super :init)
   (setq _time (float __time))
   (setq _input (float __input))
   (setq _output (float __output))
   self)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:input
   (&optional __input)
   (if __input (setq _input __input)) _input)
  (:output
   (&optional __output)
   (if __output (setq _output __output)) _output)
  (:serialization-length
   ()
   (+
    ;; float64 _time
    8
    ;; float64 _input
    8
    ;; float64 _output
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _input
       (sys::poke _input (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _output
       (sys::poke _output (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _input
     (setq _input (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _output
     (setq _output (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get mybot_description::Record :md5sum-) "b9c15b4326735ca7166c3d905ae5b1de")
(setf (get mybot_description::Record :datatype-) "mybot_description/Record")
(setf (get mybot_description::Record :definition-)
      "
float64 time
float64 input
float64 output

")



(provide :mybot_description/Record "b9c15b4326735ca7166c3d905ae5b1de")


