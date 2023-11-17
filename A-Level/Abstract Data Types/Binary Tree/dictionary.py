#empty dictionay- key/value pair
CSPredictedGrades  = {}

#fill in dictionary values
CSPredictedGrades["Jeff"]  = "B"
CSPredictedGrades["Arnold"]  = "C"
CSPredictedGrades["Sally"]  = "A*"

#simple retrival using key
PredictedGrade = CSPredictedGrades["Arnold"]
print("PredictedGrade is " + PredictedGrade)

#iterate over the dictionary
for key in CSPredictedGrades:
    print("key: " + key + " value: " + CSPredictedGrades[key]) 