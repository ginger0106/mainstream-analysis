
from matplotlib import colors

# http://colorbrewer2.org/#type=diverging&scheme=Spectral&n=4
COLORLISTS = {4: [
                colors.colorConverter.to_rgb("#d53e4f"),
                colors.colorConverter.to_rgb("#fdae61"),
                colors.colorConverter.to_rgb("#abdda4"),
                colors.colorConverter.to_rgb("#2b83ba")
                ],
              8: [
                colors.colorConverter.to_rgb("#d53e4f"),
                colors.colorConverter.to_rgb("#f46d43"),
                colors.colorConverter.to_rgb("#fdae61"),
                colors.colorConverter.to_rgb("#fee08b"),
                colors.colorConverter.to_rgb("#e6f598"),
                colors.colorConverter.to_rgb("#abdda4"),
                colors.colorConverter.to_rgb("#66c2a5"),
                colors.colorConverter.to_rgb("#3288bd")
                ]
              }


COLORS = {"grey": colors.colorConverter.to_rgb("#4D4D4D"),
          "blue": colors.colorConverter.to_rgb("#2B83BA"),
          "orange": colors.colorConverter.to_rgb("#FDAE61"),
          "green": colors.colorConverter.to_rgb("#ABDDA4"),
          "seafoam": colors.colorConverter.to_rgb("#9DD192"),
          "pink": colors.colorConverter.to_rgb("#F2686D"),
          "brown": colors.colorConverter.to_rgb("#B2912F"),
          "purple": colors.colorConverter.to_rgb("#C988BB"),
          "yellow": colors.colorConverter.to_rgb("#DECF3F"),
          "red": colors.colorConverter.to_rgb("#d7191c"),
          "grey1": colors.colorConverter.to_rgb("#ffffff"),
          "grey2": colors.colorConverter.to_rgb("#f2f2f2"),
          "grey3": colors.colorConverter.to_rgb("#e6e6e6"),
          "grey4": colors.colorConverter.to_rgb("#d9d9d9"),
          "grey5": colors.colorConverter.to_rgb("#bfbfbf"),
          }

MAINSTREAM = {"color": COLORS["orange"],
              "marker": "h",
              "pattern": "---",
              "label": "Mainstream"
              }

NO_SHARING = {"color": COLORS["blue"],
              "marker": "o",
              "pattern": "\\\\",
              "label": "No Sharing"
              }

MAX_SHARING = {"color": COLORS["red"],
              "marker": "d",
              "pattern": "xxxxx",
              "label": "Max Sharing"
              }
