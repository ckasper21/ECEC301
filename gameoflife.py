#!/usr/bin/python
"""
 Author: James A. Shackleford
   Date: Oct. 16th, 2015

   A simple implementation of Conway's Game of Life
"""
import patterns
import sys
import argparse
from matplotlib import pyplot as plt
from matplotlib import animation
from random import random


def generate_world(opts):
    """
    Accepts: opts  -- parsed command line options
    Returns: world -- a list of lists that forms a 2D pixel buffer

    Description: This function generates a 2D pixel buffer with dimensions
                 opts.cols x opts.rows (in pixels).  The initial contents
                 of the generated world is determined by the value provided
                 by opts.world_type: either 'random' or 'empty'  A 'random'
                 world has 10% 'living' pixels and 90% 'dead' pixels.  An
                 'empty' world has 100% 'dead' pixels.
    """
    world = []

    ## TASK 1 #############################################################
    if opts.world_type=='empty':
        world=[[0 for x in range(opts.rows)] for y in range(opts.cols)]
    elif opts.world_type=='random':
        world=[[0 for x in range(opts.rows)] for y in range(opts.cols)]
        for i in range(0,opts.rows):
            for j in range(0,opts.rows):
                randnum=random()
                if randnum < 0.10:
                    world[i][j]=1
    
    #######################################################################

    return world


def update_frame(frame_num, opts, world, img):
    """
    Accepts: frame_num  -- (automatically passed in) current frame number
             opts       -- a populated command line options instance
             world      -- the 2D world pixel buffer
             img        -- the plot image
    """

    # set the current plot image to display the current 2D world matrix
    img.set_array(world)

    # Create a *copy* of 'world' called 'new_world' -- 'new_world' will be
    # our offscreen drawing buffer.  We will draw the next frame to
    # 'new_world' so that we may maintain an in-tact copy of the current
    # 'world' at the same time.
    new_world = []
    for row in world:
        new_world.append(row[:])

    ## TASK 3 #############################################################
    for j in range(opts.rows): #row
        for i in range(opts.cols): #col
            # Check for if current position is along the top, bottom, left,
            # or right (and corners)
            if i==0: #Top area
                if j==0: #Top left corner
                    pos1=world[len(world)-1][len(world[0])-1]           
                    pos2=world[len(world)-1][j]
                    pos3=world[i][len(world[0])-1]
                    pos4=world[i][j+1]
                    pos5=world[i+1][j]
                    pos6=world[i+1][j+1]
                    pos7=world[i+1][len(world[0])-1]
                    pos8=world[len(world)-1][j+1]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    cur_point_val=world[i][j]
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                            
                elif j==(len(world[0])-1): #Top right corner
                    pos1=world[len(world)-1][j]            
                    pos2=world[len(world)-1][j-j]
                    pos3=world[i][j-1]
                    pos4=world[i][j-j]
                    pos5=world[i+1][j-1]
                    pos6=world[i+1][j]
                    pos7=world[i+1][j-j]
                    pos8=world[len(world)-1][j-1]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                else: #Top
                    pos1=world[len(world)-1][j-1]            
                    pos2=world[len(world)-1][j]
                    pos3=world[len(world)-1][j+1]
                    pos4=world[i][j-1]
                    pos5=world[i][j+1]
                    pos6=world[i+1][j-1]
                    pos7=world[i+1][j]
                    pos8=world[i+1][j+1]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=1
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
            elif i==(len(world)-1): #Bottom Area
                if j==0: #Bottom left corner
                    pos1=world[i-1][j]
                    pos2=world[i-1][j+1]
                    pos3=world[i][len(world[0])-1]
                    pos4=world[i][j+1]
                    pos5=world[i-i][len(world[0])-1]
                    pos6=world[i-i][j]
                    pos7=world[i-1][len(world[0])-1]
                    pos8=world[i-i][j+1]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                elif j==(len(world[0])-1): #Bottom right corner
                    pos1=world[i-1][j-1]
                    pos2=world[i-1][j]
                    pos3=world[i][j-1]
                    pos4=world[i][j-j]
                    pos5=world[i-i][j]
                    pos6=world[i-i][j-j]
                    pos7=world[i-i][j-1]
                    pos8=world[i-1][j-j]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                else: #Bottom
                    pos1=world[i-1][j-1]
                    pos2=world[i-1][j]
                    pos3=world[i-1][j+1]
                    pos4=world[i][j-1]
                    pos5=world[i][j+1]
                    pos6=world[i-i][j-1]
                    pos7=world[i-i][j]
                    pos8=world[i-i][j+1]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
            else: 
                 if j==0: #Left side
                    pos1=world[i-1][len(world[0])-1]
                    pos2=world[i-1][j]
                    pos3=world[i-1][j+1]
                    pos4=world[i][len(world[0])-1]
                    pos5=world[i][j+1]
                    pos6=world[i+1][len(world[0])-1]
                    pos7=world[i+1][j]
                    pos8=world[i+1][j+1]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                 elif j==(len(world[0])-1):#Right Side
                    pos1=world[i-1][j-1]
                    pos2=world[i-1][j]
                    pos3=world[i-1][j-j]
                    pos4=world[i][j-1]
                    pos5=world[i][j-j]
                    pos6=world[i+1][j-1]
                    pos7=world[i+1][j]
                    pos8=world[i+1][j-j]
                    cur_point_val=world[i][j]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]
                 else: #Rest of the space
                    pos1=world[i-1][j-1]
                    pos2=world[i-1][j]
                    pos3=world[i-1][j+1]
                    pos4=world[i][j-1]
                    pos5=world[i][j+1]
                    pos6=world[i+1][j-1]
                    pos7=world[i+1][j]
                    pos8=world[i+1][j+1]
                    total=pos1+pos2+pos3+pos4+pos5+pos6+pos7+pos8
                    cur_point_val=world[i][j]
                    if cur_point_val==1:
                        if total< 2:
                            new_world[i][j]=0
                        elif total>3:
                            new_world[i][j]=0
                        else:
                            new_world[i][j]=world[i][j]
                    else:
                        if total==3:
                            new_world[i][j]=1
                        else:
                            new_world[i][j]=world[i][j]



    #######################################################################

    # Copy the contents of the new_world into the world
    # (i.e. make the future the present)
    world[:] = new_world[:]
    return img,


