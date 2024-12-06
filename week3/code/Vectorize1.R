# Generate a large 1000x1000 matrix with random values
M <- matrix(runif(1000000), 1000, 1000)

# Define a function to sum all elements of a matrix using nested loops
SumAllElements <- function(M) {
  Dimensions <- dim(M) # Get the dimensions of the matrix (number of rows and columns)
  Tot <- 0 # Initialize the total sum to 0
  for (i in 1:Dimensions[1]) { # Loop through each row
    for (j in 1:Dimensions[2]) { # Loop through each column
      Tot <- Tot + M[i, j] # Add the value of the current element to the total
    }
  }
  return(Tot) # Return the total sum
}

# Measure the time taken to sum all elements using nested loops
print("Using loops, the time taken is:")
print(system.time(SumAllElements(M)))

# Measure the time taken to sum all elements using the in-built vectorized function
print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M))) # The sum() function is optimized for fast execution

