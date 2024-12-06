# Clear the current R environment
rm(list = ls())

# Load the dataset containing Key West annual mean temperatures
load("../data/KeyWestAnnualMeanTemperature.RData")

# Check the class and preview the dataset
cat("Loaded variables:", ls(), "\n")
cat("Class of the data object:", class(ats), "\n")
cat("First few rows of data:\n")
print(head(ats))

# Define a function to calculate the observed correlation coefficient
get_observed_correlation <- function(data) {
  cor(data$Year, data$Temp)
}

# Compute the observed correlation coefficient
observed_correlation <- get_observed_correlation(ats)
cat("Observed correlation coefficient:", observed_correlation, "\n")

# Define a function for the randomization test
perform_randomization_test <- function(data, num_permutations = 10000, seed = 123) {
  set.seed(seed)  # Ensure reproducibility
  replicate(num_permutations, cor(data$Year, sample(data$Temp)))
}

# Perform the randomization test
num_permutations <- 10000
random_coefficients <- perform_randomization_test(ats, num_permutations)

# Compute summary statistics for the null distribution
null_mean <- mean(random_coefficients)
null_sd <- sd(random_coefficients)
cat("Mean of null distribution:", null_mean, "\n")
cat("Standard deviation of null distribution:", null_sd, "\n")

# Save the histogram plot as a PNG image in the ../results directory
png("../results/Null_Distribution_Histogram.png", width = 800, height = 600)

# Create the histogram plot
hist(
  random_coefficients,
  breaks = 30,
  main = "Null Distribution of Correlation Coefficients",
  xlab = "Correlation Coefficient",
  col = "skyblue",
  border = "white",
  ylim = c(0, max(table(cut(random_coefficients, breaks = 30))) + 50),
  xlim =  c(-0.4, 0.8)    # Ensure both ranges are covered
)

# Add observed and null mean lines
abline(v = null_mean, col = "blue", lwd = 2, lty = 2)  # Null mean (dashed blue)
abline(v = observed_correlation, col = "red", lwd = 2)  # Observed (solid red)

# Add a legend
legend(
  "topright",
  legend = c("Observed Correlation", "Null Mean"),
  col = c("red", "blue"),
  lwd = 2,
  lty = c(1, 2),
  box.lty = 0,
  cex = 0.7
)

# Add a grid for better readability
grid(nx = NULL, ny = NULL, col = "gray", lty = "dotted")

# Close the device to save the file
dev.off()

# Summarize results
cat("Results Summary:\n")
cat("- Observed correlation coefficient:", observed_correlation, "\n")
cat("- Mean of null distribution:", null_mean, "\n")
cat("- Standard deviation of null distribution:", null_sd, "\n")

# Confirm the image has been saved
cat("Histogram saved to ../results/Null_Distribution_Histogram.png\n")

