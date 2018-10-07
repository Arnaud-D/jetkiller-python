import tkinter as tk
import tkinter.filedialog as fd
import jetkiller as jk
from PIL import Image
import PIL.ImageTk as PilTk
import sys


def scaling_transform(w1, h1, w2, h2):
    """Rescale rectangle (w1, h1) to fit in rectangle (w2, h2) without changing the ratio."""
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
    """Use an image to update a preview canvas."""
    frame_width, frame_height = int(preview_canvas["width"]), int(preview_canvas["height"])
    w1, h1 = image.width, image.height
    w, h = scaling_transform(w1, h1, frame_width, frame_height)
    image_miniature = image.resize((int(w), int(h)))
    tk_miniature = PilTk.PhotoImage(image_miniature)
    preview_canvas.create_image(frame_width / 2, frame_height / 2, image=tk_miniature)
    preview_canvas.tk_miniature = tk_miniature  # reference to avoid garbage collection
    return image_miniature


def update_previews(input_1, menu_var, input_preview_canvas, output_preview):
    """Update the input and output preview canvases from interface data."""
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
    """Action when clicking on the browse button."""
    file = fd.askopenfilename()
    if file != ():
        input_1.delete(0, last=tk.END)
        input_1.insert(0, file)
        update_previews(input_1, cm_menu, input_preview, output_preview)


def save_click(input_1, v):
    """Action when clicking on the save button."""
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
    input_preview_canvas = tk.Canvas(root, width=300, height=300)
    input_preview_canvas.grid(column=0, row=2, columnspan=2)

    # Preview of output file
    output_preview_canvas = tk.Canvas(root, width=300, height=300)
    output_preview_canvas.grid(column=2, row=2, columnspan=2)

    # Input file entry
    input_file_prompt = tk.Label(root, text="Input file:")
    input_file_prompt.grid(column=0, row=0)
    input_file_entry = tk.Entry(root)
    input_file_entry.grid(column=1, row=0)
    input_file_browse_button = tk.Button(root, text="...")
    input_file_browse_button.grid(column=2, row=0)

    # Colormap menu
    colormap_prompt = tk.Label(root, text="Colormap:")
    colormap_prompt.grid(column=0, row=1)
    colormap_var = tk.StringVar()
    colormap_options = ("viridis", "plasma", "inferno", "magma")  # TODO: add other  colormap choices for matplotlib
    colormap_var.set("viridis")
    colormap_menu = tk.OptionMenu(root, colormap_var, *colormap_options)
    colormap_menu.grid(column=1, row=1, columnspan=2)

    # Save button
    save_button = tk.Button(root, text="Convert and save")
    save_button.grid(column=3, row=0, rowspan=2, sticky=tk.N+tk.S)

    # Actions
    def input_file_browse_button_action():
        return browse_click(input_file_entry, colormap_var, input_preview_canvas, output_preview_canvas)

    def save_button_action():
        return save_click(input_file_entry, colormap_var)

    def colormap_action(*args):
        return update_previews(input_file_entry, colormap_var, input_preview_canvas, output_preview_canvas)

    input_file_browse_button["command"] = input_file_browse_button_action
    save_button["command"] = save_button_action
    colormap_var.trace("w", colormap_action)

    # Main loop
    root.mainloop()
