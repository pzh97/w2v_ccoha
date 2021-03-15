#load required packages
library("dplyr")
library("ggpubr")
library("ggplot2")
library(moments)

#check the normality of continuous variables 
my_data <- read.csv(file.choose())
shapiro.test(my_data$frequency)
shapiro.test(my_data$polysemy)
head(my_data)

#plot the normality density
ggdensity(my_data$frequency, fill = "lightgray")
ggdensity(my_data$polysemy, fill = "lightgray")

#log transformation
my_data$frequency <- log10(my_data$frequency)
my_data$polysemy <- log10(my_data$polysemy)

#check normality after transformation
ggdensity(my_data, x = "frequency", fill = "lightgray", title = "FREQ") +
  stat_overlay_normal_density(color = "red", linetype = "dashed")
ggdensity(my_data, x = "polysemy", fill = "lightgray", title = "POLY") +
  stat_overlay_normal_density(color = "red", linetype = "dashed")
skewness(my_data$frequency, na.rm = TRUE)
skewness(my_data$polysemy, na.rm = TRUE)

#plot the normality density after log transformation
ggdensity(my_data$frequency, fill = "lightgray")
ggdensity(my_data$polysemy, fill = "lightgray")

#fit a binary logistic regression model
model1 <- glm(change ~ my_data$frequency + my_data$polysemy + technology, data = my_data, family = binomial())
summary(model1)