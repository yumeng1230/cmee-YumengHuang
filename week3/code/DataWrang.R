
MyMetaData <- read.csv("../data/PoundHillMetaData.csv",header = TRUE,  sep=";")
class(MyMetaData)
MyData <- as.matrix(read.csv("../data/PoundHillData.csv",header = FALSE))
class(MyData)

head(MyData)
MyData[MyData == ""] = 0
MyData <- t(MyData) 
head(MyData)
colnames(MyData)
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F)
head(TempData)
colnames(TempData) <- MyData[1,] # assign column names from original data
head(TempData)
rownames(TempData) <- NULL
head(TempData)

require(reshape2)
MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
head(MyWrangledData); tail(MyWrangledData)

MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
str(MyWrangledData)



