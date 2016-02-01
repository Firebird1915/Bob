#!/usr/bin/env python3

import wpilib
from wpilib.command import Scheduler
from networktables import NetworkTable
import logging
from oi import OI

from subsystems.drivetrain import DriveTrain

class Bob(wpilib.IterativeRobot):

	#: update every 0.005 seconds/5 milliseconds (200Hz)
	kUpdatePeriod = 0.005

	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
		"""
		self.drivetrain = DriveTrain(self)
		self.oi = OI(self)
		self.sd = NetworkTable.getTable("SmartDashboard")


		
	def autonomousInit(self): #has nothing so far probably wont who knows

		self.auto_loop_counter = 0 #teaches the roboto how to count

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""

		# if self.auto_loop_counter < 100:
		#     self.robot_drive.drive(-0.5, 0) #drive forward
		#     self.auto_loop_counter += 1
		# else:
		#     self.robot_drive.drive(0,0)
		

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		#cancel out autonomous
		while self.isOperatorControl() and self.isEnabled():

			Scheduler.getInstance().run()
			self.log()
		

	def testPeriodic(self):
		"""This function is called periodically during test mode."""
		wpilib.LiveWindow.run()

	def log(self):
		self.drivetrain.log()
		self.sd.putNumber('someNumber', 1234)


if __name__ == "__main__":
	wpilib.run(Bob)
