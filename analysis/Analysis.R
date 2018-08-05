# Read data
source(file.path("./read_egt.R"),chdir=F)
FileThreat03Trail01 <- read.egt("text")
DataThreat03Trail01 <- FileThreat03Trail01["results"]
RepsThreat03Trail01 <- FileThreat03Trail01["reps"]

library(plyr)
library(data.table)
library(ggplot2)

DatasetsListThreat05 <- list(DataThreat05Trial01,DataThreat05Trial02)
DatasetsListThreat25 <- list(DataThreat25Trial01,DataThreat25Trial02)
ListOfThreats <- list(DatasetsListThreat05,DatasetsListThreat25)
ThreatLevelList <- list(5,25)
LengthThreatLevelList <- length(ThreatLevelList)
ThreatLevelIndex <- c(1:LengthThreatLevelList)

CStratFunction <- function(ThreatList,Levels){
  CStratThreatLevelAnalysis <- function(TrialList){
    CStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(cstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      Counts[,1][Counts[,1] == 1] <- "Contribute"
      Counts[,1][Counts[,1] == 2] <- "Dissent"
      Counts[,1][Counts[,1] == 3] <- "Opportunistic"
      names(Counts) <- c("Contribution_Strategy","Proportion")
      return(Counts)
    }
    AllTrialsList <- lapply(TrialList,CStratProportionFunction)
    AllTrialsDF <- rbindlist(AllTrialsList)
    CStratSummaryFunction <- function(DF){
      Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
      return(Summary)
    }
    SummaryTable <- ddply(AllTrialsDF,.(Contribution_Strategy),CStratSummaryFunction)
    return(SummaryTable)
  }
  SummaryTableList <- lapply(ThreatList,CStratThreatLevelAnalysis)
  AddThreatLevel <- function(i){
    SummaryTable <- data.frame(SummaryTableList[[i]],ThreatLevel = ThreatLevelList[[i]])
    return(SummaryTable)
  }
  SimultationDF <- rbindlist(lapply(Levels,AddThreatLevel))
  CStratPlot <- ggplot(data = SimulationDF, aes(x=Threat_Level, y=Proportion, group=Contribution_Strategy, colour=Contribution_Strategy)) + geom_line() + geom_point() + scale_x_continuous(breaks=seq(min(ThreatLevelList[[1]]),max(ThreatLevelList[[1]]), 20)) + geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05))
  return(CStratPlot)
}

PStratFunction <- function(ThreatList,Levels){
  PStratThreatLevelAnalysis <- function(TrialList){
    PStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(pstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      Counts[,1][Counts[,1] == 1] <- "Responsibly"
      Counts[,1][Counts[,1] == 2] <- "Anti_Socially"
      Counts[,1][Counts[,1] == 3] <- "Spitefully"
      Counts[,1][Counts[,1] == 4] <- "Never"
      names(Counts) <- c("Punishment_Strategy","Proportion")
      return(Counts)
    }
    AllTrialsList <- lapply(TrialList,PStratProportionFunction)
    AllTrialsDF <- rbindlist(AllTrialsList)
    PStratSummaryFunction <- function(DF){
      Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
      return(Summary)
    }
    SummaryTable <- ddply(AllTrialsDF,.(Punishment_Strategy),PStratSummaryFunction)
    return(SummaryTable)
  }
  SummaryTableList <- lapply(ThreatList,PStratThreatLevelAnalysis)
  AddThreatLevel <- function(i){
    SummaryTable <- data.frame(SummaryTableList[[i]],ThreatLevel = ThreatLevelList[[i]])
    return(SummaryTable)
  }
  SimultationDF <- rbindlist(lapply(Levels,AddThreatLevel))
  PStratPlot <- ggplot(data = SimulationDF, aes(x=Threat_Level, y=Proportion, group=Punishment_Strategy, colour=Punishment_Strategy)) + geom_line() + geom_point() + scale_x_continuous(breaks=seq(min(ThreatLevelList[[1]]),max(ThreatLevelList[[1]]), 20)) + geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05))
  return(PStratPlot)
}

CStratFunction(ListOfThreats,ThreatLevelIndex)
PStratFunction(ListOfThreats,ThreatLevelIndex)
