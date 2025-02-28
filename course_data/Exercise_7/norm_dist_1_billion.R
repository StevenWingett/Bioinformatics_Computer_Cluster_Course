# Set seed for reproducibility
set.seed(123)

# Generate 1 billion normally distributed data points
data <- rnorm(1000000000, mean = 7, sd = 1)

# Open a PNG device to save the plot
png("normal_distribution_histogram.png", width = 800, height = 600)

# Plot histogram
hist(data, breaks = 50, col = "skyblue", main = "Histogram of Normally Distributed Data", 
     xlab = "Value", ylab = "Frequency")

# Close the PNG device (this writes the plot to the file)
dev.off()
