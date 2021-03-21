import numpy as np
import matplotlib.pyplot as plt
import math
import imageio
import sys

def ts_cos_x(x, nofapprox):
    """ This function returns the approximation of cos("x") as per the Taylor series
    up until the "nofapprox" of degrees of polynomial

    Args:
        x (int): value of cos angle in radians
        nofapprox (int): No of degrees of polynomial to which the Taylor series for cos("x") need to be approximated to

    Returns:
        [int]: the approximate value of cos("x") for nofapprox degrees of polynomial for the value x

    example:
        1. ts_cos_x(0,1) : returns 0 since cos(0) is 0
        2. ts_cos_x(90,1) : returns 1 since cos(90) is 0 # here x is in degrees.
    """    
    
    result = 0
    for i in range(nofapprox):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2*i)
        result += (coef) * ((num)/(denom))
    return result


def approx_plotting(approx, n_frames=3):
    '''
    Function to plot the values from the cos() function implemented in math library and
    the points approximated by our custom ts_cos_x approximation function.

    Args:

        approx (int): No of degrees of polynomial to which the Taylor series for cos("x") need to be approximated to
        n_frames (int): Number of times the same image needs to be repeated in ur frames when you create the gif.
                        WE need to do this in order to make our gif's tranistions smooth during frames.
                        To test what happens if this is not the case, set n_frames to 1 and test.
    
    return:
        [list]: fnames a list of filenames

    '''
    fnames = []
    if n_frames <=0:
        print("Invalid argument for n_frames")
        sys.exit()
    for i in range(approx): 
        angles = np.arange(-2*np.pi,2*np.pi,0.1)
        p_cos = np.cos(angles)
        t_cos = [ts_cos_x(angle,i) for angle in angles]

        fig, ax = plt.subplots()
        ax.plot(angles,p_cos)
        ax.plot(angles,t_cos)
        ax.set_ylim([-5,5])
        ax.legend(['cos() function',f'Taylor Series - {i} terms'], loc="upper right")
        plt.grid()
        ax.axhline(y=0, color='b')
        ax.axvline(x=0, color='r')
        #print(f'../plots/cos_aprrox_{i}.png')
        plt.savefig(f'../plots/cos_aprrox_{i}.png')
        for frames in range(n_frames):
            fnames.append(f'../plots/cos_aprrox_{i}.png')
    
    return fnames



def create_gif(filename, images):
    """This function is to create a gif by typing up the various plots created.

    Args:
        filename (str): filename with which the gif needs to be saved as
        images (list): the list with paths to the image that need to be stichted together in a gif 
    """    
    with imageio.get_writer(filename, mode='I') as writer:
        for filename in images:
            image = imageio.imread(filename)
            writer.append_data(image)
