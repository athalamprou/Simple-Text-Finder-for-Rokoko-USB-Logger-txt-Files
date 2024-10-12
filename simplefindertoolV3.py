import tkinter as tk
from tkinter import filedialog
import sys


class TextRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str1):
        self.text_widget.insert(tk.END, str1)
        self.text_widget.see(tk.END)  # Scroll to the end


def run_script(window1, filename):
    # Create a new window for the output
    output_window = tk.Toplevel(window1)
    output_window.title("Output")

    # Create a text widget to display the output
    output_text = tk.Text(output_window)
    output_text.pack(expand=True, fill="both")

    # Redirect stdout to the text widget
    sys.stdout = TextRedirector(output_text)

    # Now execute your script content
    import pandas as pd

    # Create empty DataFrame
    data = {'Sensor with addr': [], 'Calibration ID': []}
    df = pd.DataFrame(data)

    # Create dictionary to store the number of occurances per sensor
    sensor_counts = {}

    # Open file and read line by line
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines in the list 'lines'
        for i, line in enumerate(lines):
            # If line contains Calibration ID with value '0xfefefefe'
            if "Calibration ID: 0xfefefefe" in line:
                calibration_id = line.split(":")[-1].strip()  # Use said Calibration ID in that line 
                sensor_line = lines[i - 6].strip()  # Store line with sensor 
                sensor_id = sensor_line.split(" ")[-1]  # Use sensor ID from specific line

                # Update the dictionary with number of occurances in sensor 
                if sensor_id in sensor_counts:
                    sensor_counts[sensor_id] += 1
                else:
                    sensor_counts[sensor_id] = 1

                # Add sensor and Calibration ID to DataFrame
                df = pd.concat([df, pd.DataFrame({'Sensor with addr': [f'Sensor with addr {sensor_id}'],
                                                  'Calibration ID': [calibration_id]})], ignore_index=True)

    # Print results
    for sensor_id, count in sensor_counts.items():
        print(f"Sensor with addr {sensor_id} and calibration id: 0xfefefefe found {count} time(s)")

    # If no sensor found print the following
    if len(sensor_counts) == 0:
        print("\nNo sensors with Calibration ID: 0xfefefefe were found.")

    # Check file for specific string
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines in list lines
        for line in lines:
            if "BMI configuration fail on finger" in line:
                # Use find() method to find string's position
                index = line.find("BMI configuration fail on finger")
                # Use line's subset from position index till the end of the line
                substring = line[index:]
                # Find the first number occurence in the substring
                number = ''.join(filter(lambda x: x.isdigit(), substring))
                # Use first digit of found number
                first_digit = number[0]
                print(f"\nBMI configuration fail on finger {first_digit}")


def open_file():
    filename = filedialog.askopenfilename(title="Select a file",
                                          filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    if filename:
        run_script(window, filename)


# Create the main application window
window = tk.Tk()
window.title("Simple Finder Tool v3")

# Create a label
label = tk.Label(window, text="Welcome to SFT v3")
label.pack()

# Create a button to open file dialog
btn_open_file = tk.Button(window, text="Open File", command=open_file)
btn_open_file.pack()

# Run the Tkinter event loop
window.mainloop()
