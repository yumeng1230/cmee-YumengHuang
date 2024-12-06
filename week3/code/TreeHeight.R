# This function calculates the height of a tree given the distance from its base
# and the angle of elevation to its top, using the trigonometric formula:
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation to the tree's top (in degrees)
# distance:  The distance from the base of the tree (in meters or any consistent unit)
#
# OUTPUT
# The height of the tree, in the same units as "distance"

TreeHeight <- function(degrees, distance) {
    radians <- degrees * pi / 180 # Convert angle from degrees to radians
    height <- distance * tan(radians) # Calculate height using the tangent function
    print(paste("Tree height is:", height, "units")) # Display the calculated height
    return(height) # Return the height
}

# Example Calculations
# Example 1: Calculate the height of a tree with a 37-degree elevation angle and 40-meter distance
example1 <- TreeHeight(37, 40) 
print(paste("Example 1: The height of the tree is", example1, "meters"))

# Example 2: Calculate the height of a tree with a 60-degree elevation angle and 10-meter distance
example3 <- TreeHeight(60, 10) 
print(paste("Example 2: The height of the tree is", example2, "meters"))
