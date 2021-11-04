from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

#first block
robotArm.grab()

for a in range (10):
    robotArm.moveRight()

robotArm.drop()

for a in range (5,10):
    robotArm.moveLeft()

robotArm.grab()

for a in range (5,10):
    robotArm.moveRight()

robotArm.drop()

for a in range (8,10):
    robotArm.moveLeft()

robotArm.grab()
for a in range (8,10):
    robotArm.moveRight()

robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()