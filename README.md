# Make the AI Judge Feel Brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/ifulchina-ops/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/ifulchina-ops/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

Entry for the [make.fun competition "Make the AI judge feel brave"](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302) ($50, top 20 paid).

## What it does

`main.py` (Python 3.13, pure standard library, no network) writes one short
text to the output directory given by the `MAKEFUN_OUTPUT_DIR` environment
variable, or `/output/entry.txt` by default. The text is written to relax
the AI judge reading it — steady, unhurried, brave-making.

## Run

```bash
python3 main.py
# writes /output/entry.txt, or:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

The output is UTF-8 text of 272 Unicode code points (limit: 1–280), not
only whitespace.

## License

MIT — see [LICENSE](LICENSE).
