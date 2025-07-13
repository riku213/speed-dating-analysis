# Speed Dating Analysis - データマイニングプロジェクト

このプロジェクトは、Columbia Business Schoolのスピードデーティング実験データを使用して、恋愛における意思決定要因を機械学習で分析するプロジェクトです。

## 📊 プロジェクト概要

Speed Datingイベントで収集されたデータを用いて、「相手からもう一度会いたいと思われる」要因を決定木分析により解明します。特に男女別の分析を行い、性別による成功要因の違いを明らかにしています。

## 🎯 分析目的

- **主要な研究課題**: どのような特徴を持つ人が、相手から「もう一度会いたい」と思われやすいか？
- **副次的な研究課題**: 男性と女性で重要視される特徴に違いはあるか？
- **実用的な目標**: Speed Datingでの成功率向上のための科学的根拠に基づくアドバイス

## 📁 ファイル構成

```
DataMining_SpeedDating/
├── README.md                    # このファイル
├── Speed Dating Data.csv        # 元データ（8,378レコード、195特徴量）
├── Speed Dating Data Key.doc    # データ項目の説明書
├── LICENSE                      # ライセンス情報
├── environment.yml              # 環境設定ファイル
│
├── add_useful_column.py         # 特徴量エンジニアリング関数
├── add_useful_column.ipynb      # 特徴量追加の試行錯誤
│
├── data_arrange.ipynb           # データ前処理・探索的分析
├── analysis.ipynb              # メイン分析（男女別決定木）
├── decision_tree.ipynb         # 決定木モデルの詳細分析
└── decision_tree_sample.ipynb  # 決定木のサンプル実装
```

## 🔧 環境セットアップ

### 必要なライブラリ

```bash
# 基本的なデータ分析ライブラリ
pandas >= 1.5.0
numpy >= 1.21.0
matplotlib >= 3.5.0
seaborn >= 0.11.0

# 機械学習ライブラリ
scikit-learn >= 1.6.0  # 欠損値自動処理対応版
 
# Jupyter Notebook
jupyter >= 1.0.0
nbformat >= 4.2.0

# オプション（インタラクティブ可視化）
plotly >= 5.0.0
```

### インストール方法

```bash
# condaを使用する場合
conda env create -f environment.yml
conda activate speed-dating-analysis

# pipを使用する場合
pip install pandas numpy matplotlib seaborn scikit-learn jupyter plotly
```

## 📋 データセット詳細

### データ概要
- **出典**: Columbia Business School Speed Dating Experiment
- **期間**: 2002-2004年
- **参加者数**: 552名（男性277名、女性275名）
- **レコード数**: 8,378件（各マッチングペア）
- **特徴量数**: 195個

### 主要な変数
- **目的変数**: `dec_o` (相手から「もう一度会いたい」と思われたか: 0=No, 1=Yes)
- **基本情報**: 年齢、性別、人種、専攻、職業志望
- **価値観**: 魅力・誠実さ・知性・楽しさ・野心・共通興味の重視度
- **相手への評価**: 6つの観点での相手に対する評価（1-10点）
- **趣味・活動**: 17種類の余暇活動への参加頻度
- **自己評価**: 自分自身への5つの観点での評価

## 🔍 分析手法

### 1. データ前処理
- 欠損値の確認と処理（scikit-learn 1.6.1の自動処理機能を活用）
- 特徴量エンジニアリング（年齢差、ワンホットエンコーディング）
- データクリーニング

### 2. 探索的データ分析 (EDA)
- 基本統計量の確認
- 男女別の成功率分布
- 特徴量間の相関分析

### 3. 機械学習モデル
- **決定木分類器** (DecisionTreeClassifier)
  - 解釈しやすさを重視
  - 過学習防止（最大深度10、最小分割サンプル数20）
  - クラス不均衡対応（balanced class weights）

### 4. 男女別分析
- 男性・女性それぞれに特化した決定木モデル
- 特徴量重要度の比較分析
- 相関係数 vs 決定木重要度の違いの検証

## 📈 主要な発見

