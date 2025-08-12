import math

AB = int(input())
BC = int(input())

angle_rad = math.atan2(AB, BC)

angle_deg = math.degrees(angle_rad)

result = round(angle_deg)

print(f"{result}\u00b0")
