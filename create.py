import os
print("Current working directory:", os.getcwd())


# Specify the path and filename for the new text file
#txt_file_path = r'C:\Users\khaza\Documents\Udemy\Python_3_Deep_Dive\my_codes\new_file.txt'

#txt_file_path = 'my_codes/new_file.txt'
#txt_file_path = 'Python_3_Deep_Dive/my_codes/new_file.txt'
txt_file_path = r'C:\Users\khaza\Desktop\new_file.txt'

# Content to write to the file
file_content = "This is the content of the new text file.\n"
file_content += "You can add more lines as needed.\n"

# Open the file in write mode ('w')
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(file_content)

print(f"File '{txt_file_path}' created and written successfully.")
