import re
from pv_data import re_patterns
re_str = "^ITV009[01]-[0-3]U?M?[BC]?[NSL]"
try:
    re.compile(re_str)
except:
    print("Invalid re string")
    exit()

verbose = False

def part_check(part_number):
    for i in range(len(re_patterns)):
        if re.fullmatch(re_patterns[i][0], part_number):
            # print(part_number)
            return True
    return False

def redo_find(index: int, length: int):
    if index < 0:
        return length + 5
    return index

def combine_2lists(a: list[str] | tuple[str], b: list[str] | tuple[str]) -> list[str]:
    if a == [] or a == tuple():
        return b
    elif b == [] or b == tuple():
        return a
    if isinstance(a, str):
        a = [a]
    if isinstance(b, str):
        b = [b]
    return_list = []
    for item_a in a:
        for item_b in b:
            return_list.append(item_a + item_b)
    return return_list

def preprocess(in_str: str) -> str:
    if in_str == "":
        return in_str
    if in_str[0] == "^":
        in_str = in_str[1:]
    if in_str[-1] == "$" and len(in_str) > 1:
        if in_str[-2] != "\\":
            in_str = in_str[:-1]
    question_list = re.findall(r"\w\?", in_str)
    for question in set(question_list):
        in_str = in_str.replace(question, '[' + question[0] + ']?')
    in_str = in_str.replace("]?", "?]").replace(")?", "|?)")
    return in_str

def sum_lists(*lists: list[list[str] | tuple[str] | str] | tuple[list[str] | tuple[str] | str]) -> list[str]:
    return_list = []
    for list in lists[0]:
        return_list += replace_questions(list)
    return return_list

def replace_questions(in_list: list[str] | tuple[str]) -> list[str]:
    new_list = []
    for item in in_list:
        if item == "?":
            new_list.append("")
        else:
            new_list.append(item)
    return new_list

def combine_lists(*lists: list[list[str] | tuple[str] | str] | tuple[list[str] | tuple[str] | str], in_brackets: bool = False) -> list[str]:
    if in_brackets:
        return sum_lists(lists)
    start_list = replace_questions(lists[0])
    if len(lists) == 1:
        return start_list
    for next_list in lists[1:]:
        if isinstance(next_list, str):
            next_list = [next_list]
        start_list = combine_2lists(start_list, replace_questions(next_list))
    return start_list

def get_re_list(instr : str, in_brackets = False) -> tuple[str]:
    if instr == "":
        return tuple()
    if verbose: print(instr)
    instr_len = len(instr)
    soft_start, hard_start = instr.find('('), instr.find('[')
    soft_end, hard_end = instr.find(')', soft_start) - 1, instr.find(']', hard_start) - 1
    start_list, end_list = [], []
    
    if soft_start < redo_find(hard_start, instr_len) and soft_start != -1:
        start_sect, mid_sect, end_sect = instr[: soft_start], instr[soft_start + 1: soft_end + 1], instr[soft_end + 2:]
        if verbose: print("PARTS (p):", start_sect, mid_sect, end_sect)
        start_list, end_list = get_re_list(start_sect, in_brackets=in_brackets), get_re_list(end_sect, in_brackets=in_brackets)
        if hard_start == -1:
            mid_list = mid_sect.split("|")
        else:
            mid_list = sum_lists(*[get_re_list(item, in_brackets=in_brackets) for item in mid_sect.split("|")])
    elif hard_start < redo_find(soft_start, instr_len) and hard_start != -1:
        start_sect, mid_sect, end_sect = instr[: hard_start], instr[hard_start + 1: hard_end + 1], instr[hard_end + 2:]
        if verbose: print("PARTS (b):", start_sect, mid_sect, end_sect)
        start_list, end_list = get_re_list(start_sect, in_brackets=in_brackets), get_re_list(end_sect, in_brackets=in_brackets)
        if soft_start == -1:
            range_list = mid_sect.split("-")
            if len(range_list) == 2 and range_list[0].isnumeric() and range_list[1].isnumeric():
                mid_list = [str(i) for i in range(int(range_list[0]), int(range_list[1]) + 1)]
            else:
                mid_list = [item for item in mid_sect]
        else:
            mid_list = get_re_list(mid_sect, in_brackets=True)
    elif hard_start == -1 and soft_start == -1:
        if in_brackets:
            range_list = instr.split("-")
            if len(range_list) == 2 and range_list[0].isnumeric() and range_list[1].isnumeric():
                mid_list = [str(i) for i in range(int(range_list[0]), int(range_list[1]) + 1)]
            else:
                mid_list = [item for item in instr]
        else:
            mid_list = [instr]
    
    return_list = combine_lists(start_list, mid_list, end_list, in_brackets=in_brackets)
    if verbose: print(return_list)
    return tuple(return_list)


if __name__ == "__main__":
    print(re_str)
    overall_check_bool = True
    check_bools = []
    for re_str_in in re_patterns:
        try:
            full_list = get_re_list(preprocess(re_str_in[0].pattern))
        except MemoryError as e:
            print(e)
        # print(full_list)
        check_bool = True
        for item in full_list:
            check_bool &= part_check(item)
        check_bools.append((re_str_in[1], check_bool))
        print(check_bools[-1])
        overall_check_bool &= check_bool
    print("OVERALL:", overall_check_bool)
    print(check_bools)