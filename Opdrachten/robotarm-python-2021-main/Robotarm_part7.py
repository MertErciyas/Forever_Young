from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for a in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for var in range(2):
        robotArm.moveRight()
robotArm.wait()