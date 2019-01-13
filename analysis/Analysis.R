# Load packages used for analysis
library(plyr)
library(dplyr)
library(data.table)
library(ggplot2)

# Read data
source(file.path("./read_egt_2.R"),chdir=F)
# FileThreat03Trial01 <- read.egt("../modelling/storage/egt_02_23_1841.egt")
# DataThreat03Trial01 <- FileThreat03Trial01["results"]
# RepsThreat03Trial01 <- FileThreat03Trial01["reps"]
# 
# # Created temporary dummy data to run analyses on
# gens0302    <- c(1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
# xs0302      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1, 2, 4, 5, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
# ys0302      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 4, 5, 3, 4, 5, 3, 5, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
# cstrats0302 <- as.factor(c(1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1, 1, 2, 3, 2, 3, 2, 1))
# pstrats0302 <- as.factor(c(3, 4, 3, 2, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 1, 2, 3, 4, 3, 2, 1, 3, 2, 3, 2, 1, 1, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 4, 2, 3, 2, 1, 2, 1, 2, 3))
# contTag0302 <- c(0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0)
# results0302 <- data.frame(gens0302, xs0302, ys0302, cstrats0302, pstrats0302,contTag0302)
# names(results0302) <- c("gens","xs","ys","cstrats","pstrats","contTag")
# FileThreat03Trial02 <- list(results0302, 5, 5, 0, 0.1, 0.1)
# names(FileThreat03Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
# gens2501    <- c(1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
# xs2501      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
# ys2501      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
# cstrats2501 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1, 1, 1))
# pstrats2501 <- as.factor(c(4, 2, 2, 3, 4, 1, 1, 2, 3, 4, 2, 2, 3, 4, 1, 2, 1, 3, 2, 4, 3, 2, 2, 2, 2, 1, 4, 3, 3, 3, 1, 2, 2, 1, 1, 1, 3, 4, 3, 4, 3, 4, 3, 2, 1, 3, 1, 1, 1, 2, 2))
# contTag2501 <- c(0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0)
# results2501 <- data.frame(gens2501, xs2501, ys2501, cstrats2501, pstrats2501,contTag2501)
# names(results2501) <- c("gens","xs","ys","cstrats","pstrats","contTag")
# FileThreat25Trial01 <- list(results2501, 5, 5, 0, 0.1, 0.1)
# names(FileThreat25Trial01) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
# gens2502    <- c(1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
# xs2502      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
# ys2502      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
# cstrats2502 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1))
# cstrats2502 <- as.factor(c(2, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 2, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 2, 2, 2, 1, 1, 2, 3))
# pstrats2502 <- as.factor(c(2, 3, 4, 4, 4, 3, 2, 1, 2, 1, 3, 4, 1, 3, 1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 4, 3, 4, 3, 2, 1, 1, 3, 2, 4, 1, 3, 2, 1, 2, 3, 4, 3, 2, 2))
# contTag2502 <- c(1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0)
# results2502 <- data.frame(gens2502, xs2502, ys2502, cstrats2502, pstrats2502,contTag2502)
# names(results2502) <- c("gens","xs","ys","cstrats","pstrats","contTag")
# FileThreat25Trial02 <- list(results2502, 5, 5, 0, 0.1, 0.1)
# names(FileThreat25Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")

FileThreat03Trial01 <- read.egt("../modelling/storage/egt_02_23_2019_1550971166.egt")
FileThreat03Trial02 <- read.egt("../modelling/storage/egt_02_23_2020_1550971259.egt")
FileThreat03Trial03 <- read.egt("../modelling/storage/egt_02_23_2024_1550971471.egt")
FileThreat03Trial04 <- read.egt("../modelling/storage/egt_02_23_2026_1550971614.egt")
FileThreat03Trial05 <- read.egt("../modelling/storage/egt_02_23_2028_1550971733.egt")
FileThreat03Trial06 <- read.egt("../modelling/storage/egt_02_23_2029_1550971765.egt")

FileThreat25Trial01 <- read.egt("../modelling/storage/egt_02_23_2017_1550971044.egt")
FileThreat25Trial02 <- read.egt("../modelling/storage/egt_02_23_2018_1550971101.egt")
FileThreat25Trial03 <- read.egt("../modelling/storage/egt_02_23_2031_1550971864.egt")
FileThreat25Trial04 <- read.egt("../modelling/storage/egt_02_23_2031_1550971867.egt")
FileThreat25Trial05 <- read.egt("../modelling/storage/egt_02_23_2032_1550971935.egt")
FileThreat25Trial06 <- read.egt("../modelling/storage/egt_02_23_2032_1550971937.egt")

# Created lists of datasets as well as indices that will be used
DatasetsListThreat03 <- list(FileThreat03Trial01$results,FileThreat03Trial02$results,FileThreat03Trial03$results,FileThreat03Trial04$results,FileThreat03Trial05$results,FileThreat03Trial06$results)
DatasetsListThreat25 <- list(FileThreat25Trial01$results,FileThreat25Trial02$results,FileThreat25Trial03$results,FileThreat25Trial04$results,FileThreat25Trial05$results,FileThreat25Trial06$results)
ListOfThreats <- list(DatasetsListThreat03,DatasetsListThreat25)
ThreatLevelVector <- c(3,25)
LengthThreatLevelVector <- length(ThreatLevelVector)
ThreatLevelIndex <- c(1:LengthThreatLevelVector)

