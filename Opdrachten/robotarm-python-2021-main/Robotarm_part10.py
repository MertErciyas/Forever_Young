from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for z in range(1,6):
    robotArm.grab()
    for a in range(2,13-(z*2)):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(9):
        robotArm.moveLeft()
    for c in range(z):
        robotArm.moveRight()                                                        
robotArm.wait()