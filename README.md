# Extractor-mock
PDF、Officeファイルからテキストのみを抽出するサンプルプログラム
 
## 使用方法
 ※ M2 MacOSで動作確認
```bash
git clone git@github.com:shogokaji/extractor-mock.git
docker run --name test -d extractor-mock-image:latest bin/bash
docker exec -it test /bin/bash
# 各ファイルを実行
python docx-sample.py
```
 
## Note
- PDF
  - 鍵付き、コピー禁止ファイルには非対応
- Office
  - doc, pptなどの旧形式は非対応