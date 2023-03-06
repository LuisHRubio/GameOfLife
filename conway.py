"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import keyboard
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import datetime

ON = 255
OFF = 0
vals = [ON, OFF]
hasStarted = False
pause = False

#TODO: Masks for Block, Beehive, Loaf, Boat, Tub, Blinker, Toad, Beacon, Glider and Spaceship

#------------------FOUR----------------------
block = np.array([[0, 0, 0, 0],
                  [0, ON, ON, 0],
                  [0, ON, ON, 0],
                  [0, 0, 0, 0]])
#------------------FIVE-------------------------
boat1 = np.array([[0, 0, 0, 0, 0],
                  [0, ON, ON, 0, 0],
                  [0, ON, 0, ON, 0],
                  [0, 0, ON, 0, 0],
                  [0, 0, 0, 0, 0]])
boat2 = np.rot90(boat1)
boat3 = np.rot90(np.rot90(boat1))
boat4 = np.rot90(np.rot90(np.rot90(boat1)))
#-------------------------------------------------
tub = np.array([[0, 0, 0, 0, 0],
                  [0, 0, ON, 0, 0],
                  [0, ON, 0, ON, 0],
                  [0, 0, ON, 0, 0],
                  [0, 0, 0, 0, 0]])
#-------------------------------------------------
blinkerV = np.array([[0, 0, 0, 0, 0],
                  [0, 0, ON, 0, 0],
                  [0, 0, ON, 0, 0],
                  [0, 0, ON, 0, 0],
                  [0, 0, 0, 0, 0]])
blinkerH = np.rot90(blinkerV)
#-------------------------------------------------
glider1 = np.array([[0, 0, 0, 0, 0],
                   [0, 0, 0, ON, 0],
                   [0, ON, 0, ON, 0],
                   [0, 0, ON, ON, 0],
                   [0, 0, 0, 0, 0]])
glider2 = np.array([[0, 0, 0, 0, 0],
                   [0, ON, 0, 0, 0],
                   [0, 0, ON, ON, 0],
                   [0, ON, ON, 0, 0],
                   [0, 0, 0, 0, 0]])
glider3 = np.array([[0, 0, 0, 0, 0],
                   [0, 0, ON, 0, 0],
                   [0, 0, 0, ON, 0],
                   [0, ON, ON, ON, 0],
                   [0, 0, 0, 0, 0]])
glider4 = np.array([[0, 0, 0, 0, 0],
                   [0, ON, 0, ON, 0],
                   [0, 0, ON, ON, 0],
                   [0, 0, ON, 0, 0],
                   [0, 0, 0, 0, 0]])
glider5 = np.rot90(glider1)
glider6 = np.rot90(glider2)
glider7 = np.rot90(glider3)
glider8 = np.rot90(glider4)
glider9 = np.rot90(np.rot90(glider1))
glider10 = np.rot90(np.rot90(glider2))
glider11 = np.rot90(np.rot90(glider3))
glider12 = np.rot90(np.rot90(glider4))
glider13 = np.rot90(np.rot90(np.rot90(glider1)))
glider14 = np.rot90(np.rot90(np.rot90(glider2)))
glider15 = np.rot90(np.rot90(np.rot90(glider3)))
glider16 = np.rot90(np.rot90(np.rot90(glider4)))
#-------------------------------------------------
spaceship1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, ON, 0, 0, ON, 0, 0],
                       [0, 0, 0, 0, 0, ON, 0],
                       [0, ON, 0, 0, 0, ON, 0],
                       [0, 0, ON, ON, ON, ON, 0],
                       [0, 0, 0, 0, 0, 0, 0]])
spaceship2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, ON, ON, 0, 0],
                       [0, ON, ON, 0, ON, ON, 0],
                       [0, ON, ON, ON, ON, 0, 0],
                       [0, 0, ON, ON, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]])
spaceship3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, ON, ON, ON, ON, 0],
                       [0, ON, 0, 0, 0, ON, 0],
                       [0, 0, 0, 0, 0, ON, 0],
                       [0, ON, 0, 0, ON, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]])
spaceship4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, ON, ON, 0, 0, 0],
                       [0, ON, ON, ON, ON, 0, 0],
                       [0, ON, ON, 0, ON, ON, 0],
                       [0, 0, 0, ON, ON, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]])
