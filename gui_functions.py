import tkinter as tk
from tkinter import messagebox, PhotoImage

def create_window():
    """Create and configure the main window"""
    window = tk.Tk()
    window.title('Guess the Country!')
    window.geometry('1200x700')
    window.resizable(False, False)

    window.bg = PhotoImage(file='assets/bg1.png')
    my_canvas = tk.Canvas(window, width=1200, height=700, highlightthickness=0)
    my_canvas.pack(fill='both', expand=True)

    my_canvas.bg_format = my_canvas.create_image(0, 0, image=window.bg, anchor='nw')

    widget_frame = tk.Frame(my_canvas, bg='#C0B89E', bd=0)
    my_canvas.create_window(600, 350, window=widget_frame, anchor='center')

    return window, my_canvas, widget_frame

def show_message(title, message):
    """Display a popup message box"""
    messagebox.showinfo(title, message)

def update_lives_display(lives_label, lives):
    """Update lives display"""
    hearts = '❤️ ' * lives
    lives_label.config(text = hearts, fg = 'brown')

def disable_key(button, correct=None):
    button.config(state='disabled')
    if correct is None:
        button.config(bg = 'white')
    elif correct:
        button.config(bg = '#4BEC4B')
    else:
        button.config(bg = '#9B9B9B')
               

def setup_ui(window, my_canvas, frame, handle_guess = None, start_new_game = None):

    blank_label = tk.Label(frame, text = '_ _ _ _ _', font = ('Courier New', 28, 'bold'), bg = '#C0B89E')
    blank_label.pack(pady=20)

    lives_label = tk.Label(frame, text = '❤️ ❤️ ❤️ ❤️ ❤️ ❤️', font = ('Courier New', 16), bg = '#C0B89E')
    lives_label.pack(pady=10)

    keyboard_frame = tk.Frame(frame, bg = '#C0B89E')
    keyboard_frame.pack(pady=20)

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i, letter in enumerate(letters):
        btn = tk.Button(
            keyboard_frame, text=letter,
            width=4, height=2,
            font=('Courier New Negrita', 12, 'bold'),
            bg='white'
        )

        btn.config(command=lambda l=letter, b=btn: handle_guess(l, b))

        btn.grid(row=i // 9, column=i % 9, padx=4, pady=4)
    

    new_game_button = tk.Button(
        frame, text = 'Reset Game', 
        command = start_new_game,
        font = ('Courier New Negrita', 14, 'bold'), 
        bg = "#1EB723", fg ='white'
        )
    new_game_button.pack(pady=10)
    
    # bg_mode = tk.Button(frame, text = 'mode', font = ('Courier New', 10), command = change_bg)

    return {'word_label': blank_label, 'lives_label': lives_label, 'keyboard_frame': keyboard_frame,}

# preview
if __name__ == '__main__':
    # ask_difficulty()
    window, my_canvas, frame, = create_window()
    setup_ui(window, my_canvas, frame)
    window.mainloop()
