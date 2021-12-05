import pandas as pd

def binaryToDecimal(binary):
    decimal, i= 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary//10
        i += 1
    return decimal

# PART 1

#data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
with open("Day3.txt") as file:
    lines = file.readlines()
    data = [line.rstrip() for line in lines]


splitData = []

for item in data:
    newList = [int(char) for char in item]
    splitData.append(newList)


df = pd.DataFrame(splitData)

# get the gamma rate
i = 0
gamma = ""
epsilon = ""
while i < len(df.columns):
    common = df[i].value_counts().idxmax()
    least = df[i].value_counts().idxmin()
    gamma = gamma + str(common)
    epsilon = epsilon + str(least)
    i = i + 1

gamma = binaryToDecimal(int(gamma))
epsilon = binaryToDecimal(int(epsilon))

print("Power Consumption: " + str(gamma * epsilon))


#PART 2

# Oxygen Generator Rating
df2 = df
stop = False
i = 0
while not stop:
    counts = df2[i].value_counts()
    numOfOne = counts[1]
    numOfZero = counts[0]
    
    if numOfOne > numOfZero:
        common = 1
    elif numOfZero > numOfOne:
        common = 0
    else:
        common = 1
    df2 = df2.loc[df2[i] == common]
    i = i + 1
    
    index = df2.index
    number_of_rows = len(index)
        
    if number_of_rows == 1:
        stop = True

oxygen = binaryToDecimal(int(''.join([str(elem) for elem in df2.values.tolist()[0]])))

# CO2 Scrubber Rating
df2 = df
stop = False
i = 0
while not stop:
    counts = df2[i].value_counts()
    numOfOne = counts[1]
    numOfZero = counts[0]
    
    if numOfOne < numOfZero:
        least = 1
    elif numOfZero < numOfOne:
        least = 0
    else:
        least = 0
    
    df2 = df2.loc[df2[i] == least]
    i = i + 1
    index = df2.index
    number_of_rows = len(index)
    
    if number_of_rows == 1:
        stop = True

co2 = binaryToDecimal(int(''.join([str(elem) for elem in df2.values.tolist()[0]])))

print("Life Support Rating: " + str(oxygen * co2))