spaceship5 = np.rot90(spaceship1)
spaceship6 = np.rot90(spaceship2)
spaceship7 = np.rot90(spaceship3)
spaceship8 = np.rot90(spaceship4)
spaceship9 = np.rot90(np.rot90(spaceship1))
spaceship10 = np.rot90(np.rot90(spaceship2))
spaceship11 = np.rot90(np.rot90(spaceship3))
spaceship12 = np.rot90(np.rot90(spaceship4))
spaceship13 = np.rot90(np.rot90(np.rot90(spaceship1)))
spaceship14 = np.rot90(np.rot90(np.rot90(spaceship2)))
spaceship15 = np.rot90(np.rot90(np.rot90(spaceship3)))
spaceship16 = np.rot90(np.rot90(np.rot90(spaceship4)))
#--------------------SIX-------------------------
loaf1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, ON, ON, 0, 0],
                  [0, ON, 0, 0, ON, 0],
                  [0, ON, 0, ON, 0, 0],
                  [0, 0, ON, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]])
loaf2 = np.rot90(loaf1)
loaf3 = np.rot90(np.rot90(loaf1))
loaf4 = np.rot90(np.rot90(np.rot90(loaf1)))
#-------------------------------------------------
beacon1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, ON, ON, 0, 0, 0],
                  [0, ON, ON, 0, 0, 0],
                  [0, 0, 0, ON, ON, 0],
                  [0, 0, 0, ON, ON, 0],
                  [0, 0, 0, 0, 0, 0]])
beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, ON, ON, 0, 0, 0],
                  [0, ON, 0, 0, 0, 0],
                  [0, 0, 0, 0, ON, 0],
                  [0, 0, 0, ON, ON, 0],
                  [0, 0, 0, 0, 0, 0]])
beacon3 = np.rot90(beacon1)
beacon4 = np.rot90(beacon2)
#-------------------------------------------------
toad1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, ON, 0, 0],
                  [0, ON, 0, 0,ON, 0],
                  [0, ON, 0, 0, ON, 0],
                  [0, 0, ON, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]])
toad2 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, ON, ON,ON, 0],
                  [0, ON, ON, ON, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]])
toad3 = np.rot90(toad1)
toad4 = np.rot90(toad2)
toad5 = np.flip(toad1)
toad6 = np.flip(toad2)
toad7 = np.rot90(toad5)
toad8 = np.rot90(toad6)
#-------------------------------------------------
beehive1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, ON, ON, 0, 0],
                  [0, ON, 0, 0,ON, 0],
                  [0, 0, ON, ON, 0, 0],
                  [0, 0, 0, 0, 0, 0]])
beehive2 = np.rot90(beehive1)
#-------------------------------------------------




def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def NewGrid(Ny,Nx,ONCoordinates):
    """returns desired grid based in file"""
    tempGrid = np.random.choice([OFF,OFF], Ny*Nx, p=[0.2, 0.8]).reshape(Ny, Nx)
    for pair in ONCoordinates:
        tempGrid[pair[0],pair[1]] = ON
    return tempGrid

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    _glider = np.array([[255,    0, 0],
                       [255,  0, 255], 
                       [255,  255, 0]])
    grid[i:i+3, j:j+3] = _glider

