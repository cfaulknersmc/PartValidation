import tkinter as tk

def add_minimize_button(frame: tk.LabelFrame, outer_frame: tk.Frame, extended_frame = tk.Frame, padx: int = 5, pady: int = 5, width: int = 1, height: int = 2):
    """
    Adds the toggle button on the top right of the LabelFrame frame using the extended_frame for the button and frame with outer_frame surrounding frame with padding. Size of button given with width and height
    """
    frame_x = tk.Button(extended_frame, text="-", padx=padx, pady=pady, command=lambda: minimize_frame(frame=frame), height=height, width=width)
    frame_x.pack(side="right", anchor="n", padx=padx, pady=pady)
    outer_frame.pack(side="left", fill="both", padx=padx, pady=pady)

def minimize_frame(frame: tk.LabelFrame) -> None:
    """
    grid_remove gets called on LabelFrame frame if grid_info is found, otherwise calls grid.
    """
    if bool(frame.grid_info()):
        frame.grid_remove()
    else:
        frame.grid()

def extend_frame(text: str, parent_frame: tk.Frame | tk.LabelFrame, row: int = 0, column: int = 0, grid: bool = True, padx: int = 5, pady: int = 5, width: int = 1, height: int = 2) -> tk.LabelFrame:
    """
    Extends input frame by adding minimize button. Grids frame in row and column given into parent frame with padding specified. Size of button passed through width and height.
    """
    extended_frame = tk.Frame(parent_frame)
    if grid:
        extended_frame.grid(row=row, column=column)
    outer_frame = tk.Frame(extended_frame)
    frame = tk.LabelFrame(outer_frame, text=text)
    frame.grid()
    add_minimize_button(frame=frame, outer_frame=outer_frame, extended_frame=extended_frame, padx=padx, pady=pady, width=width, height=height)
    return frame
    
def create_condition(parent_frame: tk.Frame | tk.LabelFrame) -> tk.Frame:
    outer_frame = tk.Frame(parent_frame)
    options_1 = tk.OptionMenu(outer_frame, tk.StringVar(outer_frame), "1", "2", "3")
    equal_label = tk.Label(outer_frame, text="=")
    options_1b = tk.OptionMenu(outer_frame, tk.StringVar(outer_frame), "3", "4")
    tile_widgets(outer_frame, by_column=True)
    return outer_frame

def return_function(arg):
    return arg

def if_creation(parent_frame: tk.Frame, creation_func):
    outer_frame = tk.Frame(parent_frame)
    remove_button = tk.Button(outer_frame, text="-", command=outer_frame.destroy)
    if_label = tk.Label(outer_frame, text="If")
    condition_frame = create_condition(outer_frame)
    # condition_frame = creation_func()
    bool_ops_button = tk.Button(outer_frame, text="+", command=lambda: add_condition(parent_frame=condition_frame))
    colon_label = tk.Label(outer_frame, text=":")
    return outer_frame
    

def add_condition(parent_frame: tk.Frame):
    previous_condition_frame = parent_frame.winfo_children()[1]
    print(parent_frame, previous_condition_frame)
    parent_frame.grid_forget() #parent of previous_condition_frame
    condition_frame = tk.Frame(parent_frame)
    condition_1 = previous_condition_frame
    and_or_var = tk.StringVar(condition_frame)
    and_or_var.set("AND")
    and_or = tk.OptionMenu(condition_frame, and_or_var, "AND", "OR")
    condition_2 = create_condition(condition_frame)
    tile_widgets(condition_frame, by_column=True)
    condition_frame.grid()
    parent_frame.grid()
    # return if_creation(parent_frame=parent_frame, creation_func=lambda: return_function(condition_frame))


def create_variable_if(parent_frame: tk.Frame | tk.LabelFrame, row: int = 0, column: int = 0, grid: bool = True, padx: int = 5, pady: int = 5) -> tk.Frame:
    """
    Returns if frame for variable statements.
    """
    # outer_frame = tk.Frame(parent_frame)
    # remove_button = tk.Button(outer_frame, text="-", command=outer_frame.destroy)
    # if_label = tk.Label(outer_frame, text="If")
    # condition_frame = create_condition(outer_frame)
    # bool_ops_button = tk.Button(outer_frame, text="+", command=lambda: add_condition(outer_frame, condition_frame))
    # colon_label = tk.Label(outer_frame, text=":")
    outer_frame = if_creation(parent_frame=parent_frame, creation_func=lambda: create_condition(parent_frame))
    tile_widgets(outer_frame, by_column=True)
    value_box = tk.Entry(outer_frame)
    value_box.grid(row=1, column=1)
    if grid:
        outer_frame.grid(row=row, column=column, padx=padx, pady=pady)
    return outer_frame

def tile_widgets(frame: tk.Frame | tk.LabelFrame, by_column: bool = False, other_value: int = 0, padx: int = 5, pady: int = 5) -> None:
    """
    Grids all the widgets in winfo_children of frame either in a column or a row with padding. The row if by column and the column if not is set by other_value.
    """
    if by_column:
        for i, widget in enumerate(frame.winfo_children()):
            widget.grid(row=other_value, column=i, padx=padx, pady=pady)
    else:
        for i, widget in enumerate(frame.winfo_children()):
            widget.grid(row=i, column=other_value, padx=padx, pady=pady)


def drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

