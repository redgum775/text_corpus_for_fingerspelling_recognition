# 指文字認識用テキストコーパスの構築  
指文字認識用テキストコーパス構築の前に、日本の指文字が何種類あるか考えよう。  
- 50音（あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん）46種  
- 濁音（ゔがぎぐげござじずぜぞだぢづでどばびぶべぼ）21種  
- 半濁音（ぱぴぷぺぽ）5種  
- 拗音・促音（ぁぃぅぇぉっゃゅょゎ）10種  
- 長音（ー｜）2種  

合計なんと**84種**。  
実際に指文字を覚えるときは、50音を覚えさえすれば、50音のときと手指の形状は同じで、指文字を横に動かすと濁音、上向きに動かすと半濁音、手前に引くと拗音・促音を表すことができる。それでも**46種**の手指の形状を覚える必要がる。  
<br>
音声コーバスでは音素を最小単位とし、母音（C）、子音（V）の三つ組みCVC・VCVがバランスよく収録されるよう、考えられて構築されている。指文字コーパスにおける最小単位は、さっき挙げた84種の文字として考える。連続する文字のバランスを考慮するため二つの文字の組みをバランスよく収録するとき、二つ組の指文字パターンは $84^2=7056$ パターンになる。日本語として出現頻度の低いパターンもあるため、網羅する必要はないかもしれないが多くのテキストが必要となる。  
<br>

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
  - `src/create_japanese_blbl_list.py`がAPIを使用して日本の書誌タイトルを取得するコードの例です  

## Reference
こちらの論文がコーバス構築方法の参考になるかと思います。  
- 江本 祐太, 宮島 千代美, 伊藤 克亘. HMMに基づく連続指文字認識・合成用コーパスの構築. 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報. 2005, vol.105 , no.295, p.53-58. 

## Author  
- [@redgum775](https://twitter.com/redgum775) (Twitter)  
