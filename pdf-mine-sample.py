from pdfminer.high_level import extract_text
import secrets

local_path = "./docs/your_file_name.pdf"

with open(f'./results/pdf-result-{secrets.token_urlsafe(6)}.txt', 'w') as file:
    file.write(extract_text(local_path))