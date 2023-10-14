# Extractor-mock
PDF、Officeファイルからテキストを抽出し、results配下にファイル出力する
 
## 使用方法
 ※ M2 MacOS, python 3.11で動作確認
  
1、抽出対象ファイルを`docs/`に置く  
2、対象拡張子のプログラムファイルの`local_path`に指定する  
3、対象拡張子のファイルを実行すると、`results/`に抽出結果がテキストファイルで出力される  
  
Docker使用の場合  
```bash
docker run --name test -d extractor-mock-image:latest bin/bash
docker exec -it test /bin/bash
```
 
## Note
- PDF
  - 鍵付き、コピー禁止ファイルには非対応
- Office
  - doc, pptなどの旧形式は非対応