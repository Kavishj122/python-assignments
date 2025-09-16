import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display_var.set("")
    else:
        expression += text
        display_var.set(expression)

# Main Window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

expression = ""
display_var = tk.StringVar()

# Entry Display
display = tk.Entry(root, textvar=display_var, font="lucida 20 bold", justify="right")
display.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        b = tk.Button(row_frame, text=btn_text, font="lucida 15", height=2, width=5)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()