def outputPrint(frame,Ny,Nx,blocks,beehives,loafs,boats,tubs,blinkers,toads,beacons,gliders,spaceships):
    total = blocks + beehives + loafs + boats + tubs + blinkers + toads + beacons + gliders + spaceships

    if frame == 0:
        with open("output.txt", "w", encoding='utf-8') as file:
            file.write(f"Simulation at {datetime.today().strftime('%Y-%m-%d')}\n")
            file.write(f"Universe size {Nx} x {Ny}\n")
            file.write("\n")
        file.close()

    if(total != 0):
        with open("output.txt", "a", encoding='utf-8') as file:
            # Write to the file
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write(f"−−           Iteration {frame}           −−\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write("|  Structure | Count | Percent   |\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write(f"|  Blocks    |  {blocks}   |    {int((blocks * 100) / total)}    |\n")
            file.write(f"|  Beehives  |  {beehives}   |    {int((beehives * 100) / total)}    |\n")
            file.write(f"|  Loafs     |  {loafs}   |    {int((loafs * 100) / total)}    |\n")
            file.write(f"|  Boats     |  {boats}   |    {int((boats * 100) / total)}    |\n")
            file.write(f"|  Tubs      |  {tubs}   |    {int((tubs * 100) / total)}    |\n")
            file.write(f"|  Blinkers  |  {blinkers}   |    {int((blinkers * 100) / total)}    |\n")
            file.write(f"|  Toads     |  {toads}   |    {int((toads * 100) / total)}    |\n")
            file.write(f"|  Beacons   |  {beacons}   |    {int((beacons * 100) / total)}    |\n")
            file.write(f"|  Gliders   |  {gliders}   |    {int((gliders * 100) / total)}    |\n")
            file.write(f"| Spaceships |  {spaceships}   |    {int((spaceships * 100) / total)}    |\n")
            file.write("−−−−−−−−−−−−− −−−−−−−−−−−−−−−−−−−\n")
            file.write(f"|    Total     | {total}   |         |\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write("\n\n\n")
        file.close()
    else:
        with open("output.txt", "a", encoding='utf-8') as file:
            # Write to the file
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write(f"−−           Iteration {frame}           −−\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write("|  Structure |  Count  |  Percent  |\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write(f"|  Blocks    |   {blocks}     |    {int((blocks * 100) / 1)}    |\n")
            file.write(f"|  Beehives  |   {beehives}     |    {int((beehives * 100) / 1)}    |\n")
            file.write(f"|  Loafs     |   {loafs}     |    {int((loafs * 100) / 1)}    |\n")
            file.write(f"|  Boats     |   {boats}     |    {int((boats * 100) / 1)}    |\n")
            file.write(f"|  Tubs      |   {tubs}     |    {int((tubs * 100) / 1)}    |\n")
            file.write(f"|  Blinkers  |   {blinkers}     |    {int((blinkers * 100) / 1)}    |\n")
            file.write(f"|  Toads     |   {toads}     |    {int((toads * 100) / 1)}    |\n")
            file.write(f"|  Beacons   |   {beacons}     |    {int((beacons * 100) / 1)}    |\n")
            file.write(f"|  Gliders   |   {gliders}     |    {int((gliders * 100) / 1)}    |\n")
            file.write(f"| Spaceships |   {spaceships}     |    {int((spaceships * 100) / 1)}    |\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write(f"|   Total    |   {total}     |         |\n")
            file.write("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−\n")
            file.write("\n\n\n")
        file.close()

def update(frameNum, img, grid, Ny,Nx, generations):
    global pause
    global hasStarted
    if keyboard.is_pressed('enter'):
        pause = not pause
    if not pause:
        # copy grid since we require 8 neighbors for calculation
        # and we go line by line

        #Nx = Ny == None
        if(Nx == None):
            Nx = Ny


        newGrid = grid.copy()

        num_blocks = 0
        num_boats = 0
        num_blinkers = 0
        num_beehives = 0
        num_loafs = 0
        num_toads = 0
        num_tubs = 0
        num_beacons = 0
        num_gliders = 0
        num_spaceships = 0



        newGrid = np.pad(newGrid, ((1, 1), (1, 1)), mode='constant', constant_values=0)

        if hasStarted:
            frameNum = frameNum+1

        if(frameNum==0):
            hasStarted=True
            print(f"Frame: {frameNum}")
            for y in range(Ny):
                #y = y + 1
                for x in range(Nx):
                    #x = x + 1

                    if newGrid[y,x] == OFF:
                        if np.array_equal(newGrid[y:y + 4, x:x + 4], block):
                            num_blocks += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], tub):
                            num_tubs += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat1):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat2):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat3):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat4):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], blinkerH):
                            num_blinkers += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], blinkerV):
                            num_blinkers += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider1):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider2):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider3):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider4):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider5):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider6):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider7):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider8):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider9):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider10):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider11):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider12):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider13):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider14):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider15):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider16):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf1):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf2):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf3):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf4):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon1):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon2):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon3):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon4):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad1):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad2):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad3):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad4):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad5):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad6):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad7):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad8):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 6], beehive1):
                            num_beehives += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 5], beehive2):
                            num_beehives += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship1):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship2):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship3):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship4):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship5):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship6):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship7):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship8):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship9):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship10):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship11):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship12):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship13):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship14):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship15):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship16):
                            num_spaceships += 1





            newGrid = newGrid[1:-1, 1:-1]

            outputPrint(frameNum,Ny,Nx,num_blocks,num_beehives,num_loafs,num_boats,num_tubs,num_blinkers,num_toads,num_beacons,num_gliders,num_spaceships)

            newGrid = np.pad(newGrid, ((1, 1), (1, 1)), mode='constant', constant_values=0)


        for y in range(Ny):
            y = y + 1
            for x in range(Nx):
                x = x + 1

                neighborMatrix = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                             (y, x - 1), (y, x + 1),
                             (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

                liveNeighborCount = 0
                for gy, gx in neighborMatrix:
                    if not (gy-1 < 0 or gx-1 < 0 or gy-1 >= Ny or gx-1 >= Nx):
                        if grid[gy-1, gx-1] == ON:
                            liveNeighborCount += 1

                if grid[y-1, x-1] == ON:
                    if liveNeighborCount < 2 or liveNeighborCount > 3:
                        newGrid[y, x] = OFF
                elif liveNeighborCount == 3:
                        newGrid[y, x] = ON

        num_blocks = 0
        num_boats = 0
        num_blinkers = 0
        num_beehives = 0
        num_loafs = 0
        num_toads = 0
        num_tubs = 0
        num_beacons = 0
        num_gliders = 0
        num_spaceships = 0

        if(True):
            print(f"Frame: {frameNum+1}")
            for y in range(Ny):
                #y = y + 1
                for x in range(Nx):
                    #x = x + 1
                    if newGrid[y, x] == OFF:
                        if np.array_equal(newGrid[y:y + 4, x:x + 4], block):
                            num_blocks += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], tub):
                            num_tubs += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat1):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat2):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat3):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], boat4):
                            num_boats += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], blinkerH):
                            num_blinkers += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], blinkerV):
                            num_blinkers += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider1):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider2):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider3):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider4):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider5):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider6):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider7):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider8):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider9):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider10):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider11):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider12):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider13):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider14):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider15):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 5], glider16):
                            num_gliders += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf1):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf2):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf3):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], loaf4):
                            num_loafs += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon1):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon2):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon3):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], beacon4):
                            num_beacons += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad1):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad2):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad3):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad4):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad5):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad6):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad7):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 6], toad8):
                            num_toads += 1
                        elif np.array_equal(newGrid[y:y + 5, x:x + 6], beehive1):
                            num_beehives += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 5], beehive2):
                            num_beehives += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship1):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship2):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship3):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship4):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship5):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship6):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship7):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship8):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship9):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship10):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship11):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 6, x:x + 7], spaceship12):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship13):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship14):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship15):
                            num_spaceships += 1
                        elif np.array_equal(newGrid[y:y + 7, x:x + 6], spaceship16):
                            num_spaceships += 1



            outputPrint(frameNum + 1, Ny, Nx, num_blocks, num_beehives, num_loafs, num_boats, num_tubs,num_blinkers, num_toads, num_beacons, num_gliders, num_spaceships)

        newGrid = newGrid[1:-1, 1:-1]



        # update data


        if frameNum+1 >= generations:
            sys.exit("Generations reached!")
        img.set_data(newGrid)
        grid[:] = newGrid[:]

    return img,

