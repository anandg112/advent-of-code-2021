
def sub_path_dist():
    with open("sub-path.txt") as file:
        horizontal = depth = 0
        for command in file:
            match command.split(" "):
                case ("forward", distance):
                    horizontal += int(distance)
                case("up", distance):
                    depth -= int(distance)
                case("down", distance):
                    depth += int(distance)
        return horizontal * depth

def sub_path_dist2():
    with open("sub-path.txt") as file:
        horizontal = depth = aim = 0
        for command in file:
            match command.split(" "):
                case ("forward", distance):
                    horizontal += int(distance)
                    depth += int(distance) * aim
                case("up", distance):
                    aim -= int(distance)
                case("down", distance):
                    aim += int(distance)
        return horizontal * depth

if __name__ == "__main__":
    print(sub_path_dist())
    print(sub_path_dist2())
