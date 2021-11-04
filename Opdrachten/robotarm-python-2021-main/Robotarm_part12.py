from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
#robotArm.speed = 3
b=0
for i in range(9):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == 'red':
        for x in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for a in range(9-i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    b=b+1 
robotArm.wait()