# main() function
def main():
    global pause
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    isRandomGrid = None
    N = None
    Ny = None
    Nx = None
    generations = 200

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    parser.add_argument('-r', '--random', type=str, choices=['True', 'False'], help='use a random grid')
    parser.add_argument('-s', '--size', type=int, help='size of the grid')
    parser.add_argument('-m', '--map', type=int, help='map to use')
    args = parser.parse_args()

    if args.random == "True":
        isRandomGrid = True
    elif args.random == "False":
        isRandomGrid = False
    print(isRandomGrid)
    N = args.size
    print(N)


    while isRandomGrid == None:
        ynInput = input("Do you want to read 'map1.csv' and create a game based on that? (y/n)")
        if ynInput == "y" or ynInput == "Y":
            isRandomGrid = False
        elif ynInput == "n" or ynInput == "N":
            isRandomGrid = True
        else:
            print("Invalid input")

    if isRandomGrid:
        # set grid size
        if N == None:
            N = int(input("Enter the desired size for the square universe: "))
        # declare grid
        grid = np.array([])
        # populate grid with random on/off - more off than on
        grid = randomGrid(N)
        # print(grid)
    else:
        with open(f'map{str(args.map)}.csv', 'r') as f:
            Ny, Nx = [int(x) for x in f.readline().split()]
            generations = int(f.readline())
            ONCoordinates = [[int(x) for x in line.split()] for line in f]

        # declare grid
        grid = np.array([])
        # populate grid with random on/off - more off than on
        grid = NewGrid(Ny, Nx, ONCoordinates)
        # print(grid)


    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(2, 6, grid)

    # set animation update interval
    updateInterval = 50 #It was 50 before --------
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    if isRandomGrid:
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N ,Ny, generations),
                                      frames = generations,
                                      interval=updateInterval,
                                      save_count=generations)
    elif not isRandomGrid:
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid, Ny,Nx, generations),
                                      frames=generations,
                                      interval=updateInterval,
                                      save_count=generations)

    plt.show()

# call main
if __name__ == '__main__':
    main()