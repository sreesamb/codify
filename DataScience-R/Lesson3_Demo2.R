#Lesson 3 - Demo 2

BankCustomer <- read.csv("Datasets/Lesson 3_Data Structures/Demo 2_ Assigning values and applying functions.csv")
View(BankCustomer)

install.packages("plyr")
library(plyr)

BankCustomer <- rename(BankCustomer, c("i..age" = "Age"))
str(BankCustomer)
View(BankCustomer)


max(BankCustomer$age)
min(BankCustomer$age)

BankCustomerAgeCategorized <- transform(BankCustomer, Generation = ifelse(age<22,"Z", ifelse(age<41, "Y", ifelse(age<53, "X", "Baby Bommers"))))
BankCustomerAgeCategorized

#2 Way frequency table
table(BankCustomerAgeCategorized$Generation, BankCustomerAgeCategorized$poutcome)

counts <- table(BankCustomerAgeCategorized$Generation,BankCustomer$education)
barplot(counts, main = "Bank Customers by Education and Generation", xlab = "Education", col =c("grey","cornflowerblue"), legend = rownames(counts))
barplot(counts, main = "Bank Customers by Education and Generation", xlab = "Education", col =c("grey","cornflowerblue"), legend = rownames(counts))

boxplot(BankCustomer$age,main="Mean of Generation",xlab="age",ylab="test",horizontal=TRUE)
