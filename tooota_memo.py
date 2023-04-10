# Databricks notebook source
# MAGIC %md
# MAGIC ### 参考
# MAGIC - [Databricksレイクハウスプラットフォームにおける非構造化データの処理](https://qiita.com/taka_yayoi/items/5e5c8598028894b7527d#databricks%E3%83%AC%E3%82%A4%E3%82%AF%E3%83%8F%E3%82%A6%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E9%9D%9E%E6%A7%8B%E9%80%A0%E5%8C%96%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%87%A6%E7%90%86)
# MAGIC - [Databricksによるエンドツーエンドのディープラーニングパイプラインの管理](https://qiita.com/taka_yayoi/items/7de9c65eb0c3f67a28a0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### セットアップ
# MAGIC ###### 1. サンプル画像データのダウンロード
# MAGIC Create Sample Images.py 実行
# MAGIC 
# MAGIC ###### 2. 画像データを別のスコアリングフォルダーに格納
# MAGIC setup.py 実行
# MAGIC 
# MAGIC ###### 3. Databricks CLI 準備
# MAGIC az login  
# MAGIC token_response=$(az account get-access-token --resource 2ff814a6-3304-4ab8-85cb-cd0e6f879c1d)  
# MAGIC export DATABRICKS_AAD_TOKEN=$(jq .accessToken -r <<< "$token_response")  
# MAGIC databricks configure --aad-token
# MAGIC 
# MAGIC ###### 4. クラスタ作成
# MAGIC - CPU  
# MAGIC   databricks clusters create --json-file dl_demo_cpu.json  
# MAGIC   databricks clusters get --cluster-name "dl-demo-ml-no-cpu"  
# MAGIC - GPU  
# MAGIC   databricks clusters create --json-file dl_demo_ml_gpu.json  
# MAGIC   databricks clusters get --cluster-name "dl-demo-ml-gpu" 
# MAGIC 
# MAGIC ###### 5. パイプライン定義を更新
# MAGIC - Pipeline_DL_Image_score.json
# MAGIC   - existing_cluster_id：CPUクラスタIDを指定
# MAGIC   - notebook_path：oliver.koernig@databricks.comを自身のアカウントで更新
# MAGIC - Pipeline_DL_Image_train.json
# MAGIC   - existing_cluster_id：2つはGPUクラスタIDを指定しそれ以外はCPUクラスタIDを指定
# MAGIC   - notebook_path：oliver.koernig@databricks.comを自身のアカウントで更新
# MAGIC   - job_user：oliver.koernig@databricks.comを自身のアカウントで更新
# MAGIC 
# MAGIC ###### 6. パイプラインジョブを作成
# MAGIC databricks jobs create --json-file Pipeline_DL_Image_score.json  
# MAGIC databricks jobs create --json-file Pipeline_DL_Image_train.json  
