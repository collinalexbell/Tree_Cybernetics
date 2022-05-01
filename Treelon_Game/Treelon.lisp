
(ql:quickload :cl-opengl)
(defpackage :treelon (:use :cl))

(use-package :treelon)

(defun hunt-for-opengl (name)
  (format t "Velcomen, senor ~s~%Ve shall hunt for ze opengl example" name))
