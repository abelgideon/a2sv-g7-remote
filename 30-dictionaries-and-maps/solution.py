# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())

contacts = {}

for _ in range(n):
    mapping = input().split()
    contacts[mapping[0]] = mapping[1]

for line in sys.stdin:
    inp = line.strip()
    if inp in contacts:
        print(f"{inp}={contacts[inp]}")
    else:
        print("Not found")