from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
i = 1
scan = 'a'

while scan != '':
    robotArm.grab()
    scan = robotArm.scan()
    if scan != '':
        for a in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for b in range(9):
            robotArm.moveLeft()
    i += 1

robotArm.wait()