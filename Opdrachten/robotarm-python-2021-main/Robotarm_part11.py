from pygame.constants import SCRAP_PBM
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
#robotArm.speed = 3
for i in range(9):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    colour = robotArm.scan()
    if colour != 'white':
        robotArm.drop()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.moveLeft() 
robotArm.wait()