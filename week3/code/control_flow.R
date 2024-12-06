#if statements
a <- TRUE
if (a == TRUE) {
  print ("a is TRUE")
} else {
  print ("a is FALSE")
}

#write an if statement on a single line
z <- runif(1) ## Generate a uniformly distributed random number
if (z <= 0.5) {print ("Less than a half")}

#much readable
z <- runif(1)

if (z <= 0.5) {
  
  print ("Less than a half")
  
}

