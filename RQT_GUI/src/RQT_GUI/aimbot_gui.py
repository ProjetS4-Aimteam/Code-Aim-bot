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
        self.kpSpeed.valueChanged[float].connect(self.update_kp)
        self.kiSpeed.valueChanged[float].connect(self.update_ki)
        self.kdSpeed.valueChanged[float].connect(self.update_kd)
        self.kpTilt.valueChanged[float].connect(self.update_kpTilt)
        self.kiTilt.valueChanged[float].connect(self.update_kiTilt)
        self.kdTilt.valueChanged[float].connect(self.update_kdTilt)
        self.kpPan.valueChanged[float].connect(self.update_kpPan)
        self.kiPan.valueChanged[float].connect(self.update_kiPan)
        self.kdPan.valueChanged[float].connect(self.update_kdPan)
        
    def update_cup_pos(self, msg):
        cup_pos = round(msg.cup_distance,3)
        cup_angle = round(msg.cup_angle,3)
        self.CUP_POS.display(str(cup_pos))
        self.CUP_POS_ANGLE.display(str(cup_angle))

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
         
    #PID SPEED
    def update_kp(self, value):
        self.main.update_kp(value)

    def update_ki(self, value):
        self.main.update_ki(value)

    def update_kd(self, value):
        self.main.update_kd(value)
        
    #PID TILT
    def update_kpTilt(self, value):
        self.main.update_kpTilt(value)

    def update_kiTilt(self, value):
        self.main.update_kiTilt(value)

    def update_kdTilt(self, value):
        self.main.update_kdTilt(value)

    #PID PAN
    def update_kpPan(self, value):
        self.main.update_kpPan(value)

    def update_kiPan(self, value):
        self.main.update_kiPan(value)

    def update_kdPan(self, value):
        self.main.update_kdPan(value)

