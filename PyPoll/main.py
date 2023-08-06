import os
import csv 

csvpath = os.path.join("Resources", "election_data.csv")
outpath = os.path.join("Analysis", "Analysis.txt")

#Create my variables 
total_votes = 0 
candidates = ""
percentage_votes = 0
total_votes0 = 0
total_votes1 = 0
total_votes2 = 0
winner = ""
greatest_votes = 0 
candidate_set = set()
candidate_list = []

#open file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip header 
    header = next(csvreader)

#iterate through row/lists in csv file
    for row in csvreader:
        total_votes += 1
        candidates = row[2]
        if candidates not in candidate_list:
            candidate_list.append(candidates)
        if candidates == candidate_list[0]:
            total_votes0 += 1
        elif candidates == candidate_list[1]:
            total_votes1 += 1
        elif candidates == candidate_list[2]:
            total_votes2 += 1

votes_list = [total_votes0, total_votes1, total_votes2]
max_votes = max(votes_list)
winner_index = votes_list.index(max(votes_list))
winner = candidate_list[winner_index]     
        
print(candidate_list) 
print(total_votes0, total_votes1, total_votes2)
print(max_votes)
print(winner_index)
print(winner)
print(f"{total_votes}")

lines = []
lines.append(f"Election Results")
lines.append(f"---------------------")
lines.append(f"Total Votes: {total_votes}")
lines.append(f"---------------------")
lines.append(f"{candidate_list[0]}: {round(votes_list[0]/total_votes*100,3)}% ({votes_list[0]})")
lines.append(f"{candidate_list[1]}: {round(votes_list[1]/total_votes*100,3)}% ({votes_list[1]})")
lines.append(f"{candidate_list[2]}: {round(votes_list[2]/total_votes*100,3)}% ({votes_list[2]})")
lines.append(f"---------------------")
lines.append(f"Winner: {winner}")

with open (outpath, 'w') as txtfile:
    for line in lines:
        txtfile.write(line + "\n")

