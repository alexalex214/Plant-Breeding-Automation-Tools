library(dplyr)
library(ggplot2)
library(rstatix)
library(GGally)
library(tidyverse)
library(emmeans)

#Creating a data frame
df <- data.frame(PlantID = factor(all_lines_roots$PlantID),
                 Condition = factor(all_lines_roots$Condition),
                 Day = factor(all_lines_roots$Day),
                 Line = factor(all_lines_roots$Line),
                 NRT = all_lines_roots$NRT,
                 NBP = all_lines_roots$NBP,
                 TRL = all_lines_roots$TRL,
                 BF = all_lines_roots$BF,
                 NAr = all_lines_roots$NAr,
                 AD = all_lines_roots$AD,
                 MedD = all_lines_roots$MedD,
                 Per = all_lines_roots$Per,
                 Vol = all_lines_roots$Vol,
                 SA = all_lines_roots$SA,
                 RLDR1 = all_lines_roots$RLDR1,
                 PADR1 = all_lines_roots$PADR1,
                 SADR1 = all_lines_roots$SADR1,
                 VolDR1 = all_lines_roots$VolDR1)

#Create a data frame with averages for all numeric parameters according to plantID
#This code results in a data frame with averages for each plant
df_plant <- df %>%
  group_by(Day, Line, Condition, PlantID) %>%
  summarise(
    across(where(is.numeric), \(x) mean(x, na.rm = TRUE)),
    .groups = "drop"
  )

#Making means and standard deviations for all lines
#Grouping for each line
df_mean <- df_plant %>%
  group_by(Day, Line, Condition) %>%
  summarise(
    across(
      where(is.numeric), 
      list(mean = \(x) mean(x, na.rm = TRUE), sd = \(x) sd(x, na.rm = TRUE)),
      .names = "{fn}_{col}"
    ),
    .groups = "drop"
  )

#Creates a matrix of scatterplots with GGally to pair each other 
#traits and conditions (columns)
plot_matrix <- ggpairs(df_plant,
                       aes(colour = Line, alpha = 0.4),
                       title = 'Pairs of traits and variables',
                       cardinality_threshold = NULL)
ggsave("Scatter_plot_matrix.png", 
       plot_matrix,
       width = 20,
       height = 20,
       dpi = 1000)

#Creates a plot with lines which corresponds 
#changes in variable e.g. root length
ggplot(df_mean,
       aes(x = Day,
           y = mean_TRL,
           group = interaction(Line, Condition),
           colour = Line,
           linetype = Condition)) +
  ylab("Total root length") +
  geom_point(size = 2) +
  geom_line() +
  geom_errorbar(aes(ymin = mean_TRL - sd_TRL,
                    ymax = mean_TRL + sd_TRL),
                width = 0.2) +
  facet_grid(.~Line)

#Creates QQ-plot for selected trait. Needs to change for the desired trait
ggplot(df_plant, aes(sample = SA, color = Line)) +
  ylab("Surface area") +
  stat_qq() +
  stat_qq_line() +
  facet_grid(.~Line)

#Creates a box plot for chosen data
ggplot(data = df_plant, aes(x = Day,
                            y = SA,
                            color = Line,)) +
  ylab("Surface area") +
  geom_boxplot() +
  facet_grid(.~Condition, labeller = labeller(Condition = c("0" = "Control", "1" = "Pi deficiency")))

#Shapiro test
shaptest <- sapply(df_plant[sapply(df_plant, is.numeric)],
              \(x) shapiro.test(x)$p.value)
print(shaptest)

#Three-way ANOVA
summary(aov(TRL ~ Line * Day * Condition, data = df_plant))

#Linear regression and plotting of residuals with predicted (fitted) values
#df_regression <- df_plant[df_plant$Line == "K3", ] #if need to compute by each line
m1421 <- lm(TRL ~ Condition * Line * Day, 
            data = df_plant)
summary(m1421)
#ANOVA of fixed effects
write.csv(anova(m1421), "anova output.csv")
#To plot fitted and residual values
plot(fitted(m1421), residuals(m1421))

#Calculation of effect size with rstatix package and visualization with ggplot
# 1. Calculation of effect size natively with rstatix
effsize_values_df <- df_plant %>% 
  pivot_longer(
    cols = where(is.numeric), 
    names_to = "Variable",
    values_to = "Value"
  ) %>% 
  # Group by both Line and Variable (pooling days together)
  group_by(Line, Day, Variable) %>% 
  wilcox_effsize(Value ~ Condition, paired = FALSE) %>% 
  ungroup() %>% 
  
  # 2. Format columns so they match your exact ggplot setup
  mutate(
    Comparison = paste(Variable, "vs Condition"),
    effsize = as.numeric(effsize) # Safely converted to numeric here
  )
print(effsize_values_df)

# 2. Visualization with ggplot for all data
ggplot(data = effsize_values_df, aes(x = Comparison, 
                                     y = effsize,
                                     color = Line)) +
  # Benchmark lines for interpretation (0.3 = Medium, 0.5 = Large)
  geom_hline(yintercept = 0.5, linetype = "dashed", color = "red", size = 0.8) +
  geom_hline(yintercept = 0.3, linetype = "dashed", color = "blue", size = 0.8) +
  geom_point(size = 6, alpha = 0.9) +
  labs(
    y = "Effect Size",
    x = "Trait Comparison"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

#To see whether lines show different reaction to Control and Pi conditions
#library(emmeans) was used. It shows performance and difference of lines
#over time under condition. It should be used together with linear regression
#emmeans() function shows general data
#pairs(emmeans()) presents comparison of lines over time (p-values for significance)
#plot(emmeans()) creates something similar to box plot for difference plotting
m1421 <- lm(TRL ~ Condition * Line * Day, 
            data = df_plant)
write.csv(pairs(emmeans(m1421, ~ Line | Day * Condition)), "emmeans paits output.csv")

plot(emmeans(m1421, ~ Line | Day * Condition))

emmeans(m1421, ~ Line | Day * Condition)

plot(m1421)

#PCA plot to understand input  of each component to variances with vegan package
PCAplot <- prcomp(df_plant %>% select(where(is.numeric)),
                  center = TRUE,
                  scale. = TRUE)

biplot(PCAplot)
summary(PCAplot)
PCAplot
