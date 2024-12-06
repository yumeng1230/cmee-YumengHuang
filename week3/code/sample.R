######### Functions ##########

## A function to take a sample of size n from a population "popn" and return its mean
myexperiment <- function(popn, n) {
    pop_sample <- sample(popn, n, replace = FALSE) # Take a sample of size n without replacement
    return(mean(pop_sample)) # Return the mean of the sampled values
}

## Calculate means using a FOR loop on a vector without preallocation
loopy_sample1 <- function(popn, n, num) {
    result1 <- vector() # Initialize an empty vector (no preallocation)
    for(i in 1:num) {
        result1 <- c(result1, myexperiment(popn, n)) # Append each result dynamically
    }
    return(result1) # Return the vector of means
}

## To run "num" iterations using a FOR loop on a vector with preallocation
loopy_sample2 <- function(popn, n, num) {
    result2 <- vector(, num) # Preallocate a vector of size num
    for(i in 1:num) {
        result2[i] <- myexperiment(popn, n) # Store results in preallocated slots
    }
    return(result2) # Return the vector of means
}

## To run "num" iterations using a FOR loop on a list with preallocation
loopy_sample3 <- function(popn, n, num) {
    result3 <- vector("list", num) # Preallocate a list of size num
    for(i in 1:num) {
        result3[[i]] <- myexperiment(popn, n) # Store each result in a list element
    }
    return(result3) # Return the list of means
}

## To run "num" iterations using vectorization with lapply
lapply_sample <- function(popn, n, num) {
    result4 <- lapply(1:num, function(i) myexperiment(popn, n)) # Use lapply to iterate efficiently
    return(result4) # Return the list of means
}

## To run "num" iterations using vectorization with sapply
sapply_sample <- function(popn, n, num) {
    result5 <- sapply(1:num, function(i) myexperiment(popn, n)) # Use sapply for simplified output
    return(result5) # Return a simplified vector of means
}

# Generate the population and visualize it
set.seed(12345) # Set seed for reproducibility
popn <- rnorm(10000) # Generate a population of 10,000 random normal values
hist(popn) # Plot the histogram to show population distribution

# Define parameters for the experiment
n <- 100 # Sample size for each experiment
num <- 10000 # Number of iterations (repeats)

# Run and time the different methods

print("Using loops without preallocation on a vector took:")
print(system.time(loopy_sample1(popn, n, num))) # Test and time loopy_sample1

print("Using loops with preallocation on a vector took:")
print(system.time(loopy_sample2(popn, n, num))) # Test and time loopy_sample2

print("Using loops with preallocation on a list took:")
print(system.time(loopy_sample3(popn, n, num))) # Test and time loopy_sample3

print("Using the vectorized sapply function (on a list) took:")
print(system.time(sapply_sample(popn, n, num))) # Test and time sapply_sample

print("Using the vectorized lapply function (on a list) took:")
print(system.time(lapply_sample(popn, n, num))) # Test and time lapply_sample
