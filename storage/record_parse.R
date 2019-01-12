record <- file("record.egt", "rb")
header_length <- readBin(record, integer(), size=1, endian = "little")
header_length

agent_bit_length <- readBin(record, integer(), size=1, endian = "little")

threat_level <- readBin(record, integer(), size=2, endian = "little")

gens <-c()
xs <- c()
ys <- c()
cstrats <- c()
pstrats <- c()
contTag <- c()

while(length(agent_record_parts <- readBin(record, integer(), size=1, n=agent_bit_length, endian = "little")) > 0) {
  gens <- c(gens, agent_record_parts[2])
  xs <- c(xs, agent_record_parts[3])
  ys <- c(ys, agent_record_parts[4])
  cstrats <- c(cstrats, agent_record_parts[5])
  pstrats <- c(pstrats, agent_record_parts[6])
  contTag <- c(contTag, agent_record_parts[7])
}

results <- data.frame(gens, xs, ys, cstrats, pstrats, contTag)
results
#help(readBin)
