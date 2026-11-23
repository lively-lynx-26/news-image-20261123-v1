# The World in One Day — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/lively-lynx-26/news-image-20261123-v1/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/lively-lynx-26/news-image-20261123-v1/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Thirty-five dated stories from Monday 23 November 2026, across seven regions — Europe, the Middle East, Asia, the Americas, Africa, Oceania and the wider world — checked against two sources where possible to a 13:00 UTC press time. The lead stories: COP31 ends in failure, with the 1.5C overshoot now inevitable; a 153-drone overnight attack on Ukraine kills 11 in Dymer; and Ukrainian sea drones sink the Russian corvette Merkury off Benghazi. Every item carries a verification tag — CONFIRMED for tallies verified by two sources, REPORTED for single-source or official-but-unconfirmed claims, CLAIM for attributed but unverified statements, PENDING for stories not yet settled — and a DATE CHECK footer keeps earlier news (the penny law, the California–OpenAI suit, the Mount Fuji warning) out of Monday's headlines.

## How to run

`python3 main.py`

It writes `entry.png` (1024x1024, 211,610 bytes) to `$MAKEFUN_OUTPUT_DIR`, falling back to `<repo>/output` when that variable is unset or not writable. The copy is byte-identical across runs, and the program needs no network access.

## The image

All text is code-rendered with PIL and DejaVu fonts — no diffusion model ever touches a word, so nothing is garbled and no story is invented. The three hero panels are code-drawn scenes (the Antalya summit hall, Kyiv under drone attack, sea drones off Benghazi), and the world map is a hand-authored dotted landmask with numbered pins for stories 1–13 and dots for briefs 14–35. No diffusion images and no copied photographs appear anywhere in the entry.

## Verification

The front page was re-rendered in the build session and reproduced byte-identically: 211,610 bytes, sha256 `b5bf967033272e4c60ac33e421a238a09a6547fad62ab18d34676e921d189d8c`, 1024x1024. `main.py` re-verifies the copy on every run — PNG magic, exact size and sha256 — and exits non-zero unless all three checks pass.

<sub>Entered on [make.fun](https://make.fun/?ref=efj00y0p&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
