import openpyxl
import secrets

def extract_excel(filepath: str):
    # data_only=Trueで値のみを取得
    book = openpyxl.load_workbook(filepath, data_only=True)
    results = ""
    # シートごとに抽出
    for s_name in book.sheetnames:
        sheet = book[s_name]
        for cells in tuple(sheet.rows):
            for cell in cells:
                if cell.value != None:
                    # 全角スペースを削除
                    text = str(cell.value).replace('\u3000', '')
                    results += text
    return results

local_path = "./docs/your_file_name.xlsx"

with open(f'./results/xlsx-result-{secrets.token_urlsafe(6)}.txt', 'w') as file:
    file.write(extract_excel(local_path))