f = open("izss_full_failed.txt", 'r')
lines = f.readlines()

specials = set()
for line in lines:
    parts = line.split("-")
    if parts[-1][0] == "X" or parts[-1][:2] == "DI" or parts[-1][:2] == "DU" or parts[-1][:2] == "CE" or parts[-1][:2] == "OA":
        specials.add(parts[0].strip() + "-" + parts[-1].strip().replace(" FAILED", ""))

print(specials)