import tkinter as tk

window = tk.Tk()

window.title('Tally Counter')
window.geometry('350x500')

bottom_frame = tk.Frame(window)

title = tk.Label(window, text='Tally Counter', font=('', 42))

count_display = tk.Label(window, font=('', 200))
count_up_btn = tk.Button(window, text='+', font=('', 80), fg="green")
count_down_btn = tk.Button(window, text='-', font=('', 80), fg='blue')
count_reset_btn = tk.Button(
    bottom_frame, text='Reset', font=('', 20), fg='red')

tally = 0


def update_count_display(tally): return count_display.configure(text=tally)


def count_up():
    global tally
    tally += 1
    update_count_display(tally)


def count_down():
    global tally
    tally = 0 if (tally - 1) < 0 else tally - 1
    update_count_display(tally)


def count_reset():
    global tally
    tally = 0
    update_count_display(tally)


count_up_btn.configure(command=count_up)
count_down_btn.configure(command=count_down)
count_reset_btn.configure(command=count_reset)

update_count_display(tally)

title.pack()
count_display.pack(expand=True, fill='both')
count_reset_btn.pack(expand=True, fill='x')
bottom_frame.pack()
count_up_btn.pack(side='right', expand=True, fill='x')
count_down_btn.pack(side='left', expand=True, fill='x')

window.mainloop()
