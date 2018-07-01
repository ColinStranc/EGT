EGTData <- read.EGT(<sample data>)

EGTDataFinalGen <- subset(EGTData,gens == 50)

CStratCount <- c(nrow(subset(EGTDataFinalGen,cstrats == 1)),nrow(subset(EGTDataFinalGen,cstrats == 2)),nrow(subset(EGTDataFinalGen,cstrats == 3)))
PStratCount <- c(nrow(subset(EGTDataFinalGen,pstrats == 1)),nrow(subset(EGTDataFinalGen,pstrats == 2)),nrow(subset(EGTDataFinalGen,pstrats == 3)),nrow(subset(EGTDataFinalGen,pstrats == 4))
