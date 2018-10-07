import tkinter as tk
import tkinter.filedialog as fd
import jetkiller as jk
from PIL import Image
import PIL.ImageTk as PilTk
import sys


def scaling_transform(w1, h1, w2, h2):
    r1 = w1 / h1
    r2 = w2 / h2
    if r1 <= r2:
        h = h2
        w = r1 * h2
    else:
        w = w2
        h = w2 / r1
    return w, h


def update_preview(image, preview_canvas):
    frame_width, frame_height = int(preview_canvas["width"]), int(preview_canvas["height"])
    w1, h1 = image.width, image.height
    w, h = scaling_transform(w1, h1, frame_width, frame_height)
    image_miniature = image.resize((int(w), int(h)))
    tk_miniature = PilTk.PhotoImage(image_miniature)
    preview_canvas.create_image(frame_width / 2, frame_height / 2, image=tk_miniature)
    preview_canvas.tk_miniature = tk_miniature  # reference to avoid garbage collection
    return image_miniature


def update_previews(input_1, menu_var, input_preview_canvas, output_preview):
    # TODO: investigate problem with alpha channel

    try:
        # Open image
        filename = input_1.get()
        input_image = Image.open(filename)
        input_miniature = update_preview(input_image, input_preview_canvas)
        output_miniature = jk.convert_image(input_miniature, colormap=menu_var.get())
        update_preview(output_miniature, output_preview)

    except AttributeError as e:
        print("Error 1:", e, file=sys.stderr)
    except IOError as e:
        print("Error 2:", e, file=sys.stderr)


def browse_click(input_1, cm_menu, input_preview, output_preview):
    file = fd.askopenfilename()
    if file != ():
        input_1.delete(0, last=tk.END)
        input_1.insert(0, file)
        update_previews(input_1, cm_menu, input_preview, output_preview)


def save_click(input_1, v):
    filename = fd.asksaveasfilename()
    try:
        jk.convert_file(input_1.get(), filename, colormap=v.get())
    except AttributeError as e:
        print("Error 3:", e, file=sys.stderr)
    except ValueError as e:
        print("Error 4:", e, file=sys.stderr)


def main():
    root = tk.Tk()
    root.title("Jet Killer")

    # Preview of input file
    input_preview = tk.Canvas(root, width=300, height=300)
    input_preview.grid(column=0, row=2, columnspan=2)

    # Preview of output file
    output_preview = tk.Canvas(root, width=300, height=300)
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
