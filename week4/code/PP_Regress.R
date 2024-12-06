# Clear the workspace
rm(list = ls())

# Install and load necessary libraries
required_packages <- c("ggplot2", "dplyr")
for (pkg in required_packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) install.packages(pkg)
  library(pkg, character.only = TRUE)
}

# Check if input data file exists
if (!file.exists("../data/EcolArchives-E089-51-D1.csv")) {
  stop("The data file '../data/EcolArchives-E089-51-D1.csv' does not exist. Please check the file path.")
}

# Load the data
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")

# Create a PDF to save the plot
pdf("../results/PP_Regress.pdf", width = 6, height = 12)

# Generate a predator-prey mass plot grouped by feeding type and predator lifestage
ggplot(MyDF, aes(x = Prey.mass, y = Predator.mass, color = Predator.lifestage)) +
  geom_point(shape = 3) +
  geom_smooth(method = "lm", formula = y ~ x, fullrange = TRUE, na.rm = TRUE) +
  scale_x_log10() +
  scale_y_log10() +
  xlab("Prey mass in grams") +
  ylab("Predator mass in grams") +
  facet_grid(Type.of.feeding.interaction ~ .) +
  theme_bw() +
  theme(legend.position = "bottom",
        panel.border = element_rect(colour = "grey", fill = NA),
        legend.title = element_text(size = 9, face = "bold")) +
  guides(colour = guide_legend(nrow = 1)) %>% print()

# Close the PDF device
dev.off()

# Filter and group data, then calculate regression results
if (!dir.exists("../results")) dir.create("../results") # Ensure output directory exists
LM <- MyDF %>%
  filter(!Record.number %in% c("30914", "30929")) %>%
  select(Record.number, Predator.mass, Prey.mass, Predator.lifestage, Type.of.feeding.interaction) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
  do(mod = lm(Predator.mass ~ Prey.mass, data = .)) %>%
  mutate(
    Regression.slope = summary(mod)$coefficients[2, 1],
    Regression.intercept = summary(mod)$coefficients[1, 1],
    R.squared = summary(mod)$adj.r.squared,
    Fstatistic = summary(mod)$fstatistic[1],
    P.value = summary(mod)$coefficients[2, 4]
  ) %>%
  select(-mod)

# Save regression results to a CSV file
write.csv(LM, "../results/PP_Regress_Results.csv", row.names = FALSE)


