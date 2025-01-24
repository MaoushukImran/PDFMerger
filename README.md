# PDFMerger
This Python script provides an easy way to merge multiple PDF files from a specified folder into a single output PDF file. It uses the `PyPDF2` library to perform the merging process and `glob` to locate all PDF files in the given directory. This tool is useful for automating the task of combining PDFs without having to manually open each file.

### Features:
- Merges all PDF files found in a specified folder into one.
- Outputs the merged PDF to a user-specified file location.
- Handles files in a case-insensitive manner (so it works on both `.pdf` and `.PDF` files).
- Easy-to-use function `merge_pdfs()` that accepts a list of PDFs and the desired output path.

### How it works:
1. The script first scans a folder for all `.pdf` files.
2. It then merges them into a single PDF using the `PdfMerger` class from `PyPDF2`.
3. The final merged file is saved to the specified output path.

### Requirements:
- Python 3.x
- `PyPDF2` library (install via `pip install PyPDF2`)

### Usage:
1. Place your PDF files in a folder.
2. Update the `input_folder_path` with the path to your folder containing PDFs.
3. Specify the desired `output_file` path for the merged PDF.
4. Run the script to merge all PDFs in the folder into a single file.