def blit(world, sprite, x, y):
    """
    Accepts: world  -- a 2D world pixel buffer generated by generate_world()
             sprite -- a 2D matrix containing a pattern of 1s and 0s
             x      -- x world coord where left edge of sprite will be placed
             y      -- y world coord where top edge of sprite will be placed

    Returns: (Nothing)

    Description: Copies a 2D pixel pattern (i.e sprite) into the larger 2D
                 world.  The sprite will be copied into the 2D world with
                 its top left corner being located at world coordinate (x,y)
    """
    ## TASK 2 #############################################################

    sprite_x=len(sprite[0])
    sprite_y=len(sprite)
    for yy in range(sprite_y):
        for xx in range(sprite_x):
            world[y+yy][x+xx]=sprite[yy][xx]
    

    #######################################################################


def run_simulation(opts, world):
    """
    Accepts: opts  -- a populated command line options class instance
             world -- a 2D world pixel buffer generated by generate_world()

    Returns: (Nothing)

    Description: This function generates the plot that we will use as a
                 rendering surfance.  'Living' cells (represented as 1s in
                 the 2D world matrix) will be rendered as black pixels and
                 'dead' cells (represetned as 0s) will be rendered as
                 white pixels.  The method FuncAnimation() accepts 4
                 parameters: the figure, the frame update function, a
                 tuple containing arguments to pass to the update function,
                 and the frame update interval (in milliseconds).  Once the
                 show() method is called to display the plot, the frame
                 update function will be called every 'interval'
                 milliseconds to update the plot image (img).
    """
    if not world:
        print("The 'world' was never created.  Exiting")
        sys.exit()

    fig = plt.figure()
    img = plt.imshow(world, interpolation='none', cmap='Greys', vmax=1, vmin=0)
    ani = animation.FuncAnimation(fig,
                                  update_frame,
                                  fargs=(opts, world, img),
                                  interval=opts.framedelay)

    plt.show()


def report_options(opts):
    """
    Accepts: opts  -- a populated command line options class instance

    Returns: (Nothing)

    Descrption: This function simply prints the parameters used to
                start the 'Game of Life' simulation.
    """

    print("Conway's Game of Life")
    print("=====================")
    print("   World Size: %i x %i") % (opts.rows, opts.cols)
    print("   World Type: %s") % (opts.world_type)
    print("  Frame Delay: %i (ms)") % (opts.framedelay)


def get_commandline_options():
    """
    Accepts: (Nothing)

    Returns: opts  -- an instance of the options class that possesses members
                      specified by the 'dest' parameter of the add_option()
                      method.  Members contain the 'default' value unless
                      the user supplies a value from the command line using
                      the appropriate switch (i.e. '-r 100' or '--rows 100')

    optparse module documentation:
    https://docs.python.org/2/library/optparse.html
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--rows',
                        help='set # of rows in the world',
                        action='store',
                        type=int,
                        dest='rows',
                        default=75)

    parser.add_argument('-c', '--columns',
                        help='set # of columns in the world',
                        action='store',
                        type=int,
                        dest='cols',
                        default=50)

    parser.add_argument('-w', '--world',
                        help='type of world to generate',
                        action='store',
                        type=str,
                        dest='world_type',
                        default='empty')

    parser.add_argument('-d', '--framedelay',
                        help='time (in milliseconds) between frames',
                        action='store',
                        type=int,
                        dest='framedelay',
                        default=100)

    opts = parser.parse_args()

    return opts


def main():
    """
    The main function -- everything starts here!
    """
    opts = get_commandline_options()
    world = generate_world(opts)
    report_options(opts)

    blit(world, patterns.glider,20,20)

    run_simulation(opts, world)


if __name__ == '__main__':
    main()
