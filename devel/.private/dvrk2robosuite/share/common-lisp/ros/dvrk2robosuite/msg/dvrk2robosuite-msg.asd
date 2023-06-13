
(cl:in-package :asdf)

(defsystem "dvrk2robosuite-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "measured_cp" :depends-on ("_package_measured_cp"))
    (:file "_package_measured_cp" :depends-on ("_package"))
  ))