
**Description**

This project includes a series of R scripts demonstrating fundamental programming concepts, data wrangling, and visualization techniques. Each script serves a specific purpose and is explained in the sections below.

**Important Note:**
To ensure proper execution of the scripts, all files must be located in the directory:
Documents/CMEECourseWork/week3/code.

**Scripts**

break.R

Demonstrates a while loop with a break condition. The script includes a counter that exits the loop when a specific condition (i == 10) is met.

sample.R

Compares sampling methods, focusing on the efficiency of preallocation versus dynamic vector growth. Highlights how preallocated vectors improve computational performance in loops.

Vectorize1.R

Compares loop-based summation with vectorized summation. Demonstrates the significant efficiency improvements achieved through vectorized operations in R.

R_conditionals.R

apply1.R

Uses the apply() function to compute row-wise and column-wise means and variances in a matrix. Illustrates the utility of apply() for streamlined operations on arrays.

boilerplate.R

Provides a basic function template that illustrates handling function arguments and outputs in R. This serves as a starting point for creating reusable functions.

apply2.R

Demonstrates the use of apply() with custom-defined functions. Highlights the flexibility of applying user-defined logic across matrix rows and columns.

DataWrang.R

Performs data wrangling steps, including reshaping and cleaning. Focuses on transforming data into a tidy format for easier analysis.

control_flow.R

Demonstrates for, if, and while control structures. Provides examples of conditional logic and iteration in R.

TreeHeight.R

Calculates the height of a tree using trigonometry. The function takes the angle of elevation and distance from the tree's base as input. Includes an example for clarity.

MyBars.R

Visualizes data from Results.txt using ggplot2. The script encountered warnings due to the size in geom_linerange, which can be resolved by updating to linewidth.

preallocate.R

Compares memory efficiency with and without preallocation in loops. Demonstrates the performance advantages of preallocated data structures in R.

try.R

Demonstrates error handling using try(). Suggests using tryCatch() for more structured and robust error management.

Pred_Prey_Overlay.R


Visualizes predator-prey data using ggplot2. Discusses issues with tidyverse package conflicts and suggests managing package loading order to resolve them.

browse.R

Contains browser() for debugging purposes. Recommends commenting out browser() in production or using it only in a sandbox environment.