import tkinter as tk
import tkinter.filedialog as fd
import jetkiller as jk
from PIL import Image
import PIL.ImageTk as PilTk


def update_previews(input_1, menu_var, input_preview, output_preview):
    # Input preview
    input_image = Image.open(input_1.get())
    input_image_preview = input_image.resize((300, 300))
    tk_image = PilTk.PhotoImage(input_image_preview)
    input_preview.tk_image = tk_image  # keep a reference to avoid deletion by garbage collector
    input_preview.create_image(0, 0, image=input_preview.tk_image, anchor=tk.NW)

    # Output preview
    output_image_preview = jk.convert_image(input_image_preview,  colormap=menu_var.get())
    output_preview.tk_image = PilTk.PhotoImage(output_image_preview)
    output_preview.create_image(0, 0, image=output_preview.tk_image, anchor=tk.NW)


def browse_click(input_1, cm_menu, input_preview, output_preview):
    file = fd.askopenfilename()
    if file != ():
        input_1.delete(0, last=tk.END)
        input_1.insert(0, file)
        update_previews(input_1, cm_menu, input_preview, output_preview)


def save_click(input_1, v):
    file = fd.asksaveasfilename()
    jk.convert_file(input_1.get(), file, colormap=v.get())


def main():
    root = tk.Tk()
    root.title("Jet Killer")

    # Preview of input file
    input_preview = tk.Canvas(root, width=300, height=300, bg="yellow")
    input_preview.grid(column=0, row=2, columnspan=2)

    # Preview of output file
    output_preview = tk.Canvas(root, width=300, height=300, bg="green")
    output_preview.grid(column=2, row=2, columnspan=2)

    # File choice
    label_1 = tk.Label(root, text="Input file:")
    label_1.grid(column=0, row=0)
    input_1 = tk.Entry(root)
    input_1.grid(column=1, row=0)
    button_1 = tk.Button(root, text="...")
    button_1.grid(column=2, row=0)

    # Colormap choice
    label_2 = tk.Label(root, text="Colormap:")
    label_2.grid(column=0, row=1)
    menu_var = tk.StringVar()
    options = ("viridis", "plasma", "inferno", "magma")
    menu_var.set("viridis")

    cm_menu = tk.OptionMenu(root, menu_var, *options)
    cm_menu.grid(column=1, row=1, columnspan=2)
    cm_menu.bind('<<OptionMenuSelect>>', update_previews)

    # Convert and save button
    button_2 = tk.Button(root, text="Convert and save")
    button_2.grid(column=3, row=0, rowspan=2, sticky=tk.N+tk.S)

    button_1["command"] = lambda: browse_click(input_1, menu_var, input_preview, output_preview)
    button_2["command"] = lambda: save_click(input_1, menu_var)
    menu_var.trace("w", lambda *args: update_previews(input_1, menu_var, input_preview, output_preview))

    # Main loop
    root.mainloop()
