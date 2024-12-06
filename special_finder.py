f = open("izts_success.txt", 'r')
lines = f.readlines()

specials = set()
for line in lines:
    parts = line.split("-")
    if parts[-1][0] == "X":
        specials.add(parts[-1].strip())

print(specials)