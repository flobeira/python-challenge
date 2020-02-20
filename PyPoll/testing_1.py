#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
# Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates 
# each of the following:

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

import csv 

raw_data = 'c:/Users/franc/Desktop/UCSD/Homework/python-challenge/PyPoll/Resources/election_data.csv'

with open (raw_data, 'r') as csvfile:
    
    datareader = csv.reader(csvfile, delimiter = ',')
    next(datareader)
    dataList = list(datareader)

    voter_ID = []
    county = []
    candidate = []
    for ii in range(len(dataList)):
        voters = dataList[ii][0]
        region = dataList[ii][1]
        cand = dataList[ii][2]

        voter_ID.append(int(voters))
        county.append(str(region))
        candidate.append(str(cand))
    
    total = len(voter_ID)


    correy_counter = 0
    khan_counter = 0
    li_counter = 0
    otoolay_counter = 0 
    for ii in candidate:
        if ii == "Correy":
            correy_counter = correy_counter + 1
        elif ii == "Khan":
            khan_counter = khan_counter + 1
        elif  ii == "Li":
            li_counter = li_counter + 1
        elif  ii == "O'Tooley":
            otoolay_counter = otoolay_counter + 1 

    #Calculate percentages and create variables to store them
    correy_percentage = round((correy_counter/total)*100)
    khan_percentage = round((khan_counter/ total)*100)
    li_percentage = round((li_counter/total)*100)
    otoolay_percentage = round((otoolay_counter/total)*100)




# Results

print("Election Results")
print("------------------------------")
print("Total Votes: " + str(len(voter_ID)))
print("------------------------------")
print("Khan: " + str(khan_percentage) + "%" + "   (" + str(khan_counter)+")")
print("Correy: " + str(correy_percentage)+"%" + "   (" + str(correy_counter)+")")
print("Li: " + str(li_percentage)+"%" + "   (" + str(li_counter)+")")
print("O'Tooley: " + str(otoolay_percentage)+"%" + "   (" + str(otoolay_counter)+")")





