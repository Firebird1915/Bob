import wpilib
from wpilib.command import Subsystem
from networktables import NetworkTable

from commands.tankdrive_with_joystick import TankDriveWithJoystick

class DriveTrain(Subsystem):
	'''The DriveTrain system holds all the inital calls for the motors this includes 
		encoders as well. If you need to mess with the motors here is the spot.
	'''

	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		
		self.motor1 = wpilib.CANTalon(1) #initialize the motor as a Talon on channel 1
		self.motor2 = wpilib.CANTalon(2)

		self.drive = wpilib.RobotDrive(self.motor1, # Tells the robot to call the tank drive method
									   self.motor2) # Alternatively can use two stick method later on


		self.motor_encoder = wpilib.Encoder(1,2) # position of these two motors

		#block for eventual test simulation (see docs)

		wpilib.LiveWindow.addActuator("Motors", "Dummy Motor 1", self.motor1)
		wpilib.LiveWindow.addActuator("Motors", "Dummy Motor 2", self.motor2)
		wpilib.LiveWindow.addSensor("Motors", "Dummy Encoder 1", self.motor_encoder)

	def initDefaultCommand(self):
		''' If i didn't tell you to do something else
			you should let me drive
		'''
		self.setDefaultCommand(TankDriveWithJoystick(self.robot))

	def log(self):
		pass

	def driveManual(self,left,right):
		'''Tank style driving
		'''
		self.drive.tankDrive(left,right)

	def driveJoystick(self, joy):
		''' using a controller to drive tank style '''
		self.driveManual(-joy.getY(), -joy.getAxis(wpilib.Joystick.AxisType.kThrottle))

	def reset(self):
		''' reset the encoders '''
		self.motor_encoder.reset()

	def getDistance(self):
		''' returns the distance driven'''
		return (self.motor_encoder.getDistance())
