from pdfminer.high_level import extract_text
text = extract_text('docs/quotation.pdf')
print(text)