def main() -> None:
    FRAME_WIDTH = 600  # noqa: F841

    #Main Window
    window = tk.Tk()
    window.title("Re Builder")
    # window.geometry('900x500')
    window.resizable(False, False)

    #Main Frame
    main_frame = tk.Frame(window)
    main_frame.pack()
    
    part_expressions_frame = tk.LabelFrame(main_frame, text="Part Expressions")
    part_expressions_buttons_frame = tk.Frame(part_expressions_frame)
    part_expressions_button_or = tk.Button(part_expressions_buttons_frame, text="OR")
    part_expressions_button_remove = tk.Button(part_expressions_buttons_frame, text="-")
    part_expressions_button_or.grid(row=0, column=0, padx=5, pady=5)
    part_expressions_button_remove.grid(row=1, column=0, padx=5, pady=5)
    part_expressions_list_frame = tk.Frame(part_expressions_frame)
    part_expressions_frame.grid(row=0, column=0, padx=5, pady=5)
    part_expressions_scrollbar = tk.Scrollbar(part_expressions_list_frame)
    part_expressions_scrollbar.pack(side="right", fill="y")
    part_expressions_list = tk.Listbox(part_expressions_list_frame, yscrollcommand=part_expressions_scrollbar.set)
    part_expressions_list.insert(tk.END, "ITV0")
    part_expressions_list.insert(tk.END, "ITV1")
    part_expressions_list.pack(side="left", fill="both")
    part_expressions_scrollbar.config(command=part_expressions_list.yview)
    part_expressions_buttons_frame.pack(side="left", fill="y")
    part_expressions_list_frame.pack(side="right", fill="both")

    properties_frame = extend_frame(text="Properties", parent_frame=main_frame, column=1)
    properties_part_frame = extend_frame(text="Part", parent_frame=properties_frame)
    properties_part_pn_label = tk.Label(properties_part_frame, text="PN: ITV###0-")  # noqa: F841
    properties_part_hto_label = tk.Label(properties_part_frame, text="How to Order Document: Doc.pdf")  # noqa: F841
    properties_part_upload = tk.Button(properties_part_frame, text="Upload")  # noqa: F841
    tile_widgets(properties_part_frame)

    properties_selection_frame = extend_frame(text="Selection", parent_frame=properties_frame, row=1)
    properties_selection_options_frame = tk.Frame(properties_selection_frame)
    properties_selection_options_label = tk.Label(properties_selection_options_frame, text="Options: ")  # noqa: F841
    properties_selection_options_scrollbar_frame = tk.Frame(properties_selection_options_frame)
    properties_selection_options_scrollbar = tk.Scrollbar(properties_selection_options_scrollbar_frame, orient="horizontal")
    properties_selection_options_scrollbar.pack(side="bottom", fill="x")
    properties_selection_options_scrollbar_vertical = tk.Scrollbar(properties_selection_options_scrollbar_frame, orient="vertical")
    properties_selection_options_scrollbar_vertical.pack(side="right", fill="y")
    properties_selection_options_list = tk.Listbox(properties_selection_options_scrollbar_frame, xscrollcommand=properties_selection_options_scrollbar.set, yscrollcommand=properties_selection_options_scrollbar_vertical.set)
    properties_selection_options_list.insert(tk.END, "1")
    properties_selection_options_list.insert(tk.END, "3")
    properties_selection_options_list.insert(tk.END, "5")
    properties_selection_options_list.pack(side="top", fill="both")
    properties_selection_options_scrollbar.config(command=properties_selection_options_list.xview)
    properties_selection_options_scrollbar_vertical.config(command=properties_selection_options_list.yview)
    properties_selection_button = tk.Button(properties_selection_options_frame, text="+")  # noqa: F841
    tile_widgets(properties_selection_options_frame, by_column=True)
    properties_selection_nil_frame = tk.Frame(properties_selection_frame)
    properties_selection_nil_label = tk.Label(properties_selection_nil_frame, text="Nil Option:")  # noqa: F841
    properties_selection_nil_checkbutton = tk.Checkbutton(properties_selection_nil_frame)  # noqa: F841
    tile_widgets(properties_selection_nil_frame, by_column=True)
    tile_widgets(properties_selection_frame)

    properties_variables_frame = extend_frame(text="Variables", parent_frame=properties_frame, row=2)
    properties_variables_x_frame = tk.Frame(properties_variables_frame)
    properties_variables_x_frame.grid()
    x_if = create_variable_if(properties_variables_x_frame)
    x_if.grid()
    properties_variables_rohs_frame = tk.Frame(properties_variables_frame)
    properties_variables_rohs_label = tk.Label(properties_variables_rohs_frame, text="RoHS:")
    properties_variables_rohs_2_frame = tk.Frame(properties_variables_rohs_frame)
    properties_variables_rohs_3_frame = tk.Frame(properties_variables_rohs_frame)
    properties_variables_rohs_2_label = tk.Label(properties_variables_rohs_2_frame, text="2")
    properties_variables_rohs_3_label = tk.Label(properties_variables_rohs_3_frame, text="3")
    properties_variables_rohs_2_checkbutton = tk.Checkbutton(properties_variables_rohs_2_frame, command=lambda: properties_variables_rohs_3_checkbutton.deselect())
    properties_variables_rohs_3_checkbutton = tk.Checkbutton(properties_variables_rohs_3_frame, command=lambda: properties_variables_rohs_2_checkbutton.select())
    tile_widgets(properties_variables_rohs_2_frame, by_column=True, padx=0)
    tile_widgets(properties_variables_rohs_3_frame, by_column=True, padx=0)
    tile_widgets(properties_variables_rohs_frame, by_column=True)
    properties_variables_rohs_frame.grid()





    items_frame = tk.LabelFrame(main_frame, text="Add Items")
    items_frame.grid(row=1, column=0)
    canvas = tk.Canvas(items_frame, width=400, height=400)
    canvas.pack(fill="both")

    rect = canvas.create_text((10, 10), text="_", fill="blue")

    canvas.tag_bind(rect, "<Button-1>", drag_start)
    canvas.tag_bind(rect, "<B1-Motion>", drag_motion)
    
    window.mainloop()

if __name__ == "__main__":
    main()