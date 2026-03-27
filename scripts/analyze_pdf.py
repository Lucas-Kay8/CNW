import sys
import fitz

def analyze_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    print(f"Total pages: {len(doc)}")
    for i, page in enumerate(doc):
        images = page.get_images()
        text = page.get_text()
        print(f"Page {i+1}: {len(images)} images, {len(text)} text chars.")
        if i >= 5:
            print("...")
            break

if __name__ == "__main__":
    analyze_pdf(sys.argv[1])
