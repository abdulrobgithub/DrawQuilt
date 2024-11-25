import tkinter as tk

# Each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    # Create the main window and canvas
    root = tk.Tk()
    root.title("Patchwork")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE * 2, 0)
    draw_circle_patch(canvas, PATCH_SIZE * 3, 0)

    # Add other rows or patterns if needed here

    # Start the main event loop
    root.mainloop()

def draw_circle_patch(canvas, start_x, start_y):
    """Draws a circle patch at (start_x, start_y)."""
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # Draw a yellow square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="yellow", outline="")
    # Draw a circle in the center
    canvas.create_oval(start_x + inset, start_y + inset, 
                       end_x - inset, end_y - inset, fill="blue", outline="")

def draw_square_patch(canvas, start_x, start_y):
    """Draws a square patch at (start_x, start_y)."""
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # Draw a purple square background
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="purple", outline="")
    # Draw a smaller white square on top
    canvas.create_rectangle(start_x + inset, start_y + inset, 
                            end_x - inset, end_y - inset, fill="white", outline="")

if __name__ == '__main__':
    main()
