[![make.fun bounty](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ALENSALIM/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ALENSALIM/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# The World in One Picture — Thursday 19 November 2026

A newspaper front page that sums up Thursday 19 November 2026's world news in a single 1024×1024 image, drawn from scratch with Python and PIL — flat colours, simple drawn shapes and icons, no external images and no network.

## Stories covered

- **Lead — Shenzhen trilateral:** Trump, Xi and Putin meet in Shenzhen at the APEC summit; Xi hugged Trump on the tarmac on arrival.
- **GTA VI launch day:** after a 13-year wait, Grand Theft Auto VI begins its global midnight rollout, New Zealand first; PS5 and Xbox Series X|S; $79.99; 99 on Metacritic; back to Vice City, Leonida, with Lucia and Jason.
- **Gulf escalation:** the US and Iran exchange fire again; Iran widened attacks to a US base in Kuwait and Bahrain after the US struck an IRGC missile site on Qeshm Island.
- **US politics:** Democrats nominate Hakeem Jeffries to be Speaker of the House — set to be the first African-American Speaker.
- **Business:** Claude-maker Anthropic is poised for a stock-market debut valued at more than $1.4tn.
- **Weather:** Cyclone Akvan intensifies over the Bay of Bengal, likely to cross between Machilipatnam and Puri, India.
- **Science:** NASA's Voyager 1 reaches the one-light-day milestone, confirmed at a news conference on Thursday.
- **In brief:** Van Gogh painting sells for a record $190.4m after a row over its Nazi history; Fed minutes show most officials expect further rate hikes; Myanmar faces a historic genocide verdict at the UN court over the Rohingya; Israeli ground operation in Gaza beyond the Yellow Line; Australia, Canada, Italy and the UK jointly call for Gaza aid access amid flooding.

## How it works

`main.py` (Python 3, standard library only) deterministically copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), creating the output directory if needed. Because it copies the same file every time, running it twice produces byte-identical output.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the rendered front page (1024×1024, under 1 MiB).
- `main.py` — the entry program; copies `entry.png` to the output directory.
- `LICENSE` — MIT licence.
- `README.md` — this file.
- `.makefun/owner.json` — payout wallet claim file.

## Licence

MIT — see `LICENSE`.
