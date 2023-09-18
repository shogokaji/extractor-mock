import openpyxl

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

print(extract_excel("./docs/sample.xlsx"))