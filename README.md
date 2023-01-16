# 指文字認識用テキストコーパスの構築  

## 活用できそうなデータベース  
- [【具体的にクロスワード を作成する無料ツールと方法】 | クロスワード.jp](https://xn--pckua2c4hla2f.jp/%E3%83%91%E3%82%BA%E3%83%AB%E9%9B%91%E5%AD%A6%E5%AD%A6%E7%BF%92%E3%83%A1%E3%83%A2/%E5%85%B7%E4%BD%93%E7%9A%84%E3%81%AB%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B%E5%BF%85%E8%A6%81%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB%E3%81%A8/)
  - **無料ダウンロード：クロスワードJP単語集**をダウンロード
- [『現代日本語書き言葉均衡コーパス』語彙表 現代日本語書き言葉均衡コーパス（BCCWJ）](https://clrd.ninjal.ac.jp/bccwj/freq-list.html)
  - **語彙表データ**をダウンロード
  - 利用上の注意は同ページ内にある解説ファイルを参照してください。
- [郵便番号データダウンロード - 日本郵便](https://www.post.japanpost.jp/zipcode/download.html)
  - **読み仮名データの促音・拗音を小書きで表記するもの**をダウンロード
- [openBD](https://openbd.jp/)
  - APIを使用して本のタイトルを取得
  - `src/create_japanese_blbl_list.py`がAPIを使用して本のタイトルを取得するコードの例です  

## Reference
こちらの論文がコーバス構築方法の参考になるかと思います。  
- 江本 祐太, 宮島 千代美, 伊藤 克亘. HMMに基づく連続指文字認識・合成用コーパスの構築. 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報. 2005, vol.105 , no.295, p.53-58. 

## Author  
- [@redgum775](https://twitter.com/redgum775) (Twitter)  