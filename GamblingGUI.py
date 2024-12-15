import tkinter as tk
from tkinter import messagebox


'''
Creates the GUI for the user and the necessary fields to determine payouts
for the specific sport.
'''
class GamblingGUI:
    def __init__(self, master):
        FontName = "Arial"
        # Create the main window
        self.master = master
        master.title("Gambling GUI")
        master.geometry("400x300")  # Initial window size

        # Configure the grid to be resizable
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Create a label with grid and make it expand
        self.label = tk.Label(master, text="Advantage Gambling GUI", font=(FontName, 14))
        self.label.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        # Create drop-down select
        self.sport_frame = tk.Frame(master)
        self.sports = ["Two Team", "Horse Race", "Prop Bet"]
        self.selected_sport = tk.StringVar()
        self.selected_sport.set(self.sports[0])
        self.sport_dropdown = tk.OptionMenu(self.sport_frame, self.selected_sport, *self.sports)

        self.sports_label = tk.Label(self.sport_frame, text="Select Sport:", font=(FontName, 12))
        self.sports_label.grid(row=0, column=0, sticky='ew', padx=20, pady=10)
        self.sport_dropdown.grid(row=0, column=1, sticky='ew', padx=20, pady=10)

        self.sport_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=10)

        # Create an entry field that expands horizontally
        self.entry = tk.Entry(master, width=30, font=(FontName, 12))
        self.entry.grid(row=2, column=0, sticky='ew', padx=20, pady=10)

        # Create a frame to hold buttons and make them expand
        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=3, column=0, sticky='nsew', padx=20, pady=10)

        # Configure button frame to be resizable
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        # Create buttons inside the frame
        self.greet_button = tk.Button(self.button_frame, text="Greet", command=self.greet)
        self.greet_button.grid(row=0, column=0, sticky='ew', padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=master.quit)
        self.quit_button.grid(row=0, column=1, sticky='ew', padx=5)

    def greet(self):
        # Get text from entry and show a message
        name = self.entry.get()
        if name:
            messagebox.showinfo("Greeting", f"Hello, {name}!")
        else:
            messagebox.showwarning("Warning", "Please enter a name!")


# Create the main window and start the GUI
def main():
    root = tk.Tk()
    my_gui = GamblingGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()