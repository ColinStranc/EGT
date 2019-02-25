read.egt <- function(egt.dir)
{
  egt.dir
  record <- file(egt.dir, "rb")
  version <- readBin(record, integer(), size=1, endian = "little")
  
  header_length <- readBin(record, integer(), size=1, endian = "little")
  header_length
  
  settings <- readBin(record, integer(), size=1, n=header_length, endian = "little")
  rounds <- settings[header_length]
  
  gens <- c()
  xs  <- c()
  ys <- c()
  cstrats <- c()
  pstrats <- c()
  contrs <- c()
  
  for (i in c(1:rounds-7)) {
    round <- readBin(record, integer(), size=1)
    n.agents <- readBin(record, integer(), size=2, endian="big")
    
    for (j in c(1:n.agents)) {
      gens <- c(gens, round)
      
      agent.round.record <- readBin(record, integer(), size=2, endian="big")
  
      xs <- c(xs, readBin(record, integer(), size=1)+1)
      ys <- c(ys, readBin(record, integer(), size=1)+1)
      cstrats <- c(cstrats, readBin(record, integer(), size=1))
      pstrats <- c(pstrats, readBin(record, integer(), size=1))
      
      contrs <- c(contrs, readBin(record, integer(), size=1))
    }
  }
  
  results <- data.frame(gens, xs, ys, as.factor(cstrats), as.factor(pstrats), contrs)
  names(results) <- c("gens", "xs", "ys", "cstrats", "pstrats", "contTag")
  
  a <- list(results, settings[14], rounds, version, settings[9]/settings[10], settings[11]/settings[12], settings[1])
  names(a) <- c("results", "size", "reps", "egt.version", "mutation_rate", "death_rate", "base_pay")
  
  close(record)
  
  return(a)
}
  
#read.egt("../modelling/storage/egt_02_23_1841.egt")
