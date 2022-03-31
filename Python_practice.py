#print("Hello World!")

# How many votes did you get?
my_votes = int(input('200'))
#  Total votes in the election
total_votes = int(input('450'))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes/total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")