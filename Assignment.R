#1. Write a code to print sequence of number from 1 to 50 with the differences of 3,5,10
 

s3<-seq(1,50,3)        #with difference of 10
print(s3)

s5<-seq(1,50,5)
s4

s10<- seq(1,50,10)
s10

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#2. What are different data objects in R? Write syntax and example for every object.
#1. Vectors -Vector can store combination of multiple values
v=c(12,4.6,"rashmi",23L,-4,-8.99)
print(v)
class(v)


#2. List - 
Student <- list(Id=c(1,2,3,4), names=c("rash","Ranj","barth","Ball"), marks=c(50,52,63,45))
print(Student)

#3. Matrices
# Syntax --- matrix(data, nrow, ncol, byrow, dimnames) 
p = matrix(c(3:14),nrow = 4, byrow = T)

print(p)


#5. Factors 
#syntax factor()
data=c("red","red","green","yellow","green","Red","green","Yellow")

factor_data=factor(data)

print(factor_data)


#6. Data Frames
students=data.frame(Id=c(1,2,3,4),name=c('Kamal','Kalyan','Kanishk','Komal'),marks=c(95,85,75,85))
students

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#3. Create data frame with 3 columns and 5 rows write a code to fetch and delete row 
#and column using index and add row to the existed data frame.

df=data.frame(stud_ID=c('M1','M2','M3','M4','M5'),
              stud_name=c("Rashmi", "Ranjana","Bharath","Bahubali","Keerthi"), 
              stud_marks=c(85,75,65,85,50))

print(df)

df[c(2,3),]  #Fetching 2 rows and 3rd row of all columns
df[c(3,5),]
df[2,3]
df[-c(2),]      #Delete 2ed row from the data frame
df[-c(3)]       #Delete 3rd column (Stud_marks)

x1=c("M6","ranj",20)

y=rbind(df,x1)
y


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  
  
#4. Write a nested if else statement to print whether the given number is positive,
#Negative or Zero.

x <- 1

if(x==0){
  print("Zero")
} else if(x>0){
  print("Positive Number")
} else{
  print("Negative Number")
}


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#5. Write a program to input any value and check whether it is character or numeric


a<- readline(prompt = "Please Enter any value: ")

class(a)
is.numeric(a)
is.character(a)

x=45
is.numeric(x)
is.character(x)


#***********************************************************************************************

#6. write difference between break and next and write program for each.


#Break -Break is used inside the loop to Stop the iteration and flow the control outside of the loop

x <- 1:5
for (val in x) {
  if (val == 3){
    break
  }
  print(val)
}

#Next -Next statement is used when we want to skip the current iteration of a loop without terminating it

x <- 1:5
for (val in x) {
  if (val == 3){         #If val==3 skips the execution, jump to the next
    next
  }
  print(val)
}


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#7. Write a program to print given vector in reverse format
x=c(1,5.6,3,10,3.5,5)


x = c(1,5.6,3,10,3.5,5)
print("Original vector-1:")
print(x)
rv = rev(x)
print("The said vector in reverse order:")
print(rv)



#*********************************************************************************************

#8. Write a program to get a mode value of given vector ('a','b','c','t','a','c','r','a','c','t','z','r','v','t','u','e','t')

v<- c('a','b','c','t','a','c','r','a','c','t','z','r','v','t','u','e','t')

getmode<- function(v){
  uniqv<- unique(v)
  uniqv[which.max(tabulate(match(v,uniqv)))]
  
}
v<- c('a','b','c','t','a','c','r','a','c','t','z','r','v','t','u','e','t')

  
result<- getmode(v)
print(result)



#*******************************************************************************************
#9. Write a program to filter only data belongs to 'setosa' in species of Iris data set using dplyr function

install.packages('dplyr')
library(dplyr)

data("iris")
View(iris)
head(iris,50)

iris[,c(1,5)]   #extract all rows of 2 and 5th column
iris[,c(2:5)]   #extract all rows(columns from 2nd(2,3,4,5) to 5th) 
filter(iris, Species=='setosa')
filter(iris, Sepal.Length==5.4| Petal.Length==1.7, Species=='setosa')
filter(iris, Sepal.Width==3.7 & Sepal.Length==5.3, Species=='setosa')


sel<- select(iris, Petal.Length, Petal.Width)
sel

arrange(iris,Petal.Length)
arrange(select(iris,"Petal.Length","Petal.Width"),Petal.Length)

filter(arrange(iris,Sepal.Length), Species=='setosa')
      


#10. Create a new column for Iris data set with the name of means_of_obs, 
#which contains mean value of each row. (using dplyr package)

data("iris")
View(iris)

iris[c(1,50),]
head(iris,50)

mean(iris$Petal.Length, na.rm=T)  #mean of column Petal.Length

#******************
#*
#Mean of each row of iris data set

iris_subset <- iris[,-5]   #removes 5th column and store in iris_subset
iris_subset 
dim(iris_subset) 

iris_subset$mean_of_Obs<- apply(iris_subset, 1, mean)
head(iris_subset)
iris_subset

#11.  Filter data for the 'Versicolor' and 
#get only  'Sepal.length' and 'Sepal.width' columns (Using dplyr package)

data(iris)
View(iris)
library(dplyr)


filter(iris, Species=='versicolor')

select(iris,Sepal.Length,Sepal.Width)
filter(select(iris, Sepal.Length, Sepal.Width),Species=='Versicolor')

#*******************************************************************************
#*12. Create a below plots for mtcars also write your inference for each andevery plot (use ggplot package) Use different size, color
#*Scatter plot
#*Box plot
#*Histogram
#*Line graph
#*Bar graph

install.packages(gglpot)
library(ggplot2)
data(mtcars)    
View(mtcars)

#*Bar graph
p<-ggplot(mtcars, aes(x=cyl, y=mpg)) +
  geom_bar(stat="identity",width=0.5, color="white",fill="blue")+
  theme_minimal()
p


#*Box plot

boxplot(mtcars$disp,
        main = "hp-cyl",
        xlab = "disp",
        ylab = "mpg",
        col = "orange",
        border = "brown",
        horizontal = TRUE,
        notch = TRUE
)

#*Histogram
ggplot(mtcars, aes(x=hp, color=qsec)) +
geom_histogram(fill="green", alpha=0.5, position="dodge")


#*Line graph
ggplot(mtcars, aes(x=hp, y=mpg, group=1)) +
  geom_line(linetype = "dashed")+
  geom_line(color="purple")+
  geom_point()

