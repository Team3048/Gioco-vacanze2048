
import tkinter as tk #tkinter= tk --> è una libreria che permette di creare interfacce grafiche nella programmazione con Python
import random
import colori as c #file che importiamo per fornire all'interfaccia la formattazione

#questa sottoclasse definirà l'aspetto della finestra di 2048
#self è una convenzione utilitzzata nelle classi, non deve essere per forza chiamato self, ma deve essere sempre il primo parametro di qualsiasi funzione appartente alla classe a cui si riferisce
class Game (tk.Frame): #abbiamo creato una classe di gioco seguita dal nome che abbiamo dato alla classe: Game, inoltre abbiamo una cornice rettangolare che conterrà gli oggetti di gioco(celle) che andremo a disegnare
    def __init__(self): #abbiamo definito e inizializzato la funzione self; tutte le classi hanno una funzione __init__, che viene sempre esegeuita quando la classe stessa viene iniziata
        tk.Frame.__init__(self)
        self.grid() #creazione delle nostra griglia di gioco
        self.master.title("2048 by Lorenzo Carbonara, Niccolò Panciroli & Francesco Righetti") #titolo dell'interfaccia
        self.main_grid = tk.Frame(self, bg=c.GRID_COLOR, bd=3 , width=900, height=900)
        #bg= back ground color; bd= border --> 3 pixel; width= larghezza; height= altezza
        self.main_grid.grid(pady=(80, 0)) #spaziatura orizzontale e verticale tra più righe e colonne
        self.make_GUI()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        self.mainloop()


    def make_GUI(self): #creiamo una griglia 4x4, GUI: graphic user interface è dunque in interfaccia che viene disegnata sullo schermo con la quale l'utente può interagire
        self.cells = [] #creiamo una lista contenente le informaioni per ogni cella della griglia
        
        for i in range(4):
            row = [] #abbiamo creato una lista riga
            for j in range(4):
                #frame= cornice
                cell_frame = tk.Frame(self.main_grid, bg=c.EMPTY_CELL_COLOR, width=120, height=120)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)

                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # creazione del punteggio in alto
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center") #anchor= orientamento
        tk.Label(score_frame, text="Punteggio", font=c.SCORE_LABEL_FONT).grid(row=0)
        #Label: testo non editabile; frame: cornice; score: punteggio
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)
    
    def start_game(self):
        # creare un creatore di zeri
        self.matrix = [[0] * 4 for _ in range(4)]

        # riempire due celle causuali con due numeri 2
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(bg=c.CELL_COLORS[2], fg=c.CELL_NUMBER_COLORS[2], font=c.CELL_NUMBER_FONTS[2], text="2")
      
        while(self.matrix[row][col] != 0): #mentre le liste row e col sono diverse da zero allora:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(bg=c.CELL_COLORS[2], fg=c.CELL_NUMBER_COLORS[2], font=c.CELL_NUMBER_FONTS[2], text="2")
        self.score = 0

    # Azioni compiute dalla matrice

    def stack(self): #comprimere tutti i numeri diversi da zero nella matrice verso un lato della griglia, eliminando tutti gli spazi vuoti tra di essi
        new_matrix = [[0] * 4 for _ in range(4)] #creazione di una nuova matrice di tutti zeri
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix
        
    def combine(self): #combina insieme tutti i numeri uguali adiacenti 
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self): #inverte l'ordine di ogni riga
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def transpose(self): #capovolge la matrice sulla sua diagonale
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    # Add a new 2 or 4 tile randomly to an empty cell
    def add_new_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    # aggiorna la GUI in modo che corrisponda alla matrice 
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(bg=c.CELL_COLORS[cell_value], fg=c.CELL_NUMBER_COLORS[cell_value], font=c.CELL_NUMBER_FONTS[cell_value], text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    # Funzioni delle Freccie in basso a sinistra
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()
    # Verifica dell'esistenza di altri movimenti
    def horizontal_move_exists(self): #up & down
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    def vertical_move_exists(self): # right & left
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False
    # Verifica della sconfitta (Win/Lose)
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(game_over_frame, text="You win!", bg=c.WINNER_BG, fg=c.GAME_OVER_FONT_COLOR, font=c.GAME_OVER_FONT).pack()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label( game_over_frame, text="Game over!", bg=c.LOSER_BG, fg=c.GAME_OVER_FONT_COLOR, font=c.GAME_OVER_FONT).pack()
# La riga if __name__ == "__main__": dice al programma che il codice all'interno di questa istruzione if deve essere eseguito solo se il programma viene eseguito come programma autonomo. Non verrà eseguito se il programma viene importato come modulo.
def main():
    Game()
if __name__ == "__main__":
    main()
# implica che il modulo viene eseguito autonomamente dall'utente e che possiamo eseguire le azioni appropriate corrispondenti.
# ogni volta che hai bisogno di un programma, che deve essere eseguito come script/programma autonomo, e vorresti anche importarlo all'interno di altri programmi