# Load packages used for analysis
library(plyr)
library(dplyr)
library(data.table)
library(ggplot2)


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
contTag0302 <- c(0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0)
results0302 <- data.frame(gens0302, xs0302, ys0302, cstrats0302, pstrats0302,contTag0302)
names(results0302) <- c("gens","xs","ys","cstrats","pstrats","contTag")
FileThreat03Trial02 <- list(results0302, 5, 5, 0, 0.1, 0.1)
names(FileThreat03Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
gens2501    <- c(1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
xs2501      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
ys2501      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
cstrats2501 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1, 1, 1))
pstrats2501 <- as.factor(c(4, 2, 2, 3, 4, 1, 1, 2, 3, 4, 2, 2, 3, 4, 1, 2, 1, 3, 2, 4, 3, 2, 2, 2, 2, 1, 4, 3, 3, 3, 1, 2, 2, 1, 1, 1, 3, 4, 3, 4, 3, 4, 3, 2, 1, 3, 1, 1, 1, 2, 2))
contTag2501 <- c(0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0)
results2501 <- data.frame(gens2501, xs2501, ys2501, cstrats2501, pstrats2501,contTag2501)
names(results2501) <- c("gens","xs","ys","cstrats","pstrats","contTag")
FileThreat25Trial01 <- list(results2501, 5, 5, 0, 0.1, 0.1)
names(FileThreat25Trial01) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")
gens2502    <- c(1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
xs2502      <- c(5, 5, 1, 2, 4, 5, 5, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5)
ys2502      <- c(4, 5, 2, 2, 5, 4, 5, 2, 1, 2, 4, 5, 4, 5, 4, 5, 1, 2, 3, 1, 2, 5, 1, 2, 3, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5)
cstrats2502 <- as.factor(c(2, 3, 3, 1, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 2, 2, 1, 3, 2, 1, 2, 2, 3, 2, 3, 1))
cstrats2502 <- as.factor(c(2, 3, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 2, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 2, 2, 2, 1, 1, 2, 3))
pstrats2502 <- as.factor(c(2, 3, 4, 4, 4, 3, 2, 1, 2, 1, 3, 4, 1, 3, 1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 4, 3, 4, 3, 2, 1, 1, 3, 2, 4, 1, 3, 2, 1, 2, 3, 4, 3, 2, 2))
contTag2502 <- c(1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0)
results2502 <- data.frame(gens2502, xs2502, ys2502, cstrats2502, pstrats2502,contTag2502)
names(results2502) <- c("gens","xs","ys","cstrats","pstrats","contTag")
FileThreat25Trial02 <- list(results2502, 5, 5, 0, 0.1, 0.1)
names(FileThreat25Trial02) <- c("results", "size", "reps", "egt.version", "mutation.rate", "death.rate")

# Created lists of datasets as well as indices that will be used
DatasetsListThreat03 <- list(FileThreat03Trial01$results,FileThreat03Trial02$results)
DatasetsListThreat25 <- list(FileThreat25Trial01$results,FileThreat25Trial02$results)
ListOfThreats <- list(DatasetsListThreat03,DatasetsListThreat25)
ThreatLevelVector <- c(3,25)
LengthThreatLevelVector <- length(ThreatLevelVector)
ThreatLevelIndex <- c(1:LengthThreatLevelVector)

# Function used in both other functions to summarize the means and standard deviations of the second row of a dataframe.
SummaryFunction <- function(DF){
  Summary <- c(Proportion=mean(DF[[2]]),sd=sd(DF[[2]]))
  return(Summary)
}

CStratDataPrep <- function(ThreatList,Levels){
  CStratThreatLevelAnalysis <- function(TrialList){
    # Function to determine the long-term proportion of each contribution strategy.
    CStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(cstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      Counts[[1]] <- recode(Counts[[1]],'1'='Contribute','2'='Dissent','3'='Opportunistic')
      names(Counts) <- c("Contribution_Strategy","Proportion")
      levels(Counts$Contribution_Strategy) <- c(levels(Counts$Contribution_Strategy),"Percentage_Contributing")
      Counts[4,] <- c("Percentage_Contributing",mean(Trial[[6]]))
      Counts[[2]] <- as.numeric(Counts[[2]])
      return(Counts)
    }
    AllTrialsDF <- rbindlist(lapply(TrialList,CStratProportionFunction)) # Apply CStratProportionFunction to each trail at a given threat level and then row bind into a dataframe.
    return(AllTrialsDF)
  }
  AllTrialsDFsList <- lapply(ThreatList,CStratThreatLevelAnalysis) # Apply the CStratThreatLevelAnalysis function to each threat level.
	AddThreatLevel <- function(i){
		AllTrialsDF <- data.frame(AllTrialsDFsList[[i]],Threat_Level = ThreatLevelVector[i])
		return(AllTrialsDF)
	}
  SimulationDF <- rbindlist(lapply(Levels,AddThreatLevel)) # Add the threat level to each dataframe and then row bind the threat levels dataframes into one dataframe.
  return(SimulationDF)
}

CStratAnalysis <- function(SimDF){
  SimDF$Threat_Level <- as.factor(SimDF$Threat_Level)
  ANOVAFunction <- function(DF){
    ANOVA <- aov(Proportion~Threat_Level,data=DF)
    return(ANOVA)
  }
  ANOVAList <- dlply(SimDF,.(Contribution_Strategy),ANOVAFunction)
  ANOVASummaryTableFunction <- function(i){
    Summary <- summary(ANOVAList[[i]])
    SummaryTable <- data.frame(Contribution_Strategy=names(ANOVAList[i]),
      DF_threat=Summary[[1]][1,1],
      DF_error=Summary[[1]][2,1],
      SS_threat=Summary[[1]][1,2],
      SS_error=Summary[[1]][2,2],
      MS_threat=Summary[[1]][1,3],
      MS_error=Summary[[1]][2,3],
      F=Summary[[1]][1,4],
      p=Summary[[1]][1,5],
      PrtlEtaSq=Summary[[1]][1,2]/(Summary[[1]][1,2]+Summary[[1]][2,2])
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
  names(TukeyList) <- c("Contribute","Dissent","Opportunistic","Percentage_Contributing")
  ResultsList <- list(ANOVASummaryTable,TukeyList) 
  return(ResultsList)
}

CStratPlot <- function(SimulationDF){
  SummaryTable <- ddply(SimulationDF,.(Contribution_Strategy,Threat_Level),SummaryFunction) # Use the summary function to find the mean proportion and SD for each contribution strategy and threat level.
  CStratPlot <- ggplot(data = SummaryTable, aes(x=Threat_Level, y=Proportion, group=Contribution_Strategy, colour=Contribution_Strategy)) +
    geom_line() +
    geom_point(aes(shape=Contribution_Strategy),size=3) +
    scale_x_continuous(breaks=seq(min(ThreatLevelVector),max(ThreatLevelVector),ThreatLevelVector[2]-ThreatLevelVector[1])) +
    coord_cartesian(ylim = c(0, 1)) +
    geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05)) +
    labs(title="Contribution Strategy",x="Threat Level",y="Long-Term Avg. Population Proportion") +
    scale_colour_discrete(name = "Contribution Strategy",breaks=c("Contribute", "Dissent", "Opportunistic","Percentage_Contributing"),labels = c("Contribute", "Dissent", "Opportunistic","% Contributing")) +
    scale_shape_manual(name = "Contribution Strategy",breaks=c("Contribute", "Dissent", "Opportunistic","Percentage_Contributing"),labels = c("Contribute", "Dissent", "Opportunistic","% Contributing"),values = c(15:18)) +
    theme_light()
  return(CStratPlot)
}

PStratDataPrep <- function(ThreatList,Levels){
  PStratThreatLevelAnalysis <- function(TrialList){
    # Function to determine the long-term proportion of each punishment strategy.
    PStratProportionFunction <- function(Trial){
      NRow <- nrow(Trial)
      Counts <- ddply(Trial,.(pstrats),.fun=nrow)
      Counts[2] <- Counts[2] / NRow
      Counts[[1]] <- recode(Counts[[1]],'1'='Responsibly','2'='Anti_Socially','3'='Spitefully','4'='Never')
      names(Counts) <- c("Punishment_Strategy","Proportion")
      return(Counts)
    }
    AllTrialsDF <- rbindlist(lapply(TrialList,PStratProportionFunction)) # Apply PStratProportionFunction to each trail at a given threat level and then row bind into a dataframe.
    return(AllTrialsDF)
  }
  AllTrialsDFsList <- lapply(ThreatList,PStratThreatLevelAnalysis) # Apply the PStratThreatLevelAnalysis function to each threat level.
  AddThreatLevel <- function(i){
		AllTrialsDF <- data.frame(AllTrialsDFsList[[i]],Threat_Level = ThreatLevelVector[i])
		return(AllTrialsDF)
	}
  SimulationDF <- rbindlist(lapply(Levels,AddThreatLevel)) # Add the threat level to each dataframe and then row bind the threat levels dataframes into one dataframe.
  return(SimulationDF)
}

PStratAnalysis <- function(SimDF){
  SimDF$Threat_Level <- as.factor(SimDF$Threat_Level)
  ANOVAFunction <- function(DF){
    ANOVA <- aov(Proportion~Threat_Level,data=DF)
    return(ANOVA)
  }
  ANOVAList <- dlply(SimDF,.(Punishment_Strategy),ANOVAFunction)
  ANOVASummaryTableFunction <- function(i){
    Summary <- summary(ANOVAList[[i]])
    SummaryTable <- data.frame(Punishment_Strategy=names(ANOVAList[i]),
      DF_threat=Summary[[1]][1,1],
      DF_error=Summary[[1]][2,1],
      SS_threat=Summary[[1]][1,2],
      SS_error=Summary[[1]][2,2],
      MS_threat=Summary[[1]][1,3],
      MS_error=Summary[[1]][2,3],
      F=Summary[[1]][1,4],
      p=Summary[[1]][1,5],
      PrtlEtaSq=Summary[[1]][1,2]/(Summary[[1]][1,2]+Summary[[1]][2,2])
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
  names(TukeyList) <- c("Responsibly","Anti_Socially","Spitefully","Never")
  ResultsList <- list(ANOVASummaryTable,TukeyList) 
  return(ResultsList)
}

PStratPlot <- function(SimulationDF){
  SummaryTable <- ddply(SimulationDF,.(Punishment_Strategy,Threat_Level),SummaryFunction) # Use the summary function to find the mean proportion and SD for each punishment strategy and threat level.
  PStratPlot <- ggplot(data = SummaryTable, aes(x=Threat_Level, y=Proportion, group=Punishment_Strategy, colour=Punishment_Strategy)) +
    geom_line() +
    geom_point(aes(shape=Punishment_Strategy),size=3) +
    scale_x_continuous(breaks=seq(min(ThreatLevelVector),max(ThreatLevelVector),ThreatLevelVector[2]-ThreatLevelVector[1])) +
    coord_cartesian(ylim = c(0, 1))+
    geom_errorbar(aes(ymin=Proportion-(sd/2), ymax=Proportion+(sd/2)), width=1,position=position_dodge(0.05)) +
    labs(title="Punishment Strategy",x="Threat Level",y="Long-Term Avg. Population Proportion") +
    scale_colour_discrete(name = "Punishment Strategy",breaks=c("Responsibly", "Anti_Socially", "Spitefully","Never"),labels = c("Responsibly", "Anti-Socially", "Spitefully","Never")) +
    scale_shape_manual(name = "Punishment Strategy",breaks=c("Responsibly", "Anti_Socially", "Spitefully","Never"),labels = c("Responsibly", "Anti-Socially", "Spitefully","Never"),values = c(15:18)) +
    theme_light()
  return(PStratPlot)
}

CStratData <- CStratDataPrep(ListOfThreats,ThreatLevelIndex)
PStratData <- PStratDataPrep(ListOfThreats,ThreatLevelIndex)
CStratAnalysis(CStratData)
PStratAnalysis(PStratData)
CStratPlot(CStratData)
PStratPlot(PStratData)