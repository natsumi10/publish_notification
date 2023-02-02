# Publish 通知モジュール

Publish時にMattermost(Slackの様なチャットツール) へパブリッシュ情報を通知する為のモジュールです。

- publish_notification.sh
メインpythonファイルを実行する為のシェルスクリプトです。

config.yml に記述されたMattermostの設定を読み込み、Mattermostへ通知します。
実際に使用する為には config_with_fake_info.yml の説明に合わせてconfig.ymlファイルを同ディレクトリ内に作成する必要があります。 
