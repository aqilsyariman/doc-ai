import PyPDF2
def validate_files(files):
    valid_files = []
    for file in files:
        if file.endswith(".pdf"):
            valid_files.append(file)
            
    
    return valid_files


def read_pdf(file_name):
    pdf_file = open(file_name,"rb")
    reader = PyPDF2.PdfReader(pdf_file)
    text = reader.pages[0].extract_text()
    print(text)    
    

result = validate_files(["L1 IP (added subnet route).jpg"])

if result:
    read_pdf(result[0])
else:
    print("Error: Not a PDF file")