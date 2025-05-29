import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result.set(eval(entry.get()))
        except:
            result.set("Error")
    elif button_text == "C":
        result.set("")
    else:
        result.set(entry.get() + button_text)

root = tk.Tk()
root.title("Basic Calculator")

result = tk.StringVar()
entry = tk.Entry(root, textvariable=result, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, 
                  command=lambda t=text: on_click(t)).grid(row=i+1, column=j)

root.mainloop()
