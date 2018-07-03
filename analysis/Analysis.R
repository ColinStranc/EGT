# Read data
source(file.path("./read_egt.R"),chdir=F)
FileThreat03Trail01 <- read.egt("text")
DataThreat03Trail01 <- FileThreat03Trail01["results"]
RepsThreat03Trail01 <- FileThreat03Trail01["reps"]

#Subset data to the final generation of the simulation
DataThreat03Trail01FinalGen <- subset(DataThreat03Trail01$results,gens == RepsThreat03Trail01)

#Count the number of each contribution strategy into a vector.
CStratCountThreat03Trail01FinalGen <- c(nrow(subset(DataThreat03Trail01FinalGen,cstrats == 1)),nrow(subset(DataThreat03Trail01FinalGen,cstrats == 2)),nrow(subset(DataThreat03Trail01FinalGen,cstrats == 3)))

#Count the number of each punishment strategy into a vector.
PStratCountThreat03Trail01FinalGen <- c(nrow(subset(DataThreat03Trail01FinalGen,pstrats == 1)),nrow(subset(DataThreat03Trail01FinalGen,pstrats == 2)),nrow(subset(DataThreat03Trail01FinalGen,pstrats == 3)),nrow(subset(DataThreat03Trail01FinalGen,pstrats == 4)))


CStratCountThreat03Trail01FinalGen
PStratCountThreat03Trail01FinalGen

