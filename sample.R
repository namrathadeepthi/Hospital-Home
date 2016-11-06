#sayHello <- function(){
#  print('hello')
#}

#sayHello()
#Set the current Working Directory

setwd("/home/admin-pc/Hospital-Home");
#Load the training data
train<-read.csv("heartdisease.csv",header=FALSE,stringsAsFactors = FALSE);
library(randomForest)
library(rpart)
#Build the model
names<-c("age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","num")
colnames(train)<-names
train$num[train$num>0]<-1
#train$thal[train$thal=='?']<-99
train$ca[train$ca=='?']<-99
set.seed(123)
forest<-randomForest(as.factor(num)~.,data=train,importance=TRUE,ntree=1)
#tree<-rpart(num~.,data=train,method="class")
#plot(forest)
#Load the test data
test<-read.csv("testHeart.csv",header=FALSE,stringsAsFactors = FALSE)
names2<-c("age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca")
colnames(test)<-names2
test$ca[test$ca=='?']<-99
#test$ca[test$ca=='?']<-99
#library(RColorBrewer)
#library(rpart.plot)
#fancyRpartPlot(tree)
#varImpPlot(forest)
#levels(test)<-levels(train)
#Use the model for predicting test data
my_prediction<-predict(forest,test,type="class")
#my_prediction<-predict(tree,test)
#print (my_prediction)
answer<-data.frame(Output=my_prediction)
#answer
#table(answer$num,answer$Output)
x=ifelse(my_prediction==0,"No","Yes")
print(x)

#write.csv(x,file="solution.csv",row.names=FALSE)
