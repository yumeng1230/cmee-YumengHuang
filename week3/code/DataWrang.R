
#load PoundHillMetaData.csv
MyMetaData <- read.csv("../data/PoundHillMetaData.csv",header = TRUE,  sep=";")
class(MyMetaData)

#Loading the data as.matrix(), and setting header=FALSE guarantees that the data are imported “as is” so that you can wrangle them. 
MyData <- as.matrix(read.csv("../data/PoundHillData.csv",header = FALSE))
class(MyData)

#check out what the data look like
head(MyData)

#replace blanks cells with zeros
MyData[MyData == ""] = 0
#transpose the data, because for a long format, the (nested) treatments variables should be in rows
MyData <- t(MyData) 
head(MyData)
#check the first row
colnames(MyData)
#create a temporary dataframe with just the data, without the column names
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F)
head(TempData)
#assign the original column names to the temporary dataset
colnames(TempData) <- MyData[1,] # assign column names from original data
head(TempData)
#get rid of row names
rownames(TempData) <- NULL
head(TempData)

#convert the data to long format(need the reshape2 package)
require(reshape2) #load the reshape2 package
MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
head(MyWrangledData); tail(MyWrangledData)

#assign the correct data types to each column
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
str(MyWrangledData)

#
require(tidyverse)
tidyverse_packages(include_self = TRUE) # the include_self = TRUE means list "tidyverse" as well 

#convert the dataframe to a “tibble”
MyWrangledData <- dplyr::as_tibble(MyWrangledData) 
MyWrangledData
#the same as
MyWrangledData <- as_tibble(MyWrangledData) 

class(MyWrangledData)

#without using ::
glimpse(MyWrangledData) #like str(), but nicer!
filter(MyWrangledData, Count>100) #like subset(), but nicer!

slice(MyWrangledData, 10:15) # Look at a particular range of data rows

# use the “pipe” %>% operator to create a compact sequence of manipulations of your dataset with dplyr
MyWrangledData %>%
  group_by(Species) %>%
  summarise(avg = mean(Count))

#the same as (not using dplyr at all)
aggregate(MyWrangledData$Count, list(MyWrangledData$Species), FUN=mean) 

