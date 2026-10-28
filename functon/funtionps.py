# write python function to count the number of lines not starting with the alphabet 'T' from the given storage

def count_lines():
    count = 0
    with open("story.txt", "r") as file:
        for line in file:
            if line.count("T") == 0:
                count += 1
    return count

print(count_lines())