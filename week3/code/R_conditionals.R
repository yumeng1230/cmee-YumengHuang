######### Functions ##########

# Checks if an integer is even
is.even <- function(n = 2) {
  # Check for edge cases: NA or non-numeric inputs
  if (is.na(n) || !is.numeric(n)) {
    return("Input must be a numeric value!")
  }
  # Check if n is an integer
  if (n %% 1 != 0) {
    return("Input must be an integer!")
  }
  # Determine if n is even or odd
  if (n %% 2 == 0) {
    return(paste(n, "is even!"))
  } else {
    return(paste(n, "is odd!"))
  }
}
is.even(6) # Test with an even number

# Checks if a number is a power of 2
is.power2 <- function(n = 2) {
  # Check for edge cases: NA, non-numeric, or non-positive values
  if (is.na(n) || !is.numeric(n)) {
    return("Input must be a numeric value!")
  }
  if (n <= 0) {
    return("Input must be a positive number!")
  }
  # Determine if n is a power of 2
  if (log2(n) %% 1 == 0) {
    return(paste(n, "is a power of 2!"))
  } else {
    return(paste(n, "is not a power of 2!"))
  }
}
is.power2(4) # Test with a power of 2

# Checks if a number is prime
is.prime <- function(n) {
  # Check for edge cases: NA, non-numeric, or non-positive values
  if (is.na(n) || !is.numeric(n)) {
    return("Input must be a numeric value!")
  }
  if (n <= 0) {
    return("Input must be a positive integer!")
  }
  # Handle special cases for 0 and 1
  if (n == 0) {
    return(paste(n, "is zero!"))
  } else if (n == 1) {
    return(paste(n, "is just a unit!"))
  }
  # Check if n is divisible by any integer from 2 to (n-1)
  ints <- 2:(n - 1)
  if (all(n %% ints != 0)) {
    return(paste(n, "is a prime!"))
  } else {
    return(paste(n, "is a composite!"))
  }
}
is.prime(3) # Test with a prime number

######### Edge Case Examples ##########
is.even(NA) # Handle NA
is.power2(-8) # Handle negative numbers
is.prime("text") # Handle non-numeric inputs
