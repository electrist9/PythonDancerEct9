# CHANGELOG

このプロジェクトでの変更を記録します。

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づき、バージョン管理は [Semantic Versioning](https://semver.org/lang/ja/) に準拠します。

## [Unreleased]

### Added
- `--energy_curve` オプションを追加しました。正規化済みエネルギーにべき乗を適用し、値が 1 より大きいほど動作の強弱（緩急）が強調されます（例: 1.5〜3.0）。`create_actions` / `render_heatmap` に `energy_curve` 引数を追加し、CLI から渡せるようにしました。
- オーディオ読み込みヘルパー `_load_audio` を追加しました。`librosa.load` で読み込めない形式は `ffmpeg` で一時 WAV に変換してフォールバックします（m4a 等で発生する `LibsndfileError` 対策）。
- PyInstaller による単一ファイル実行ファイル化を追加しました。GUI 版 `PythonDancer-GUI.exe`（`gui.spec` / `ui_entry.py`）と CLI 版 `PythonDancer-CLI.exe`（`cli.spec` / `cli_entry.py`）を `--onefile` でビルドでき、Python 環境がなくても実行できます（ffmpeg は同梱されないため `PATH` が必要）。ビルド手順を README（英語・日本語）に記載しました。

### Changed
- Python 3.14 で動作するように依存関係を更新しました（`numpy>=2.3,<3`、`librosa>=0.11,<2`、`matplotlib>=3.10,<4`、`scipy>=1.15,<2`。`pyproject.toml` / `requirements.txt`）。
- `audioread` への直接依存を廃止し、`ffmpeg` フォールバックに置き換えました。
- Tk 9.0 対応のため、GUI の変数監視を `.trace("w", ...)` から `.trace_add("write", ...)` に変更しました（`TclError: bad option "variable"` の解消）。
- `--energy` を float 受け付けに変更し、範囲検証用の `frange` ヘルパーを追加しました。
- ヒートマップ出力を修正しました。空のバウンディングボックスで例外となる `bbox_inches`/`pad_inches` を除去し、`FigureCanvasAgg` でキャンバスを明示しました。あわせて CLI の `render_heatmap` 呼び出しにおける位置引数の誤り（`overflow` の二重指定、`center_offset` が `w` に渡っていた）をキーワード引数に修正しました。

### Notes
- 検証に使用した実楽曲サンプルで動作を確認しました。
