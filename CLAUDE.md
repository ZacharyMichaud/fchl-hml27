# FCHL league site (HLM27 sim league)

Zachary is GM of the Chicago Blackhawks (CHI) in the FCHL, an online Hockey Legacy Manager 27 league that uses real player names. This repo publishes the league site on GitHub Pages: https://zacharymichaud.github.io/fchl-hml27/. It has six tabs: the GM trade report cards, plus team value, the cap board, standings, player stats and progression. It is the PHL site's build (`../phl-hml27`) pointed at this league.

Zachary is a developer. Keep answers short and decision-ready. The page is public to the whole league: only league-wide facts any GM could look up in the game go on it. Chicago's plans and notes live in Zachary's private workspace, not here.

Status: first published Nov 12, 2026 and rebuilt the same day from the four saves through Nov 2, 2026 (repo github.com/ZacharyMichaud/fchl-hml27; Pages serves the `main` branch).

## How it relates to the PHL site

- The scripts are copies of the PHL site's, with every league fact moved into `league.py`: the name, the home team, the saves folder, team names (Quebec plays in Colorado's place) and the trade lists.
- `../phl-hml27/CLAUDE.md` documents the save format, values, ratings, the grading rules and the page conventions. All of it applies here except what this file says.
- Differences from the PHL scripts, to keep in mind when porting a change either way:
  - Edge divides by the value moved counted at its size, |in| + |out| per trade, not by in + out. A contract with negative value made Seattle's Edge −574% under the PHL formula (it is −46.1% here). Quebec is the only grade it changes (B+ to B).
  - The trades lede says "on Sep 1, 2026" when every trade is on one game day.
  - Team value: with a single period the table shows one grade column, not the period and an identical Overall. The value tool is found one or two folders above the saves and is called with `--league fchl`.
  - Standings: "Under the hood" is hidden until a game is played. The race constants are the PHL's fit (same game, same roster file); refit with `fit_race_model.py` after this league's first season.
  - Player stats: the preseason gets a table until the regular season's first game, so the tab isn't empty on opening day.
  - Progression: a short note stands in until a league's first tick (this one's came on Nov 2, 2026).

## Files

- `league.py`: the league's facts and trade lists. The first place to look.
- `build_report_cards.py`: builds `report.html` from the saves, then runs `site_pages.py` for the other tabs. `python build_report_cards.py`, about a minute.
- `site_shell.py`, `site_pages.py`, `site_value.py`, `site_cap.py`, `site_standings.py`, `site_stats.py`, `site_progression.py`, `fit_race_model.py`: as in the PHL repo.
- `index.html` (the loader) and `report.html`, `value.html`, `cap.html`, `standings.html`, `stats.html`, `progression.html`: generated.
- `../fchl/saves/`: the official league saves, outside this folder. Never commit saves.
- `../tools/value_grades.py`: the value tool, shared with the PHL. Its `LEAGUES["fchl"]` phase list needs a new entry as each season unfolds.

## After each sim block

1. The new save zip goes in `../fchl/saves/`.
2. `python build_report_cards.py`, check the output (counts, a few cards, every tab in a browser), commit the six pages plus any script changes, push. Pages deploys on push.
   - A `CHECK:` line is a move entered like a waiver claim or an offer sheet. Ask Zachary which it was and add its ids to the matching list in `league.py`.
   - A new "combined" group in the output needs the same question (see Trades).

From the four saves through Nov 2, 2026 the build gives 3 combined deals, 80 deals and 161 ledger rows; 32 teams over 1 period; 1,518 contracts through 2034-35; 229 games played and 1,115 to play; 614 skaters and 65 goalies in the NHL, 1,349 players in other leagues and 2 tables, with goals matching the standings for 32 of 32 teams; 469 rating changes over 1 monthly tick. No `CHECK:` lines.

## Trades

- 84 trades. #3832 to #3907 are all dated Sept 1, 2026: the league dealt through the whole preseason on one game day. The first save holds #3832 to #3857, the second up to #3906, the Oct 6 save adds #3907. #3908 to #3915 are dated Oct 6, 2026 and first appear in the Nov 2 save; none of them combine.
- The same-day rule (same two teams, one part at 5 assets) therefore also catches deals made weeks apart. Until Zachary says otherwise, only back-to-back trade numbers count as one deal:
  - Combined: BUF–SJS 3832+3833 (Celebrini), PIT–WPG 3849+3850+3851 (Connor; T. Hayes rides on a 7th-round swap that is swapped straight back) and NSH–QUE 3896+3897 (Marchment for Marchessault, with a swap of 2028 1sts).
  - Left split (`KEEP_SEPARATE`, by the later trade): SJS–PHI 3881 (Bunting), CHI–SJS 3872 (Comrie), QUE–PHI 3882 (Moser), QUE–VGK 3885 (Burns), QUE–SEA 3886 (Landeskog), NSH–VGK 3901 (O'Reilly), NSH–QUE 3903 (Josi).
- `CHECKED_TRADES` holds 3850, 3851 and 3903: flagged as claim-like (a pick goes out and comes back), kept as trades.
- No waiver claims or offer sheets yet. One three-team trade: #3869 (QUE, NYR, with NJD keeping half of Svechkov's salary).
- Player values in the Sept 1 saves are live in this league (2,124 of 2,174 NHL-owned players carry one, and they agree across the two saves), unlike the PHL's opening save, so nothing is marked stale. All three saves hold pick values.

## Team value

- One period so far, "2026-27 season": the preseason and the regular season to date. The Nov 2 save caches only 74 of 2,190 player values, so most of that save's values are copied or estimated, as the page's own table shows.
- The first save already holds trades #3832 to #3857, so they sit outside the value grades; the trade report cards cover them.

## Open

- Zachary to confirm the combined and split groups above, and that 3850 and 3851 are the Connor trade's overflow rather than a waiver claim.
- Whether the PHL site should take the same Edge rule.
- GM names (`GM_NAMES` in `league.py`) if they should show on the cards.
