# Define a function 'doit' to sample data and calculate its mean
doit <- function(x) {
  # Generate a bootstrap sample from x with replacement
  temp_x <- sample(x, replace = TRUE)
  
  # Check if the sample has more than 30 unique values
  if(length(unique(temp_x)) > 30) { # Only calculate the mean if the sample is diverse enough
    print(paste("Mean of this sample was:", as.character(mean(temp_x))))
  } else {
    # Stop execution with an error message if the sample has too few unique values
    stop("Couldn't calculate mean: too few unique values!")
  }
}

# Set seed for reproducibility
set.seed(1345) # Ensures the random number generation is consistent for demonstration purposes

# Generate a population of 50 normally distributed random values
popn <- rnorm(50)

# Visualize the population distribution with a histogram
hist(popn)

# Use lapply to repeatedly apply the 'doit' function and handle errors with try()
result <- lapply(1:15, function(i) try(doit(popn), FALSE))

# Check the class of the 'result' object, which should be a list
class(result)

# View the result, including successful outputs and error messages
result

# Preallocate a list to store results for improved efficiency
result <- vector("list", 15) # Initialize an empty list with a fixed length of 15

# Use a for loop to apply the 'doit' function and store each result in the list
for(i in 1:15) {
  # Apply 'doit' to the population and handle potential errors with try()
  result[[i]] <- try(doit(popn), FALSE)
}

# The 'result' list now contains outputs for all 15 iterations, 
# with either successful results or error messages for each attempt.
