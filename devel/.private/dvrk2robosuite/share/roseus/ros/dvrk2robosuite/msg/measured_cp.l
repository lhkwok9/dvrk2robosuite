;; Auto-generated. Do not edit!


(when (boundp 'dvrk2robosuite::measured_cp)
  (if (not (find-package "DVRK2ROBOSUITE"))
    (make-package "DVRK2ROBOSUITE"))
  (shadow 'measured_cp (find-package "DVRK2ROBOSUITE")))
(unless (find-package "DVRK2ROBOSUITE::MEASURED_CP")
  (make-package "DVRK2ROBOSUITE::MEASURED_CP"))

(in-package "ROS")
;;//! \htmlinclude measured_cp.msg.html


(defclass dvrk2robosuite::measured_cp
  :super ros::object
  :slots (_a _b _c _d _e _f _g _gripper ))

(defmethod dvrk2robosuite::measured_cp
  (:init
   (&key
    ((:a __a) 0.0)
    ((:b __b) 0.0)
    ((:c __c) 0.0)
    ((:d __d) 0.0)
    ((:e __e) 0.0)
    ((:f __f) 0.0)
    ((:g __g) 0.0)
    ((:gripper __gripper) 0.0)
    )
   (send-super :init)
   (setq _a (float __a))
   (setq _b (float __b))
   (setq _c (float __c))
   (setq _d (float __d))
   (setq _e (float __e))
   (setq _f (float __f))
   (setq _g (float __g))
   (setq _gripper (float __gripper))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:c
   (&optional __c)
   (if __c (setq _c __c)) _c)
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:e
   (&optional __e)
   (if __e (setq _e __e)) _e)
  (:f
   (&optional __f)
   (if __f (setq _f __f)) _f)
  (:g
   (&optional __g)
   (if __g (setq _g __g)) _g)
  (:gripper
   (&optional __gripper)
   (if __gripper (setq _gripper __gripper)) _gripper)
  (:serialization-length
   ()
   (+
    ;; float64 _a
    8
    ;; float64 _b
    8
    ;; float64 _c
    8
    ;; float64 _d
    8
    ;; float64 _e
    8
    ;; float64 _f
    8
    ;; float64 _g
    8
    ;; float64 _gripper
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _a
       (sys::poke _a (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _b
       (sys::poke _b (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _c
       (sys::poke _c (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _d
       (sys::poke _d (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _e
       (sys::poke _e (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _f
       (sys::poke _f (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _g
       (sys::poke _g (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gripper
       (sys::poke _gripper (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _a
     (setq _a (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _b
     (setq _b (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _c
     (setq _c (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _d
     (setq _d (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _e
     (setq _e (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _f
     (setq _f (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _g
     (setq _g (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gripper
     (setq _gripper (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get dvrk2robosuite::measured_cp :md5sum-) "175a49f06988368beca4d79073ba2f80")
(setf (get dvrk2robosuite::measured_cp :datatype-) "dvrk2robosuite/measured_cp")
(setf (get dvrk2robosuite::measured_cp :definition-)
      "float64 a
float64 b
float64 c
float64 d
float64 e
float64 f
float64 g
float64 gripper
")



(provide :dvrk2robosuite/measured_cp "175a49f06988368beca4d79073ba2f80")


