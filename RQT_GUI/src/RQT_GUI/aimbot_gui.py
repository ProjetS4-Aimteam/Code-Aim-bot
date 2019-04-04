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
        self.Manual_control_check.stateChanged[int].connect(self.update_mode)
        self.Launch_manual.pressed.connect(self.launch_start)   #launch in Manual tab
        self.Launch_Aimbot.pressed.connect(self.launch_start)   #launch in Aimbot tab
        self.Launch_manual.released.connect(self.launch_stop)   #launch in Manual tab
        self.Launch_Aimbot.released.connect(self.launch_stop)   #launch in Aimbot tab
        self.tilt_angle.valueChanged[float].connect(self.update_tilt)
        self.pan_angle.valueChanged[float].connect(self.update_pan)
        self.motor_speed_man.valueChanged[float].connect(self.update_speed)    #Motor_speed in manual tab
        self.motor_speed_pid.valueChanged[float].connect(self.update_speed)    #Motor_speed in pid tab
        self.kp.valueChanged[float].connect(self.update_kp)
        self.ki.valueChanged[float].connect(self.update_ki)
        self.kd.valueChanged[float].connect(self.update_kd)
        
    def update_cup_pos(self, msg):
        cup_pos = round(msg.data,3)
        self.CUP_POS.display(str(cup_pos))

    def update_mode(self, mode):
        self.main.change_mode(mode)

    def launch_start(self):
        self.main.launch_start()
        
    def launch_stop(self):
        self.main.launch_stop()

    def update_tilt(self, value):
            self.main.update_tilt(value)

    def update_pan(self, value):
            self.main.update_pan(value)

    def update_speed(self, value):
            self.main.update_motor_speed(value)

    def update_kp(self, value):
        self.main.update_kp(value)

    def update_ki(self, value):
        self.main.update_ki(value)

    def update_kd(self, value):
        self.main.update_kd(value)

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
