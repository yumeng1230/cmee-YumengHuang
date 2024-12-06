# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

setwd("Documents/CMEECourseWork/week7/code")  
# 
TreeHeight <- function(degrees, distance) {
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))
  
  return (height)
}

trees_data <- read.csv("../data/trees.csv")  

# 
if (!("Angle.degrees" %in% colnames(trees_data)) || !("Distance.m" %in% colnames(trees_data)) || !("Species" %in% colnames(trees_data))) {
  stop("The data must contain 'Species', 'Angle.degrees', and 'Distance.m' columns.")
}

# 
height_values <- mapply(TreeHeight, trees_data$Angle.degrees, trees_data$Distance.m)

# 
result_data <- cbind(trees_data, Tree.Height.m  = height_values)

# 
print(result_data)

# 
write.csv(result_data, "../results/trees_with_height.csv", row.names = FALSE)
