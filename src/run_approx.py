import approx



images = approx.approx_plotting(10) # Plot iteratively value of cos between -360 to 360 degrees with increasing approxmation in the Taylor series (polynomial degrees upto 10)

approx.create_gif(filename='../cos_approx.gif', images=images) # Save the 10 images generated in the previous function as a gif