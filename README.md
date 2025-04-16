# github actions sandbox

[![pytest status](https://github.com/yuto-kimura-g/github-actions-sandbox/actions/workflows/pytest.yml/badge.svg)](https://github.com/yuto-kimura-g/github-actions-sandbox/actions/workflows/pytest.yml)

github actions の練習

NOTE
- 設定ファイルは [`.github/`](./.github/) にある
- actionは、信頼できる団体／作者のもの(github.com/actions/* や github.com/github/* など)を使う
- 最新版を使用する：ネットの情報は古いものが多いので注意。古いとエラーで動かないこともある。dependabotを導入したので、もう大丈夫のはず
- `.yaml`と`.yml`は区別されるらしい（github actionsはyml）
- ラベルは k/k (github.com/kubernetes/kubernetes) を参考にしてみた

## References
- https://docs.github.com/ja/actions/automating-builds-and-tests/building-and-testing-python
- https://github.com/actions/stale
- https://github.com/actions/labeler
- https://github.com/actions/setup-python
- https://github.com/actions/checkout
- https://github.com/actions/upload-artifact
- https://github.com/actions/download-artifact
- https://github.com/kubernetes/website
- https://docs.github.com/ja/rest/pulls/pulls?apiVersion=2022-11-28#get-a-pull-request
- https://cli.github.com/manual/gh_pr_view
- https://docs.github.com/ja/actions
