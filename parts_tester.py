import re
from pv_data import re_patterns
# from xml.etree import ElementTree as ET

# with open("itvs.txt", 'r') as f:
#     s = f.readline()

# find_result = s.find("<label")
# while find_result != -1:
#     end_find = s.find("</label>")
#     s = s[:find_result] + s[end_find + 8:]
#     find_result = s.find("<label")
# with open("itvs_formatted.txt", 'w') as f2:
#     f2.write(s)

verbose = False

filename = "izss_full.txt"

with open(filename, 'r') as f:
    lines = f.readlines()


def part_check(part_number):
    for i in range(len(re_patterns)):
        if re.fullmatch(re_patterns[i][0], part_number):
            # print(part_number)
            return True
    return False

sum = 0
failed = 0
with open(filename[:-4] + "_success.txt", 'w') as f2_success:
    with open(filename[:-4] + "_failed.txt", 'w') as f2:
        for line in lines:
            line = line.strip()
            result = part_check(line)
            if not result:
                result_line = line + " FAILED\n"
                if verbose: print(result_line, end='')
                f2.write(result_line)
                failed += 1
            else:
                f2_success.write(line + "\n")
                if verbose: print(line)
            sum += 1
print(f"{sum - failed} succeeded, {failed} failed out of {sum} or {100*failed/sum:.3f}% failed.")
    

# table = ET.XML(s)
# rows = iter(table)
# headers = [col.text for col in next(rows)]
# for row in rows:
#     values = [col.text for col in row]
#     part_check(values[1])