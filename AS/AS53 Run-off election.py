candidates = ["Alice", "Bob", "Eve"]
votes = [
    ["Alice", "Bob", "Eve"],   
    ["Bob", "Alice", "Eve"],   
    ["Alice", "Eve", "Bob"],   
    ["Eve", "Bob", "Alice"],   
    ["Eve", "Alice", "Bob"],   
]

counts = [0] * len(candidates)
for ballot in votes:
    counts[candidates.index(ballot[0])] += 1

max_votes = max(counts)
if max_votes > len(votes) / 2:
    print(f"{candidates[counts.index(max_votes)]} wins with a majority!")
else:
    print("Runoff election needed!")
    counts = [0] * len(candidates)
    for ballot in votes:
        for i in range(len(candidates)):
          max_votes = max(counts)
          if ballot[i] == candidates[counts.index(max_votes)]:
            counts[i] += 1
            break
    print(f"{candidates[counts.index(max(counts))]} wins the runoff election!")
