from player import filechooser

# Open a file chooser dialog
file_path = filechooser.open_file()
print("Selected file:", file_path)

# Open multiple files chooser dialog
files_path = filechooser.open_file(multiple=True)
print("Selected files:", files_path)

# Save file chooser dialog
save_path = filechooser.save_file()
print("Save file path:", save_path)