SummaryFunction <- function(DF){
  Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
  return(Summary)
}

StratDataPrep <- function(ThreatList,Levels,Strategy){
  StratThreatLevelAnalysis <- function(TrialList){
    StratProportionFunction <- function(Trial){
      Trial[[4]] <- recode(Trial[[4]],'1'='Contribute','2'='Dissent','3'='Opportunistic')
      Trial[[5]] <- recode(Trial[[5]],'1'='Responsibly','2'='Anti_Socially','3'='Spitefully','4'='Never')
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,Strategy,nrow)
      Counts[2] <- Counts[2] / NRow
      names(Counts) <- c("Strategy","Proportion")
      if(Strategy=='cstrats'){
        levels(Counts$Strategy) <- c(levels(Counts$Strategy),"Percentage_Contributing")
        Counts[4,] <- c("Percentage_Contributing",mean(Trial[[6]]))
        Counts[[2]] <- as.numeric(Counts[[2]])
      }else{}  
      return(Counts)
    }
    AllTrialsDF <- rbindlist(lapply(TrialList,StratProportionFunction))
    return(AllTrialsDF)
  }
  AllTrialsDFsList <- lapply(ThreatList,StratThreatLevelAnalysis)
  AddThreatLevel <- function(i){
    AllTrialsDF <- data.frame(AllTrialsDFsList[[i]],Threat_Level = ThreatLevelVector[i])
    return(AllTrialsDF)
  }
  SimulationDF <- rbindlist(lapply(Levels,AddThreatLevel))
  return(SimulationDF)
}

StratAnalysis <- function(SimDF){
  SimDF$Threat_Level <- as.factor(SimDF$Threat_Level)
  ANOVAFunction <- function(DF){
    ANOVA <- aov(Proportion~Threat_Level,DF)
    return(ANOVA)
  }
  ANOVAList <- dlply(SimDF,"Strategy",ANOVAFunction)
  ANOVASummaryTableFunction <- function(i){
    Summary <- summary(ANOVAList[[i]])
    SummaryTable <- data.frame(Strategy=names(ANOVAList[i]),
      DF_threat=Summary[[1]][1,1],
      DF_error=Summary[[1]][2,1],
      SS_threat=Summary[[1]][1,2],
      SS_error=Summary[[1]][2,2],
      MS_threat=Summary[[1]][1,3],
      MS_error=Summary[[1]][2,3],
      F=Summary[[1]][1,4],
      p=Summary[[1]][1,5],
      EtaSq=Summary[[1]][1,2]/(Summary[[1]][1,2]+Summary[[1]][2,2])
    )
    return(SummaryTable)
  }
  ANOVASummaryTable <- ldply(c(1:length(ANOVAList)),ANOVASummaryTableFunction)
  TukeyFunction <- function(ANOVA){
    Tukey <- TukeyHSD(ANOVA)
    Tukey <- Tukey$Threat_Level
    return(Tukey)
  }
  TukeyList <- lapply(ANOVAList,TukeyFunction)
  ResultsList <- list(ANOVASummaryTable,TukeyList) 
  return(ResultsList)
}

StratPlot <- function(SimulationDF,Strategy){
  SummaryTable <- ddply(SimulationDF,.(Strategy,Threat_Level),SummaryFunction)
  Labels <- if(Strategy=="Contribution"){c("Contribute", "Dissent", "Opportunistic","% Contributing")}else{c("Responsibly", "Anti-Socially", "Spitefully","Never")}
  CStratPlot <- ggplot(data=SummaryTable,aes(x=Threat_Level,y=Proportion,group=Strategy,colour=Strategy)) +
    geom_line() +
    geom_point(aes(shape=Strategy),size=3) +
    scale_x_continuous(breaks=seq(min(ThreatLevelVector),max(ThreatLevelVector),ThreatLevelVector[2]-ThreatLevelVector[1])) +
    coord_cartesian(ylim=c(0, 1)) +
    geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05)) +
    labs(title=paste0(Strategy," Strategy"),x="Threat Level",y="Long-Term Avg. Population Proportion") +
    scale_colour_discrete(name=paste0(Strategy," Strategy"),breaks=levels(SummaryTable$Strategy),labels=Labels) +
    scale_shape_manual(name=paste0(Strategy," Strategy"),breaks=levels(SummaryTable$Strategy),labels=Labels,values=c(15:18)) +
    theme_light()
  return(CStratPlot)
}

CStratData <- StratDataPrep(ListOfThreats,ThreatLevelIndex,"cstrats")
PStratData <- StratDataPrep(ListOfThreats,ThreatLevelIndex,"pstrats")
StratAnalysis(CStratData)
StratAnalysis(PStratData)
StratPlot(CStratData,"Contribution")
StratPlot(PStratData,"Punishment")