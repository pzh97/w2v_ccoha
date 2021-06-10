#load required packages
library("dplyr")
library("ggpubr")
library("ggplot2")
library("moments")

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

#check normality after transformation
skewness(my_data$frequency, na.rm = TRUE)

#plot normality after transformation
ggdensity(my_data, x = "frequency", fill = "lightgray", title = "FREQ") +
  stat_overlay_normal_density(color = "red", linetype = "dashed")

#fit a binary logistic regression model
model1 <- glm(change ~ my_data$frequency + my_data$polysemy + technology, data = my_data, family = binomial())
summary(model1)

#goodness-of-fit
model2 <- glm(change ~  pos, data = my_data, family = binomial())
model3 <- glm(change ~ technology + pos, data = my_data, family = binomial())
model4 <- glm(change ~ polysemy+technology + pos, data = my_data, family = binomial())
a<-model3$deviance-model4$deviance
b<-model3$df.residua-model4$df.residual
chisq.prob<-1-pchisq(a,b)
chisq.prob
a
b
