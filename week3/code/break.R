i <- 0 # Initialize the counter variable i
while (i < Inf) { # Infinite loop condition (runs indefinitely unless a break condition is met)
    if (i == 10) { # Check if i has reached 10
        break # Exit the while loop if i equals 10
    } else { # If i is not equal to 10
        cat("i equals", i, "\n") # Print the current value of i
        i <- i + 1 # Increment i by 1
    }
}
