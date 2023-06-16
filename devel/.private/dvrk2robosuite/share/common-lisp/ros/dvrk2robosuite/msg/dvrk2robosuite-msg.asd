
(cl:in-package :asdf)

(defsystem "dvrk2robosuite-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "measured_cp" :depends-on ("_package_measured_cp"))
    (:file "_package_measured_cp" :depends-on ("_package"))
    (:file "measured_cv" :depends-on ("_package_measured_cv"))
    (:file "_package_measured_cv" :depends-on ("_package"))
    (:file "measured_js" :depends-on ("_package_measured_js"))
    (:file "_package_measured_js" :depends-on ("_package"))
  ))