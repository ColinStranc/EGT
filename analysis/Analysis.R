# Read data
source(file.path("./read_egt.R"),chdir=F)
FileThreat03Trial01 <- read.egt("text")
DataThreat03Trial01 <- FileThreat03Trial01["results"]
RepsThreat03Trial01 <- FileThreat03Trial01["reps"]

# Created temporary dummy data to run analyses on
gens0302    <- c(1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
xs0302      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1, 2, 4, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
ys0302      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 4, 5, 3, 4, 5, 3, 5, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
cstrats0302 <- as.factor(c(1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1, 1, 2, 3, 2, 3, 2, 1))
pstrats0302 <- as.factor(c(3, 4, 3, 2, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 1, 2, 3, 4, 3, 2, 1, 3, 2, 3, 2, 1, 1, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 4, 2, 3, 2, 1, 2, 1, 2, 3))
results0302 <- data.frame(gens0302, xs0302, ys0302, cstrats0302, pstrats0302)
names(results0302) <- c("gens","xs","ys","cstrats","pstrats")
FileThreat03Trial02 <- list(results0302, 5, 5, 0, 0.1, 0.1)
names(FileThreat03Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
gens2501    <- c(1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
xs2501      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
ys2501      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
cstrats2501 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1, 1, 1))
pstrats2501 <- as.factor(c(4, 2, 2, 3, 4, 1, 1, 2, 3, 4, 2, 2, 3, 4, 1, 2, 1, 3, 2, 4, 3, 2, 2, 2, 2, 1, 4, 3, 3, 3, 1, 2, 2, 1, 1, 1, 3, 4, 3, 4, 3, 4, 3, 2, 1, 3, 1, 1, 1, 2, 2))
results2501 <- data.frame(gens2501, xs2501, ys2501, cstrats2501, pstrats2501)
names(results2501) <- c("gens","xs","ys","cstrats","pstrats")
FileThreat25Trial01 <- list(results2501, 5, 5, 0, 0.1, 0.1)
names(FileThreat25Trial01) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
gens2502    <- c(1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
xs2502      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
ys2502      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
cstrats2502 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1))
cstrats2502 <- as.factor(c(2, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 2, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 2, 2, 2, 1, 1, 2, 3))
pstrats2502 <- as.factor(c(2, 3, 4, 4, 4, 3, 2, 1, 2, 1, 3, 4, 1, 3, 1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 4, 3, 4, 3, 2, 1, 1, 3, 2, 4, 1, 3, 2, 1, 2, 3, 4, 3, 2, 2))
results2502 <- data.frame(gens2502, xs2502, ys2502, cstrats2502, pstrats2502)
names(results2502) <- c("gens","xs","ys","cstrats","pstrats")
FileThreat25Trial02 <- list(results2502, 5, 5, 0, 0.1, 0.1)
names(FileThreat25Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")

library(plyr)
library(data.table)
library(ggplot2)

DatasetsListThreat03 <- list(FileThreat03Trial01$results,FileThreat03Trial02$results)
DatasetsListThreat25 <- list(FileThreat25Trial01$results,FileThreat25Trial02$results)
ListOfThreats <- list(DatasetsListThreat03,DatasetsListThreat25)
ThreatLevelVector <- c(3,25)
LengthThreatLevelVector <- length(ThreatLevelVector)
ThreatLevelIndex <- c(1:LengthThreatLevelVector)

CStratFunction <- function(ThreatList,Levels){
  CStratThreatLevelAnalysis <- function(TrialList){
    CStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(cstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      levels(Counts[,1]) <- c("1","2","3","Contribute","Dissent","Opportunistic")
      Counts[,1][Counts[,1] == 1] <- "Contribute"
      Counts[,1][Counts[,1] == 2] <- "Dissent"
      Counts[,1][Counts[,1] == 3] <- "Opportunistic"
      names(Counts) <- c("Contribution_Strategy","Proportion")
      return(Counts)
    }
    AllTrialsDF <- rbindlist(lapply(TrialList,CStratProportionFunction))
    CStratSummaryFunction <- function(DF){
      Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
      return(Summary)
    }
    SummaryTable <- ddply(AllTrialsDF,.(Contribution_Strategy),CStratSummaryFunction)
    return(SummaryTable)
  }
  SummaryTableList <- lapply(ThreatList,CStratThreatLevelAnalysis)
  AddThreatLevel <- function(i){
    SummaryTable <- data.frame(SummaryTableList[[i]],Threat_Level = ThreatLevelList[[i]])
    return(SummaryTable)
  }
  SimulationDF <- rbindlist(lapply(Levels,AddThreatLevel))
  CStratPlot <- ggplot(data = SimulationDF, aes(x=Threat_Level, y=Proportion, group=Contribution_Strategy, colour=Contribution_Strategy)) + geom_line() + geom_point() + scale_x_continuous(breaks=seq(min(ThreatLevelList[[1]]),max(ThreatLevelList[[1]]), 20)) + geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05))
  return(CStratPlot)
}

PStratFunction <- function(ThreatList,Levels){
  PStratThreatLevelAnalysis <- function(TrialList){
    PStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(pstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      levels(Counts[,1]) <- c("1","2","3","4","Responsibly","Anti_Socially","Spitefully","Never")
      Counts[,1][Counts[,1] == 1] <- "Responsibly"
      Counts[,1][Counts[,1] == 2] <- "Anti_Socially"
      Counts[,1][Counts[,1] == 3] <- "Spitefully"
      Counts[,1][Counts[,1] == 4] <- "Never"
      names(Counts) <- c("Punishment_Strategy","Proportion")
      return(Counts)
    }
    AllTrialsDF <- rbindlist(lapply(TrialList,PStratProportionFunction))
    PStratSummaryFunction <- function(DF){
      Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
      return(Summary)
    }
    SummaryTable <- ddply(AllTrialsDF,.(Punishment_Strategy),PStratSummaryFunction)
    return(SummaryTable)
  }
  SummaryTableList <- lapply(ThreatList,PStratThreatLevelAnalysis)
  AddThreatLevel <- function(i){
    SummaryTable <- data.frame(SummaryTableList[[i]],Threat_Level = ThreatLevelVector[i])
    return(SummaryTable)
  }
  SimulationDF <- rbindlist(lapply(Levels,AddThreatLevel))
  PStratPlot <- ggplot(data = SimulationDF, aes(x=Threat_Level, y=Proportion, group=Punishment_Strategy, colour=Punishment_Strategy)) + geom_line() + geom_point() + scale_x_continuous(breaks=seq(min(ThreatLevelVector),max(ThreatLevelVector), 22)) + geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05))
  return(PStratPlot)
}

CStratFunction(ListOfThreats,ThreatLevelIndex)
PStratFunction(ListOfThreats,ThreatLevelIndex)
