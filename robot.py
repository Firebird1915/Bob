#!/usr/bin/env python3

import wpilib
from wpilib.command import Scheduler
from networktables import NetworkTable
import logging
from oi import OI

from subsystems.drivetrain import DriveTrain
from subsystems.pneumatics_comp import Pneumatics
from subsystems.intake import Intake
from subsystems.lift import LiftMech

class Bob(wpilib.IterativeRobot):

    #: update every 0.005 seconds/5 milliseconds (200Hz)
    kUpdatePeriod = 0.005

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.drivetrain = DriveTrain(self)
        self.pneumatics_comp = Pneumatics(self)
        self.intake = Intake(self)
        self.lift = LiftMech(self)
        self.oi = OI(self)
        self.sd = NetworkTable.getTable("SmartDashboard")

        self.drivetrain.drive.setExpiration(0.1)
        self.drivetrain.drive2.setExpiration(0.1)
        self.drivetrain.drive.setSafetyEnabled(True)
        self.drivetrain.drive2.setSafetyEnabled(True)


        
    def autonomousInit(self): #has nothing so far probably wont who knows

        self.auto_loop_counter = 0 #teaches the roboto how to count

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        self.drivetrain.drive.setSafetyEnabled(False)
        self.drivetrain.drive2.setSafetyEnabled(False)
        if self.auto_loop_counter < 100:
            self.drivetrain.drive.tankDrive(-0.5, -0.5) #drive forward
            self.drivetrain.drive2.tankDrive(-0.5, -0.5)
            self.auto_loop_counter += 1
        else:
            self.drivetrain.drive.tankDrive(0,0)
            self.drivetrain.drive2.tankDrive(0,0)
            self.drivetrain.drive.setSafetyEnabled(True)
            self.drivetrain.drive2.setSafetyEnabled(True)

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
        self.lift.log()
        self.sd.putNumber('someNumber', 1234) #checks to see if dashboard is working
        #self.sd.getBoolean('Right trigger?',self.r_trig.get())


if __name__ == "__main__":
    wpilib.run(Bob)
