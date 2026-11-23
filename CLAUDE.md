# FCHL league site (HLM27 sim league)

Zachary is GM of the Chicago Blackhawks (CHI) in the FCHL, an online Hockey Legacy Manager 27 league that uses real player names. This repo publishes the league site on GitHub Pages: https://zacharymichaud.github.io/fchl-hml27/. It has six tabs: the GM trade report cards, plus team value, the cap board, standings, player stats and progression. It is the PHL site's build (`../phl-hml27`) pointed at this league.

Zachary is a developer. Keep answers short and decision-ready. The page is public to the whole league: only league-wide facts any GM could look up in the game go on it. Chicago's plans and notes live in Zachary's private workspace, not here.

Status: first published Nov 12, 2026 and rebuilt the same day from the four saves through Nov 2, 2026 (repo github.com/ZacharyMichaud/fchl-hml27; Pages serves the `main` branch). Rebuilt Nov 13, 2026 to show the overall the game shows, with the temporary streak or injury modifier (see Ratings in the PHL file); five players in NHL organizations carry one on the Nov 2 save. Rebuilt again the same day so Team value prices rating changes (see Team value). Rebuilt Nov 15, 2026 on the Dec 2, 2026 save, Nov 17 on the Jan 2, 2027 save and Nov 18 on the Feb 2, 2027 save. Rebuilt Nov 21 on the Feb 28, 2027 save and Nov 22 on the Apr 12, 2027 save (the regular season's last day), pushed together.

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
   - The Player stats `CHECK:` (players' goals don't add up to a team's) is a different thing: a player who scored for that team is missing from the save.

From the nine saves through Apr 12, 2027 (the regular season is over; the playoffs haven't started) the build gives 6 combined deals, 118 deals and 237 ledger rows; 32 teams over 1 period; 1,533 contracts through 2034-35; 1,344 games played and 0 to play; 684 skaters and 69 goalies in the NHL, 1,494 players in other leagues and 2 tables, with goals matching the standings for 30 of 32 teams; 1,302 rating changes over 5 monthly ticks. Two `CHECK:` lines, neither a trade. Florida's players have 285 goals against the team's 286: the 1 goal since the Feb 28 save belongs to a player in neither save nor among the retired, a generated depth player like Pittsburgh's below. Pittsburgh's have 322 against 324, the same 2 goals as on Feb 2 (225 against 227) and Feb 28 (260 against 262). The team's 66 goals since the Jan 2 save match its games, but 2 of them belong to a player who is in neither save nor among the retired players, most likely a generated depth player the game created and dropped between the two saves. No trade is involved, so nothing goes in `league.py`. The PHL's `site_stats.py` keeps the line of a player who leaves the save mid-season (`departed`), read from the last save that held him; that isn't ported here, and it couldn't recover this one.

## Trades

- 126 trades (#3832 to #3957). #3945 to #3957 are dated Feb 28, 2027, the trade deadline, and first appear in the Apr 12 save. #3935 and #3936 are dated Jan 2, 2027 and first appear in the Feb 2 save. #3832 to #3907 are all dated Sept 1, 2026: the league dealt through the whole preseason on one game day. The first save holds #3832 to #3857, the second up to #3906, the Oct 6 save adds #3907. #3908 to #3915 are dated Oct 6, 2026 and first appear in the Nov 2 save; none of them combine. #3916 to #3927 are dated Nov 2, 2026 and first appear in the Dec 2 save. #3928 to #3934 are dated Dec 2, 2026 and first appear in the Jan 2, 2027 save.
- The same-day rule (same two teams, one part at 5 assets) therefore also catches deals made weeks apart. Until Zachary says otherwise, only back-to-back trade numbers count as one deal:
  - Combined: BUF–SJS 3832+3833 (Celebrini), PIT–WPG 3849+3850+3851 (Connor; T. Hayes rides on a 7th-round swap that is swapped straight back) and NSH–QUE 3896+3897 (Marchment for Marchessault, with a swap of 2028 1sts). NJD–DET 3926+3927 (Nov 2, 2026): Faulk to New Jersey, Detroit keeping half his salary, for Gashilov, Rodrigues and three 3rds, then all of it back the same day with a different set of 3rds; one deal, confirmed by Zachary Nov 15, 2026. WSH–EDM 3950+3951 (Feb 28, 2027: Hutson and Leonard, then Sourdif for a 2nd) and WSH–DET 3954+3955+3957 (Wallinder, Seider, then Gibson for Nedeljkovic), both by the same-day rule. 3957 comes after PIT–VGK 3956, not straight after 3955, but Zachary said combine all three (Nov 22, 2026).
  - Left split (`KEEP_SEPARATE`, by the later trade): SJS–PHI 3881 (Bunting), CHI–SJS 3872 (Comrie), QUE–PHI 3882 (Moser), QUE–VGK 3885 (Burns), QUE–SEA 3886 (Landeskog), NSH–VGK 3901 (O'Reilly), NSH–QUE 3903 (Josi), NYI–NSH 3932 (back-to-back with 3931, Dowd for Stjernberg; Zachary said keep them separate, Nov 17, 2026).
- `CHECKED_TRADES` holds 3850, 3851, 3903, 3926 and 3927: flagged as claim-like (a pick goes out and comes back), kept as trades.
- No waiver claims or offer sheets yet. One three-team trade: #3869 (QUE, NYR, with NJD keeping half of Svechkov's salary).
- Player values in the Sept 1 saves are live in this league (2,124 of 2,174 NHL-owned players carry one, and they agree across the two saves), unlike the PHL's opening save, so nothing is marked stale. All three saves hold pick values.

## Team value

- One period so far, "2026-27 season": the preseason and the regular season to date. The Nov 2 save caches only 74 of 2,190 player values, so most of that save's values are copied or estimated, as the page's own table shows.
- The first save already holds trades #3832 to #3857, so they sit outside the value grades; the trade report cards cover them.
- A player whose rating changed since his last stored value keeps that value, moved by the game's value per overall point at his level. The value tool measures that rate from players stored at two overalls on the same contract. This league's saves can't measure it yet (9 such pairs after the Nov 2 tick), so since Nov 13, 2026 the tool uses the PHL's measurement at every level this league can't measure (same game). Before that, the 289 players under NHL contract whose rating changed by the Nov 2 save kept their old value, so development since Oct 6 was missing from every grade (prospects without an NHL contract are valued by potential, not rating, so theirs don't move). Chicago went from C+ to B and Buffalo from B- to A; moves-only grades didn't change.

## Open

- Zachary to confirm the combined and split groups above, and that 3850 and 3851 are the Connor trade's overflow rather than a waiver claim.
- Whether the PHL site should take the same Edge rule.
- GM names (`GM_NAMES` in `league.py`) if they should show on the cards.
