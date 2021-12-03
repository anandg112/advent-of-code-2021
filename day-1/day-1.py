f = open("input.txt", "r")
sonar_scan = f.read().splitlines()
sonar_scan_int = list(map(int, sonar_scan))
f.close()

compare_previous = sum(x < y for x, y in zip(sonar_scan_int, sonar_scan_int[1:]))
print(compare_previous)

compare_previous_3 = sum(x < y for x, y in zip(sonar_scan_int, sonar_scan_int[3:]))
print(compare_previous_3)¬