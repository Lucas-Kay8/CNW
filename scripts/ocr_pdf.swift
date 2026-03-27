import Cocoa
import Quartz
import Vision

func ocrPDF(url: URL) {
    guard let pdfDocument = PDFDocument(url: url) else {
        print("Failed to load PDF")
        return
    }

    let pageCount = pdfDocument.pageCount
    for i in 0..<pageCount {
        guard let page = pdfDocument.page(at: i) else { continue }
        let pageRect = page.bounds(for: .mediaBox)
        
        // Render page to image
        let image = NSImage(size: pageRect.size)
        image.lockFocus()
        guard let context = NSGraphicsContext.current?.cgContext else {
            image.unlockFocus()
            continue
        }
        
        context.setFillColor(NSColor.white.cgColor)
        context.fill(pageRect)
        
        page.draw(with: .mediaBox, to: context)
        image.unlockFocus()
        
        guard let tiffData = image.tiffRepresentation,
              let bitmap = NSBitmapImageRep(data: tiffData),
              let cgImage = bitmap.cgImage else {
            continue
        }
        
        let request = VNRecognizeTextRequest { (request, error) in
            guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
            var pageText = ""
            for observation in observations {
                guard let topCandidate = observation.topCandidates(1).first else { continue }
                pageText += topCandidate.string + "\n"
            }
            print("--- Page \(i + 1) ---")
            print(pageText)
        }
        
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["zh-Hans", "zh-Hant", "en-US"]

        let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        do {
            try handler.perform([request])
        } catch {
            print("Error parsing page \(i+1): \(error)")
        }
    }
}

if CommandLine.arguments.count < 2 {
    print("Usage: swift ocr_pdf.swift <path_to_pdf>")
    exit(1)
}

let path = CommandLine.arguments[1]
let url = URL(fileURLWithPath: path)
ocrPDF(url: url)
