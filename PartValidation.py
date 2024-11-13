import tkinter as tk
import re
from claims_data import re_patterns
from re_builder import main

printing_outputs = False

def write_output(output):
    output_label.configure(state="normal")
    output_label.delete("1.0", tk.END)
    output_label.insert(tk.END, output)
    output_label.configure(state="disabled")

def part_check():
    part_number = input_text.get("1.0", "end-1c").strip()
    write_output("Not Valid")
    for i in range(len(re_patterns)):
        if re.fullmatch(re_patterns[i][0], part_number):
            part_type = re_patterns[i][1]
            part_number_sections = part_number.split("-")
            try:
                (x, y, z, weight, description) = re_patterns[i][2](part_type, part_number_sections)
            except:
                error_string = f"No wframe found for {i}, {re_patterns[i][1]}"
                print(error_string)
                write_output(error_string)
                break
            info_string = f"Part Number: {part_number}\nX: {x}\nY: {y}\nZ: {z}\nWeight: {weight}\nDescription: {description}"
            if printing_outputs:
                print(info_string)
            write_output(info_string)
            break
    

root = tk.Tk()
root.title("Part Validation")
# photo = tk.PhotoImage(file="face.png")
# root.iconphoto(False, photo)
instruction_label = tk.Label(root, text="Part Number:")
input_text = tk.Text(root, height=5, width=35)
button = tk.Button(root, text="Get Info", command=part_check)
output_label = tk.Text(root, height=10, width=35)
output_label.configure(state="disabled")
output_label.bind("<1>", lambda event: output_label.focus_set())
builder_button = tk.Button(root, text="Add RE", command=main)
builder_button.pack(side="top", anchor="ne")
for widget in root.winfo_children():
    widget.pack()

tk.mainloop()