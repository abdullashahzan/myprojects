import tkinter as tk

parent = tk.Tk()
canvas = tk.Canvas(parent)
scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)
# group of widgets
for i in range(30):
    tk.Label(frame, text = "This is a spam label").pack()
tk.Button(frame, text = "Save All",
              font = ("poppins", 10, "bold"),
              background = "lightblue",
              width = 25).pack(side = "bottom", padx = 10, pady = 10)

# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

parent.mainloop()