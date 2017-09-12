
from matplotlib import colors

COLORS = {"grey": colors.colorConverter.to_rgb("#4D4D4D"),
          "blue": colors.colorConverter.to_rgb("#5DA5DA"),
          "orange": colors.colorConverter.to_rgb("#FAA43A"),
          "green": colors.colorConverter.to_rgb("#60BD68"),
          "pink": colors.colorConverter.to_rgb("#F17CB0"),
          "brown": colors.colorConverter.to_rgb("#B2912F"),
          "purple": colors.colorConverter.to_rgb("#B276B2"),
          "yellow": colors.colorConverter.to_rgb("#DECF3F"),
          "red": colors.colorConverter.to_rgb("#F15854"),
          "grey1": colors.colorConverter.to_rgb("#ffffff"),
          "grey2": colors.colorConverter.to_rgb("#f2f2f2"),
          "grey3": colors.colorConverter.to_rgb("#e6e6e6"),
          "grey4": colors.colorConverter.to_rgb("#d9d9d9"),
          "grey5": colors.colorConverter.to_rgb("#bfbfbf"),
          }

MAINSTREAM = {"color": COLORS["grey1"],
              "marker": "h",
              "pattern": "-----"
              }

NO_SHARING = {"color": COLORS["grey5"],
              "marker": "o",
              "pattern": "\\\\\\"
              }

MAX_SHARING = {"color": COLORS["grey3"],
              "marker": "d",
              "pattern": "xxxxx"
              }