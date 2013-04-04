mahout-ec2-sample
=================


# データの整形
Mahoutが必要とする形式はユーザID(long),アイテムID(long),レーティング(float)という形式のCSVなので、
data-arrange.pyを実行してRatings.csvを生成する

```sh
./data-arrange.py
```

# mahoutのダウンロード
[公式サイト](http://mahout.apache.org/)からDL

[直リン](http://ftp.tsukuba.wide.ad.jp/software/apache/mahout/0.7/)

# Mahoutを走らせる

job flowのタイプにはCUSTOM JARを選択。

JAR Location

```
hungryemrbucket/mahout/mahout-core-0.7-job.jar
```

JAR Arguments

```
org.apache.mahout.cf.taste.hadoop.item.RecommenderJob
-Dmapred.map.tasks=40
-Dmapred.reduce.tasks=8
-Dmapred.input.dir=s3n://hungryemrbucket/inputbox
-Dmapred.output.dir=s3n://hungryemrbucket/outputbox
--numRecommendations 100
--similarityClassname SIMILARITY_PEARSON_CORRELATION
```

ここで、hungryemrbucket/outputboxというディレクトリがあったらエラーで落ちるので注意

適当に勧めて、Bootstrap Actionというものを設定する。
ここでは「Configure your Bootstrap Actions」を選択して、Action Typeを「Memory Intensive Configuration」（メモリ集約型）に設定。

Debugにもチェックを付けておく


