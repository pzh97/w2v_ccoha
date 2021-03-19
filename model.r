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
my_data$polysemy <- log10(my_data$polysemy)

#check normality after transformation
skewness(my_data$frequency, na.rm = TRUE)
skewness(my_data$polysemy, na.rm = TRUE)

#plot normality after transformation
ggdensity(my_data, x = "frequency", fill = "lightgray", title = "FREQ") +
  stat_overlay_normal_density(color = "red", linetype = "dashed")
ggdensity(my_data, x = "polysemy", fill = "lightgray", title = "POLY") +
  stat_overlay_normal_density(color = "red", linetype = "dashed")

#fit a binary logistic regression model
model1 <- glm(change ~ my_data$frequency + my_data$polysemy + technology, data = my_data, family = binomial())
summary(model1)

###################################################################################################################
#ctree: run separately!
library("party")
library("plyr")
library("readr")

mydata <- read_csv("untitled copy.csv", col_names = FALSE)
mydata<-rename(mydata, c("X1"="mydata.change", "X2"="mydata.frequency", "X3"="mydata.polysemy", "X4"="mydata.technology"))
mydata$mydata.change<-as.factor(mydata$mydata.change) 
mydata$mydata.frequency<-as.factor(mydata$mydata.frequency) 
mydata$mydata.polysemy<-as.factor(mydata$mydata.polysemy) 
mydata$mydata.technology<-as.factor(mydata$mydata.technology) 
summary(mydata)
tree<-ctree(mydata.change~mydata.frequency + mydata.polysemy + mydata.technology, data=mydata)
plot(tree)
####################################################################################################################
#correlation test
library(Hmisc)

mydata<-read.csv(file.choose())
mydata<-mydata[, c(2,3,4)]
head(mydata, 6)
res<-rcorr(as.matrix(mydata))
####################################################################################################################
res
