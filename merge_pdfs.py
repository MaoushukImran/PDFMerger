import os
import PyPDF2
import glob

def merge_pdfs(pdf_files, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    for file in pdf_files:
        pdf_merger.append(file)

    with open(output_file, 'wb') as output:
        pdf_merger.write(output)
    print("PDFs merged successfully into: {output_file}")

def get_pdf_files_from_folder(folder_path):
    # Use glob to get all PDF files in the folder (case insensitive)
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
    return pdf_files

# Specify the folder path where the PDFs are located
input_folder_path = 'C:\\Users\\PM'

# Get all PDF files from the folder
pdf_files = get_pdf_files_from_folder(input_folder_path)

# Specify the output path for the merged PDF
output_file = 'C:\\Users\\PM\\merged_output.pdf'

if pdf_files:
    # Merge PDFs if there are any files in the folder
    merge_pdfs(pdf_files, output_file)
else:
    print("No PDF files found in the specified folder.")
