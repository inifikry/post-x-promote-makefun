[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/inifikry/post-x-promote-makefun/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/inifikry/post-x-promote-makefun/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

# Promote make.fun's make-your-own-bounty post on X

Entry for the make.fun bounty
[post-x-promote-make-your-own-bounty-01](https://make.fun/c/post-x-promote-make-your-own-bounty-01)
($250, scored by the post's replies + reposts + quotes).

The post itself is the entry: a quote of make.fun's post
https://x.com/makefunai/status/2124915864336236646, posted from
[@tuyullabs](https://x.com/tuyullabs/status/2125048731024388324) with a
photo of its own attached. Its text (in `post-text.txt`) carries make.fun,
a tag of @makefunai, and the make.fun play code `makefun-recipe-pocket-cub`.

## How it works

`main.ts` (Node 22, standard library only) copies `POST.json` to
`/output/POST.json`, where the gate reads the post's address. The house
reads the post's counts from X itself; nothing written here is scored.
`draw_post.py` drew the attached photo (`post-photo.png`) with Pillow
from make.fun's official press-kit assets.
