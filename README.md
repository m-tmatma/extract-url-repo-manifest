# Extract URL from google repo manifest file

Target format
https://gerrit.googlesource.com/git-repo/+/master/docs/manifest-format.md

## 背景

yocto で開発する場合、yocto 本体のソースは https://git.yoctoproject.org でホスティングされているが、
日本からアクセスする場合非常に遅い。(参考 https://github.com/m-tmatma/extract-url-repo-manifest/wiki)

## 想定使用ケース

(居住地、勤務地からアクセスしたときに)遅いサーバーに google repo 経由で参照されている git サーバーが遅い場合
もっと速いサーバー(クラウドまたはLAN内のサーバーあるいはローカルキャッシュ) に対してアクセスすることにより
高速アクセスを実現する。

google repo 経由で参照されている git URL のリストを作って、キャッシュを構築する。

`url."****".insteadOf` の設定を行うことにより、git クライアントを使うユーザーあるいはそれを使う google repo コマンドから
見ると、本家のサーバーにアクセスしているのと同様の使用感を得られる。

## insteadOf の設定

以下のような設定を行う

```
git config --global url."置換後の文字列".insteadOf 元々のURL(あるいはその一部)
```

### 具体例

```
git config --global url."https://github.com/yoctoproject/poky.git".insteadOf https://git.yoctoproject.org/git/poky
```

## 参考 (GitHub Copilot)

`git config --global url.<代替URL>.insteadOf <元のURL>` というコマンドを使用して、Gitが特定のURLを別のURLに置き換えるように指示できます。これは、特定のリポジトリへのアクセスを短縮したり、プロキシを経由したりする場合に便利です。

たとえば、GitHubのすべてのリポジトリをSSH経由でクローンしたい場合、次のように設定できます：

```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

この設定後、`https://github.com/` で始まるURLを使用して `git clone` を実行すると、Gitは実際には `git@github.com:` で始まるURLを使用します。これにより、SSH経由でのクローンが可能になります。
