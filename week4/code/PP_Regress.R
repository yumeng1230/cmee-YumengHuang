# Clear the workspace
rm(list = ls())

# Install and load required packages
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr")
library(ggplot2); library(dplyr)

# Load data and convert Prey.mass from mg to g if needed
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv") %>%
  mutate(Prey.mass = ifelse(Prey.mass.unit == "mg", Prey.mass / 1000, Prey.mass),
         Prey.mass.unit = "g")

# Save plot as PDF
pdf("../results/PP_Regress.pdf", width = 9, height = 12)
ggplot(MyDF, aes(x = Prey.mass, y = Predator.mass, color = Predator.lifestage)) +
  geom_point(shape = 3) + geom_smooth(method = "lm", formula = y ~ x, fullrange = TRUE, na.rm = TRUE) +
  scale_x_log10() + scale_y_log10() +
  xlab("Prey mass (g)") + ylab("Predator mass (g)") +
  facet_grid(Type.of.feeding.interaction ~ .) +
  theme_bw() + theme(legend.position = "bottom",
                     panel.border = element_rect(colour = "grey", fill = NA),
                     legend.title = element_text(size = 9, face = "bold")) +
  guides(colour = guide_legend(nrow = 1)) %>% print()
dev.off()

# Compute regression results for each feeding type and predator lifestage
LM <- MyDF %>%
  filter(!Record.number %in% c("30914", "30929")) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
  summarize(
    Regression.slope = coef(lm(Predator.mass ~ Prey.mass, data = .))[2],
    Regression.intercept = coef(lm(Predator.mass ~ Prey.mass, data = .))[1],
    R.squared = summary(lm(Predator.mass ~ Prey.mass, data = .))$adj.r.squared,
    Fstatistic = summary(lm(Predator.mass ~ Prey.mass, data = .))$fstatistic[1],
    P.value = summary(lm(Predator.mass ~ Prey.mass, data = .))$coefficients[2, 4]
  )

# Save regression results to CSV
write.csv(LM, "../results/PP_Regress_Results.csv", row.names = FALSE)

