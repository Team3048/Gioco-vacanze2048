#import colori.py
#COLOR HEX --> ESEMPIO: FC(RED), EF(GREEN), E6(BLUE)

GRID_COLOR = "#a39489" # RGB % COLORE DELLA GRIGLIA: 36.38% RED, 33.04 % GREEN, 30.58 % BLUE 
EMPTY_CELL_COLOR  = "#c2b3a9" # RGB % COLORE DI CELLE VUOTE : 35.79% RED, 33.03% GREEN, 31.18% BLUE
SCORE_LABEL_FONT = ("Verdana", 20) # CARATTERE ETICHETTA SCORE
SCORE_FONT = ("Tahoma", 32, "bold") # FONT PUNTEGGIO
GAME_OVER_FONT = ("Georgia Pro", 48, "bold") # FONT SCONFITTA 
GAME_OVER_FONT_COLOR = "RED" # RGB % COLORE FONT SCONFITTA: 33.33% RED/ GREEN/ BLUE
WINNER_BG = "#ffcc00" # RGB % : 55.56 % RED, 44.44% GREEN, 0 % BLUE
LOSER_BG = "WHITE"

#COLORE DELLE CELLE
CELL_COLORS = {
    2: "#fcefe6", 
    4: "#f2e8cb",
    8: "#f5b682",
    16: "#f29446",
    32: "#ff775c",
    64: "#e64c2e",
    128: "#ede291",
    256: "#fce130",
    512: "#ffdb4a",
    1024: "#f0b922",
    2048: "#fad74d"
}

CELL_NUMBER_COLORS = {
    2: "#695c57",
    4: "#695c57",
    8: "#ffffff",
    16: "#ffffff",
    32: "#ffffff",
    64: "#ffffff",
    128: "#ffffff",
    256: "#ffffff",
    512: "#ffffff",
    1024: "#ffffff",
    2048: "#ffffff"
}

CELL_NUMBER_FONTS = {
    2: ("Helvetica", 55, "bold"),
    4: ("Helvetica", 55, "bold"),
    8: ("Helvetica", 55, "bold"),
    16: ("Helvetica", 50, "bold"),
    32: ("Helvetica", 50, "bold"),
    64: ("Helvetica", 50, "bold"),
    128: ("Helvetica", 45, "bold"),
    256: ("Helvetica", 45, "bold"),
    512: ("Helvetica", 45, "bold"),
    1024: ("Helvetica", 40, "bold"),
    2048: ("Helvetica", 40, "bold")
}
#BOLD= GRASSETTO