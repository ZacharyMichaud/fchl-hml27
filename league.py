"""What is specific to this league. The other scripts are the PHL site's, reading their league facts from here."""
import os

NAME = "FCHL"  # the brand in the tab bar and in every page title
FRONT_OFFICE = "Chicago Blackhawks front office"  # the footer's byline
HOME_TEAM = "CHI"  # the team a page opens on when its link names none
SAVES = os.path.join("..", "fchl", "saves")  # the official league saves, outside the repo
OPENED = "September 2026"  # when the league opened, for the method text
FIRST_SEASON = 2026  # the league's first season; stat lines from before it are real-life history
VALUE_LEAGUE = "fchl"  # the phase list ../tools/value_grades.py grades this league by

# Quebec (the Nordiques) plays in Colorado's place in this league.
TEAM_NAMES = {"ANA": "Anaheim", "BOS": "Boston", "BUF": "Buffalo", "CAR": "Carolina", "CBJ": "Columbus", "CGY": "Calgary",
              "CHI": "Chicago", "DAL": "Dallas", "DET": "Detroit", "EDM": "Edmonton", "FLA": "Florida",
              "LAK": "Los Angeles", "MIN": "Minnesota", "MTL": "Montreal", "NJD": "New Jersey", "NSH": "Nashville",
              "NYI": "NY Islanders", "NYR": "NY Rangers", "OTT": "Ottawa", "PHI": "Philadelphia", "PIT": "Pittsburgh",
              "QUE": "Quebec", "SEA": "Seattle", "SJS": "San Jose", "STL": "St. Louis", "TBL": "Tampa Bay", "TOR": "Toronto",
              "UTA": "Utah", "VAN": "Vancouver", "VGK": "Vegas", "WPG": "Winnipeg", "WSH": "Washington"}
# GM names: fill this in once and they show on the cards.
GM_NAMES = {}

# Trades (see build_report_cards.py for what each list does). Trade ids as strings.
# Same-day trades between the same two teams are combined into one deal when a part reaches the game's
# 5 assets a side. KEEP_SEPARATE lists groups to leave split anyway (any one of their ids is enough);
# EXTRA_MERGES lists other groups to combine, as tuples of ids.
# The whole preseason is one day in the game (Sept 1, 2026), so the same-day rule also catches deals made weeks
# apart. Until Zachary says otherwise, only back-to-back trade numbers count as one deal: BUF-SJS 3832+3833
# (Celebrini), PIT-WPG 3849+3850+3851 (Connor) and NSH-QUE 3896+3897. Left split, by their later trade: SJS-PHI
# 3881 (Bunting), CHI-SJS 3872 (Comrie), QUE-PHI 3882 (Moser), QUE-VGK 3885 (Burns), QUE-SEA 3886 (Landeskog),
# NSH-VGK 3901 (O'Reilly) and NSH-QUE 3903 (Josi).
KEEP_SEPARATE = {"3881", "3872", "3882", "3885", "3886", "3901", "3903"}
EXTRA_MERGES = [("3896", "3897")]
# Moves entered in the game as trades that are not trades, so they are left out.
WAIVER_CLAIMS = set()
OFFER_SHEETS = set()
# Entries the build flagged with a CHECK line that turned out to be real trades.
# PIT-WPG 3850 and 3851: T. Hayes rides with the Connor trade (3849, already at 5 assets) on a 7th-round swap
# that is swapped straight back. NSH-QUE 3903: the Josi trade returns the 2027 3rd that 3896 sent.
# NJD-DET 3926 and 3927 (Nov 2, 2026): Faulk to New Jersey for Gashilov, Rodrigues and three 3rds, then all of it
# back the same day with a different set of 3rds; graded as one deal (confirmed by Zachary, Nov 15, 2026).
CHECKED_TRADES = {"3850", "3851", "3903", "3926", "3927"}
