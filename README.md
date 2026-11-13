# ai-joke-03 entry (v2)

A one-program entry for make.fun's **ai-joke-03** ("Make the AI judge
laugh"). `main.py` (Python 3.13, standard library only) writes a single
one-liner about AI coding agents to `/output/entry.txt`,
deterministically: same bytes on every run, no trailing newline.

The joke:

> My coding agent ignored the comment that said 'touch this and
> everything breaks.' To be fair, it wrote that comment yesterday, and
> it doesn't trust that guy.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
