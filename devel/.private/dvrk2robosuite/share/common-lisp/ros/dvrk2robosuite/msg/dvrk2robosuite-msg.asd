
(cl:in-package :asdf)

(defsystem "dvrk2robosuite-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "measured_js" :depends-on ("_package_measured_js"))
    (:file "_package_measured_js" :depends-on ("_package"))
  ))