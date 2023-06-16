; Auto-generated. Do not edit!


(cl:in-package dvrk2robosuite-msg)


;//! \htmlinclude measured_cv.msg.html

(cl:defclass <measured_cv> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (twist
    :reader twist
    :initarg :twist
    :type geometry_msgs-msg:Twist
    :initform (cl:make-instance 'geometry_msgs-msg:Twist)))
)

(cl:defclass measured_cv (<measured_cv>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <measured_cv>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'measured_cv)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dvrk2robosuite-msg:<measured_cv> is deprecated: use dvrk2robosuite-msg:measured_cv instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <measured_cv>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dvrk2robosuite-msg:header-val is deprecated.  Use dvrk2robosuite-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'twist-val :lambda-list '(m))
(cl:defmethod twist-val ((m <measured_cv>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dvrk2robosuite-msg:twist-val is deprecated.  Use dvrk2robosuite-msg:twist instead.")
  (twist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <measured_cv>) ostream)
  "Serializes a message object of type '<measured_cv>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'twist) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <measured_cv>) istream)
  "Deserializes a message object of type '<measured_cv>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'twist) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<measured_cv>)))
  "Returns string type for a message object of type '<measured_cv>"
  "dvrk2robosuite/measured_cv")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'measured_cv)))
  "Returns string type for a message object of type 'measured_cv"
  "dvrk2robosuite/measured_cv")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<measured_cv>)))
  "Returns md5sum for a message object of type '<measured_cv>"
  "98d34b0043a2093cf9d9345ab6eef12e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'measured_cv)))
  "Returns md5sum for a message object of type 'measured_cv"
  "98d34b0043a2093cf9d9345ab6eef12e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<measured_cv>)))
  "Returns full string definition for message of type '<measured_cv>"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Twist twist~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'measured_cv)))
  "Returns full string definition for message of type 'measured_cv"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Twist twist~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <measured_cv>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'twist))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <measured_cv>))
  "Converts a ROS message object to a list"
  (cl:list 'measured_cv
    (cl:cons ':header (header msg))
    (cl:cons ':twist (twist msg))
))
