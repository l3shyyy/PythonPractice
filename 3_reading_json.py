import json
import pandas
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path) as x:
    data = pandas.read_json(x)
    csv_data = data.to_csv()

root = tk.Tk()
root.withdraw()

save_to = filedialog.askdirectory()
completeName = os.path.join(save_to, "ExportedToCSV"+".csv")
file1 = open(completeName, "w")
toFile = csv_data
file1.write(toFile)
file1.close()