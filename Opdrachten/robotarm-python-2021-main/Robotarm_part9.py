from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range(1,5):
    for e in range(i):
        robotArm.grab()
        for q in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for w in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()