

# creating a table showing frequency that
# displays the distribution of the Tattoo variable
# by Illia Polishchuk
table(Course_Data_Set$Tatoos)

# creating a table showing percentages that
# displays the distribution of the Tattoo variable
# by Illia Polishchuk
table1 <- table(Course_Data_Set$Tatoos)
percent <- 100*table1/sum(table1)
percent

# Generating a pie chart to display the distribution 
# of the Tattoos variable (Illia Polishchuk)
pie(table(Course_Data_Set$Tatoos), col=rainbow(length(table(Course_Data_Set$Tatoos))),
    main="Pie Chart of Whether a Student has a Tattoo, created by Illia Polishchuk")

# Generating a histogram for the Current_credit_hrs variable,
# which measures the number of enrolled credits for each student
# in the Course Data Set (Illia Polishchuk)
hist(Course_Data_Set$Current_credit_hrs, main="Distribution of Credit Hours with 6 bins, created by Illia Polishchuk",
     xlab="Number of Course Credit Hours", right=FALSE, breaks=6, labels=TRUE, ylim=c(0,700))

# Generate side-by-side boxplots showing the distribution
# of student heights (the Height_Inches variable) for different
# groups of the Sex variable (Illia Polishchuk)
boxplot(Course_Data_Set$Height_inches ~ Course_Data_Set$Sex, 
        main="Distribution of Height by Gender Categories, created by Illia Polishchuk",
        xlab="Sex", ylab="Height in inches", ylim=c(55,80), col="green3")


# Using the probability distribution creating a table summarizing 
# the probability distribution of X (Illia Polishchuk)
x_values <- c(2,4,6,8,10)
x_probs <- (15-x_values)/45
x_table1 <- data.frame(x_values, x_probs)
names(x_table1) <- c("x", "P(X=x)")
x_table1


# Providing the percentile of the 660 SAT score (Illia Polishchuk)
round(100*pnorm(660, mean=525, sd=119, lower.tail=TRUE), 0)
round(100*pnorm(470, mean=525, sd=119, lower.tail=TRUE), 0)
pnorm(-0.28, lower.tail=FALSE)







