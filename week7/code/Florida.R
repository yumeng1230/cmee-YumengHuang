# Clear the current R environment
rm(list = ls())

# Load the dataset containing Key West annual mean temperatures
load("../data/KeyWestAnnualMeanTemperature.RData")

# Check the variables loaded into the environment
ls()

# Check the class of the main data object and preview its content
class(ats)
head(ats)

# Plot the dataset to visualize trends or patterns
plot(ats)

# Calculate the observed correlation coefficient between Year and Temp
observed_correlation <- cor(ats$Year, ats$Temp)

# Print the observed correlation coefficient
print(observed_correlation)

# Set the number of permutations for the randomization test
num_permutations <- 10000

# Generate randomized correlation coefficients using replicate
set.seed(123)  # Set a seed for reproducibility
random_coefficients <- replicate(num_permutations, cor(ats$Year, sample(ats$Temp)))

# Print the first 10 random correlation coefficients to verify results
print(head(random_coefficients, 10))

# Create a histogram of the random correlation coefficients
hist(
  random_coefficients,                           # Data to plot
  breaks = 30,                            # Number of bins
  main = "Null Distribution of Correlation Coefficients",  # Title
  xlab = "Correlation Coefficient",       # X-axis label
  col = "skyblue",                        # Bar color
  border = "white",                       # Border color
  ylim = c(0, 800),                       # Y-axis limits
  xlim = c(-0.4, 0.8)                     # X-axis limits
)

# Calculate the mean and standard deviation of the null distribution
null_mean <- mean(random_coefficients)
null_sd <- sd(random_coefficients)

# Add a blue vertical dashed line for the mean of the null distribution
abline(v = null_mean, col = "blue", lwd = 2, lty = 2)

# Add a red vertical line for the observed correlation coefficient
abline(v = observed_correlation, col = "red", lwd = 2)

# Add a legend to explain the lines in the plot
legend(
  x = 0.55, y = 800,                       # Position of the legend
  legend = c("Observed Correlation", "Null Mean"),  # Labels
  col = c("red", "blue"),                 # Colors of the lines
  lwd = 2,                               # Line widths
  lty = c(1, 2),                         # Line types (solid and dashed)
  box.lty = 0,                           # Remove the box around the legend
  cex = 0.6                            # Text size of the legend
)

# Add a grid to the plot for better readability
grid(nx = NULL, ny = NULL, col = "gray", lty = "dotted")

# Print key statistics
cat("Observed correlation coefficient:", observed_correlation, "\n")
cat("Mean of null distribution:", null_mean, "\n")
cat("Standard deviation of null distribution:", null_sd, "\n")

    