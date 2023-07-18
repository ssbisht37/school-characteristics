df <- read.csv("Public_School_Characteristics_2018-19.csv", sep = ",", header = TRUE, stringsAsFactors = FALSE)

df$MAGNET_TEXT[is.na(df$MAGNET_TEXT)]

df[is.na(df)] <- '?'

write.csv(df, "Public_School_Characteristics_2018-19_?Miss.csv")
