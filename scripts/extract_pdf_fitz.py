import sys
import fitz

def extract_text_to_file(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n==== PAGE BREAK ====\n"
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Extracted {len(text)} characters.")

if __name__ == "__main__":
    extract_text_to_file(sys.argv[1], sys.argv[2])
