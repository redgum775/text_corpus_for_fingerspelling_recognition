import requests
from more_itertools import chunked
import csv

OPENBD_ENDPOINT = 'https://api.openbd.jp/v1/'
JA_ISBN_CODE = '9784'
BATCH_SIZE = 10000

# 全てのISBNコードを取得
def get_coverage():
  return requests.get(OPENBD_ENDPOINT + 'coverage').json()

# 書誌データを取得
def get_bibl_data(items):
  return requests.post(OPENBD_ENDPOINT + 'get', data={'isbn': ','.join(items)}).json()

# 全てのISBNコードを取得
coverage = get_coverage()

# 全てのISBNコードうち日本の書籍コードだけ抽出
japanese_isbn_list = list(filter(lambda isbn: isbn[:4]==JA_ISBN_CODE, coverage))

print(f'Total Japanese bibliography: {len(japanese_isbn_list)} books')

# ISBNのリストを10000件単位に分割
chunked_japanese_isbn_list = chunked(japanese_isbn_list, BATCH_SIZE)

# CSV出力の設定
bibl_title_file = open('output/bibl_title.csv', 'w', encoding='utf-8', newline="")
bibl_title_writer = csv.writer(bibl_title_file)
bibl_title_writer.writerow(['id','isbn','title'])

# ISBNとタイトルをCSV形式で出力
idx = 0
for isbn_list in chunked_japanese_isbn_list:
  result = get_bibl_data(isbn_list)
  for bibl in result:
    idx += 1
    if bibl is None:
      continue
    # ここで書誌1件単位の処理
    isbn = bibl['summary']['isbn']
    title = bibl['summary']['title']
    bibl_title_writer.writerow([idx, isbn, title])

bibl_title_file.close()