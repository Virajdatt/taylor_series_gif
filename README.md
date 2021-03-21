# taylor_series_gif

## Introduction
Inspired from 3Blue1Brown to learn mathematics with vizualization and use these vizualization to better my intutions. I have created this repo which shows how Taylor series approximation gets better with additional degree of polyinomal added (specifically with the cos function as an example). Here I have utilized the python libraries matplotlib (to generate the graphs) and imageio (to create the gif).

![Taylor Series Cos Approximation with new increasing polynomial terms](https://github.com/Virajdatt/taylor_series_gif/blob/main/cos_approx.gif)

## Code Details

1. The src folder contains the source code, like the functions used to approximate the value of cos at a given value, plotting various values and creating the gif.
   The run_approx.py  runs these functions implemented in the approx.py file.

2. The tests folder contain a couple of test cases to confirm the code works as expected (TDD).

3. The notebooks folder contains a jupter notebook which shows how to use the functions from src (approx.py) to vizualize things.

Feel free to play around and implement other functions(like sin, e^x) and see how the approxmiations get better.

## TO-DO

Show how the Taylor Serier fails to approximate nasty discontinued function f(x) = 1/x when x<0 (As the funtion is undefined at x = 0 and if we start with x=1 we just get the upper right half the graph).
