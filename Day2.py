#PART 1
#instructions = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
with open("Day2.txt") as file:
    lines = file.readlines()
    instructions = [line.rstrip() for line in lines]

horizontal = 0
depth = 0

for instruction in instructions:
    splitInstruction = instruction.split()
    direction = splitInstruction[0]
    val = int(splitInstruction[1])
    
    if direction == "up":
        depth = depth - val
    elif direction == "down":
        depth = depth + val
    elif direction == "forward":
        horizontal = horizontal + val

print("Horizontal Position: " + str(horizontal) + " Depth: " + str(depth) + " Multiplied: " + str(horizontal * depth))


# PART 2
horizontal = 0
depth = 0
aim = 0

for instruction in instructions:
    splitInstruction = instruction.split()
    direction = splitInstruction[0]
    val = int(splitInstruction[1])
    
    if direction == "up":
        aim = aim - val
    if direction == "down":
        aim = aim + val
    if direction == "forward":
        horizontal = horizontal + val
        depth = depth + (aim * val)


print("Horizontal Position: " + str(horizontal) + " Depth: " + str(depth) + " Multiplied: " + str(horizontal * depth))
