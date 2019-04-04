import os
import rospkg
import rospy
import rosnode
from rospkg import RosPack
from qt_gui.plugin import Plugin
import subprocess
from python_qt_binding import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from std_msgs.msg import Float32
from filtre.msg import UIParameter
from filtre.msg import cup_pos

from .aimbot_gui import AimBotWidget

class AimBotPlugin(Plugin):
    """
        Application window controller
    """

    def __init__(self, context):
        super(AimBotPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('AimBotPlugin')

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print('arguments: ', args)
            print('unknowns: ', unknowns)

        # Create Application main
        self.main = AimBotMain()
        self._widget = self.main.get_widget()
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() +
                                        (' (%d)' % context.serial_number()))
        context.add_widget(self._widget)

    ####### Tutorial functions #########
    def shutdown_plugin(self):
        # TODO unregister all publishers here
        # Stopping the path_creator node
        rospy.signal_shutdown('Shutting down')

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    # def trigger_configuration(self):
    # Comment in to signal that the plugin has a way to configure
    # This will enable a setting button (gear icon) in each dock widget title bar
    # Usually used to open a modal configuration dialog


class AimBotMain():
    def __init__(self):
        self.widget = AimBotWidget(self)
        #self.manual_mode = False
        self.UI_parameter = UIParameter()
        self.cup_pos_msg = rospy.Subscriber("cup_pos", cup_pos, self.cup_pos_callback)
        #self.UImsg = rospy.Subscriber("msgUIParameter",UIParameter, self.ui_callback)
        self.UI_pub = rospy.Publisher("msgUIParameter",UIParameter, queue_size=0)
        

    def get_widget(self):
        return self.widget

    def cup_pos_callback(self, data):
        self.widget.update_cup_pos(data)
	
    def launch_start(self):
        self.UI_parameter.launch = True
        self.UI_pub.publish(self.UI_parameter)

    def launch_stop(self):
        self.UI_parameter.launch = False
        self.UI_pub.publish(self.UI_parameter)

    def change_mode(self, mode):
        self.UI_parameter.mode = mode
        self.UI_pub.publish(self.UI_parameter)

    def update_kp(self,kp):
        self.UI_parameter.kpSpeed= kp
        self.UI_pub.publish(self.UI_parameter)

    def update_ki(self,ki):
        self.UI_parameter.kiSpeed = ki
        self.UI_pub.publish(self.UI_parameter)

    def update_kd(self,kd):
        self.UI_parameter.kdSpeed = kd
        self.UI_pub.publish(self.UI_parameter)

    def update_motor_speed(self,speed):
        self.UI_parameter.motor_speed = speed
        self.UI_pub.publish(self.UI_parameter)

    def update_tilt(self,tilt):
        self.UI_parameter.tilt_angle = tilt
        self.UI_pub.publish(self.UI_parameter)

    def update_pan(self,pan):
        self.UI_parameter.pan_angle = pan
        self.UI_pub.publish(self.UI_parameter)



