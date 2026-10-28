#28.Store scores of a batsman in 10 matches and calculate:
#a.Highest score b.Lowest score c.Total runs d.Average runs
#e.Number of centuries (≥100) f.Number of half-centuries (50– 99)
scores = [102, 45, 67, 89, 12, 134, 55, 0, 78, 92]
print("scores =",scores)

highest = max(scores)
lowest = min(scores)
total_runs = sum(scores)
avg = total_runs / len(scores)

centuries = sum(1 for s in scores if s >= 100)
half_centuries = sum(1 for s in scores if 50 <= s <= 99)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total_runs)
print("Average runs:", avg)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)