### 全体的な傾向
- **年齢差の影響**: 年上の相手からの方が好意を持たれやすい
- **相手への評価**: 楽しさ（fun）や魅力（attr）の評価が重要
- **価値観の一致**: 共通の興味（shar）が成功要因

### 男女差
- **男性**: [実行結果に基づいて更新予定]
- **女性**: [実行結果に基づいて更新予定]

### モデル性能
- **全体モデル精度**: [実行結果に基づいて更新予定]
- **男性特化モデル精度**: [実行結果に基づいて更新予定]  
- **女性特化モデル精度**: [実行結果に基づいて更新予定]

## 🚀 使用方法

### 1. 基本分析の実行

```bash
# Jupyter Notebookを起動
jupyter notebook

# 以下の順序でノートブックを実行
1. data_arrange.ipynb     # データの前処理と基本的な探索
2. analysis.ipynb         # メイン分析（男女別決定木）
3. decision_tree.ipynb    # 決定木の詳細分析と可視化
```

### 2. カスタム分析

```python
# 独自の特徴量を追加
from add_useful_column import add_useful_columns
df = add_useful_columns(df)

# 男女別分析の実行例
from sklearn.tree import DecisionTreeClassifier

# 男性データで訓練
clf_male = DecisionTreeClassifier(random_state=42, max_depth=10)
clf_male.fit(X_male, y_male)

# 特徴量重要度の確認
feature_importance = clf_male.feature_importances_
```

## 📊 可視化機能

### 決定木の可視化
- 階層別分割表示（深さ2-5を別々に表示）
- ノードサイズ比例表示
- Seabornによる美しい可視化

### 統計分析
- 混同行列のヒートマップ
- ROC/PR曲線
- 特徴量重要度の比較チャート
- 相関行列のヒートマップ

### インタラクティブ分析
- Plotlyによるズーム可能なグラフ
- 特徴量重要度の動的比較
- 深さ-精度関係の可視化

## 🔬 技術的特徴

### scikit-learn 1.6.1の活用
- **自動欠損値処理**: 前処理不要で欠損値を含むデータの学習が可能
- **決定木の改良**: より安定した分岐アルゴリズム
- **性能向上**: 従来のバージョンより高速・高精度

### 特徴量エンジニアリング
- **年齢差の計算**: `age_diff = age_o - age`
- **ワンホットエンコーディング**: 人種、専攻、職業の詳細分類
- **相互作用項**: 重要な特徴量間の組み合わせ効果

## 📝 今後の拡張予定

### 分析手法の拡張
- [ ] ランダムフォレスト・勾配ブースティングの比較
- [ ] ニューラルネットワークによる非線形関係の探索
- [ ] クラスタリング分析（参加者の類型化）

### セグメント分析
- [ ] 年齢層別の分析
- [ ] 職業・専攻別の分析
- [ ] 人種・文化的背景別の分析

### 実用化
- [ ] Speed Datingアドバイスシステムの構築
- [ ] リアルタイム成功率予測
- [ ] マッチングアルゴリズムの開発

## 🤝 貢献方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/新機能`)
3. 変更をコミット (`git commit -am '新機能を追加'`)
4. ブランチにプッシュ (`git push origin feature/新機能`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 📚 参考文献

- Fisman, R., Iyengar, S. S., Kamenica, E., & Simonson, I. (2006). Gender differences in mate selection: Evidence from a speed dating experiment. *The Quarterly Journal of Economics*, 121(2), 673-697.
- Speed Dating Data: [Kaggle Dataset](https://www.kaggle.com/annavictoria/speed-dating-experiment)
- Columbia Business School Speed Dating Experiment

## 📧 お問い合わせ

プロジェクトに関する質問や提案がありましたら、以下の方法でお気軽にお問い合わせください：

- GitHub Issues: [プロジェクトページ](https://github.com/riku213/speed-dating-analysis)
- Email: [お問い合わせ先]

---

**最終更新**: 2025年7月13日  
**作成者**: riku213  
**バージョン**: 1.0.0
