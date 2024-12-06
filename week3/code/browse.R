Exponential <- function(N0 = 1, r = 1, generations = 10) {
  # Runs a simulation of exponential growth
  # N0: Initial population size (default = 1)
  # r: Growth rate (default = 1)
  # generations: Number of generations to simulate (default = 10)
  # Returns a vector of population sizes over the generations
  
  N <- rep(NA, generations)    # Initialize a vector of NA with length 'generations'
  
  N[1] <- N0                   # Set the initial population size
  for (t in 2:generations) {   # Loop through generations, starting from the second
    N[t] <- N[t-1] * exp(r)    # Calculate population size for generation t
    # browser()                # Debugging tool: Uncomment for sandbox or debugging purposes
  }
  return(N)                    # Return the vector of population sizes
}

# Plot the result of exponential growth simulation
plot(Exponential(), type = "l", main = "Exponential Growth", 
     xlab = "Generations", ylab = "Population Size")
