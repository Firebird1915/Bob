import wpilib
from wpilib.command import Subsystem
from commands.tankdrive_with_joystick import TankDriveWithJoystick

class DriveTrain(Subsystem):
    '''
        The DriveTrain system holds all the inital calls for the motors this includes 
        encoders as well as the compressor and solenoid switch. If you need to mess with the motors in the drive here is the spot.
    '''

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        
        # Initialize gearbox Talons
        self.l_motor1 = wpilib.CANTalon(1)
        self.l_motor2 = wpilib.CANTalon(2)
        self.l_motor3 = wpilib.CANTalon(3)


        # Reverse our motors
        self.l_motor1.reverseOutput(True)
        self.l_motor2.reverseOutput(True)
        self.l_motor3.reverseOutput(True)

        # Slow ramp up to full speed.
        self.l_motor1.setVoltageRampRate(24/0.6)
        self.l_motor2.setVoltageRampRate(24/0.6)
        self.l_motor3.setVoltageRampRate(24/0.6)


        # Right gearbox Talon
        self.r_motor1 = wpilib.CANTalon(4)
        self.r_motor2 = wpilib.CANTalon(5)
        self.r_motor3 = wpilib.CANTalon(6)

        self.r_motor1.reverseOutput(True)
        self.r_motor2.reverseOutput(True)
        self.r_motor3.reverseOutput(True)

        self.r_motor1.setVoltageRampRate(24/0.6)
        self.r_motor2.setVoltageRampRate(24/0.6)
        self.r_motor3.setVoltageRampRate(24/0.6)

        # #Compressor starts from the drivetrain but this all might change
        # if self.robot.isReal():
        #     self.compressor = wpilib.Compressor()
        #     self.compressor.start()
        
        # self.switcher = wpilib.DoubleSolenoid(0,1)
        # self.shifter = False            

        #Encoder talons from testbed
        #self.motor1 = wpilib.CANTalon(8) #initialize the motor as a Talon on channel 1
        #self.motor2 = wpilib.CANTalon(2)

        '''This is set to the first two sets of gearbox motors for each side'''
        self.drive = wpilib.RobotDrive(self.l_motor1, # Tells the robot to call the tank drive method
                                       self.l_motor2,
                                       self.r_motor1,
                                       self.r_motor2)

        '''This is for the two 3rd motors of each gearbox'''
        self.drive2= wpilib.RobotDrive(self.l_motor3,self.r_motor3)


        self.motor_encoder = wpilib.Encoder(0,1) # position of these two motors

        # Block for eventual test simulation
        self.sd = wpilib.SmartDashboard

    def initDefaultCommand(self):
        ''' If i didn't tell you to do something else
            you should let me drive
        '''
        self.setDefaultCommand(TankDriveWithJoystick(self.robot))


    def driveManual(self,left,right):
        '''Tank style driving
        '''
        self.drive.tankDrive(left,right)
        self.drive2.tankDrive(left,right)

    def driveJoystick(self, joy):
        ''' using a controller to drive tank style '''
        self.drive.tankDrive(joy.getRawAxis(1)/1.2, joy.getRawAxis(5)/1.2)
        self.drive2.tankDrive(joy.getRawAxis(1)/1.2,joy.getRawAxis(5)/1.2) #these have to be the same as self.drive or you might break the gearboxes
    
    # #turbo mode
    # def shiftFast(self):
    #     self.switcher.set(1)
    #     self.shifter = True

    # #cruise mode
    # def shiftReturn(self):
    #     self.switcher.set(0)
    #     self.shifter = False

    # #did we change speeds?
    # def is_shifted(self):
    #     return self.shifter

    def reset(self):
        ''' reset the encoders '''
        self.motor_encoder.reset()

    def log(self):
        # self.sd.putDouble("Encoder Distance", self.motor1.getEncPosition())
        # self.sd.putDouble("Big Encoder", self.motor1.getEncPosition()*2)
        pass            
