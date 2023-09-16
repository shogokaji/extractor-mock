from pdfminer.high_level import extract_text
text = extract_text('docs/access_log_1 15.pdf')
print(text)