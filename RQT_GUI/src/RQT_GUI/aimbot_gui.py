import os
import rospkg
import rospy
import numpy as np
from rospkg import RosPack

from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QFileDialog
from python_qt_binding.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from std_msgs.msg import Float32, Bool, Int32, String


class AimBotWidget(QtWidgets.QWidget):
    def __init__(self, main):
        super(AimBotWidget, self).__init__()

        ui_file = os.path.join(rospkg.RosPack().get_path('RQT_GUI'), 'resource', 'AIMBOT_PLUGIN.ui')
        loadUi(ui_file, self)

        rp = RosPack()
        self.pkg_path = rp.get_path('RQT_GUI')

        self.main = main

        self.CUP_POS.display(0)
        self.verticalSlider.valueChanged[int].connect(self.test_txt_update)
        self.label.setText(str(0))

    def update_cup_pos(self, msg):
        cup_pos = round(msg.data,3)
        self.CUP_POS.display(str(cup_pos))

    def test_txt_update(self, value):
        self.label.setText(str(value))

"""
        self.disable_btn.clicked[bool].connect(self.enable_motors_callback)
        self.auto_btn.clicked[bool].connect(lambda: self.change_mode(AUTO))
        self.track_btn.clicked[bool].connect(self.track_face_callback)
        self.home_btn.clicked[bool].connect(self.home_callback)

        self.yaw_slider.valueChanged[int].connect(self.slider_callback_yaw)
        self.pitch_slider.valueChanged[int].connect(self.slider_callback_pitch)
        self.roll_slider.valueChanged[int].connect(self.slider_callback_roll)
        
        self.val_yaw.setText(str(0))
        self.val_pitch.setText(str(0)) 
        self.val_roll.setText(str(0))

    def update_motors(self, angles):
        self.val_yaw.setText(str(angles[0]))
        self.val_pitch.setText(str(angles[1])) 
        self.val_roll.setText(str(angles[2]))
        
    def home_callback(self):
        self.change_mode(MANUAL)
        self.main.go_home()
        self.yaw_slider.setValue(50)
        self.pitch_slider.setValue(50)
        self.roll_slider.setValue(50)

    def change_mode(self, mode):
        if mode == MANUAL:
            self.auto_btn.setEnabled(True)
            
        if mode == AUTO:
            self.auto_btn.setEnabled(False)
        self.main.change_mode(mode)
 
    def enable_motors_callback(self, enable):
        if self.disable_btn.text() == "Enable":
            self.main.enable_motors(True)
            self.disable_btn.setText("Disable")

        elif self.disable_btn.text() == "Disable":
            self.main.enable_motors(False)
            self.disable_btn.setText("Enable")

    def track_face_callback(self):
        pass
    
    def slider_callback_yaw(self, value):
        self.change_mode(MANUAL)
        self.main.move_axis(1, value-50, [-50, 50])    

    def slider_callback_pitch(self, value):
        self.change_mode(MANUAL)
        self.main.move_axis(2, value-50, [-50, 50])  

    def slider_callback_roll(self, value):
        self.change_mode(MANUAL)
        self.main.move_axis(3, value-50, [-50, 50])   

"""
