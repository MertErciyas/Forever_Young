from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()

for a in range(7,10):
    robotArm.moveRight()

robotArm.drop()

for a in range(7,10):
    robotArm.moveLeft()

robotArm.grab()

for a in range(8,10):
    robotArm.moveRight()

robotArm.drop()

for a in range(1,10):
    robotArm.moveLeft()

robotArm.grab()

for a in range(9,10):
    robotArm.moveRight()

robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

for a in range(8,10):
    robotArm.moveRight()
robotArm.grab()

for a in range (8,10):
    robotArm.moveLeft()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()