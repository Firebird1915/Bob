import wpilib

from wpilib import SmartDashboard
from wpilib.buttons import JoystickButton

class OI:

	def __init__(self, robot):
		self.joy = wpilib.Joystick(0)


		#Buttons for controller

	def getJoystick(self):
		return self.joy