import os
import PyPDF2

merger = PyPDF2.PdfMerger()
new_file_suffix = ""

for file in os.listdir(os.curdir):
    new_file_suffix = ""
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
        new_file_suffix = new_file_suffix +"-"+ file

new_file_name = "combined-"+new_file_suffix+".pdf"
merger.write(new_file_name)
print("Combined file created with name: " + new_file_name)
