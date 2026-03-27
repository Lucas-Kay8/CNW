import sys
from pypdf import PdfReader

def extract_text_to_file(pdf_path, txt_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n==== PAGE BREAK ====\n"
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    extract_text_to_file(sys.argv[1], sys.argv[2])
