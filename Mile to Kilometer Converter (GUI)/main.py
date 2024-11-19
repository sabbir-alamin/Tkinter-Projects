from tkinter import *  # Import the tkinter library for GUI development.

# Initialize the main program window.
program = Tk()
program.minsize(width=300, height=150)  # Set the minimum window size.
program.title("Mile to Km Converter")  # Set the window title.
program.config(padx=40, pady=40)  # Add padding around the elements in the window.

# Create an input entry field for entering miles.
given_mile = Entry(width=6, font="Caladea")  # Entry widget with a width of 6 and font style 'Caladea'.
given_mile.grid(column=2, row=1)  # Place the entry field in column 2, row 1 of the grid.

# Create a label to display the converted kilometers.
label4 = Label(text=0, font="Caladea")  # Initially set to 0 with font style 'Caladea'.
label4.grid(column=2, row=2)  # Place the label in column 2, row 2 of the grid.

# Add a label for the "Miles" text.
label = Label(text="Miles", font="Caladea")  # Display the text "Miles".
label.grid(column=3, row=1)  # Place the label in column 3, row 1 of the grid.
label.config(padx=10, pady=10)  # Add padding around the label.

# Add a label for the "is equal to" text.
label2 = Label(text="is equal to", font="Caladea")  # Display the text "is equal to".
label2.grid(column=1, row=2)  # Place the label in column 1, row 2 of the grid.
label2.config(padx=10, pady=10)  # Add padding around the label.

# Define the function to handle the conversion from miles to kilometers.
def buttons():
    # Retrieve the value entered in the entry field.
    value = float(given_mile.get())
    # Convert miles to kilometers (1 mile = 1.6 km) and round to 2 decimal places.
    kilometer = round((value * 1.60), 2)
    # Update the label4 to display the converted value.
    label4.config(text=f"{kilometer}", font="Caladea")

# Add a button that triggers the conversion function.
button = Button(text="Calculate", font="Caladea", command=buttons)  # Button labeled "Calculate".
button.grid(column=2, row=3)  # Place the button in column 2, row 3 of the grid.

# Add a label for the "Km" text.
label3 = Label(text="Km", font="Caladea")  # Display the text "Km".
label3.grid(column=3, row=2)  # Place the label in column 3, row 2 of the grid.
label3.config(padx=10, pady=10)  # Add padding around the label.

# Start the main event loop to run the program.
program.mainloop()
