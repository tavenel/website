import time, sys
import keyboard

class Space:
    def __init__(self, nb_l, nb_c, empty_cell=' ', invader='#', missile='^', pos_canon=None):
        self.nb_l = nb_l
        self.nb_c = nb_c

        self.empty_cell = empty_cell
        self.invader = invader
        self.missile = missile

        self.grille = [ [ empty_cell for _ in range(nb_c) ] for _ in range(nb_l) ]
        # Ou algorithmiquement :
        #self.grille = []
        #for i in range(nb_l):
        #    ligne = []
        #    self.grille.append(ligne)
        #    for j in range(nb_c):
        #        ligne.append(empty_cell)

        # Add invaders
        self.grille[0] = [invader for _ in range(self.nb_c)]

        # Add canon
        if pos_canon is None:
            pos_canon = int(self.nb_c /2) # center
        self.canon = Canon(pos_canon)
        self.grille[-1][pos_canon] = self.canon

        # Add score
        self.score = 0

    def __repr__(self) -> str:

        # 1st line
        # ''.join(list) is a shortcut to concatenate all characters in a list
        screen = '┌' + ''.join( ['─' for _ in range(self.nb_c)] ) + '┐\n'

        # iterate on lines
        for i in self.grille:

            # start line with a '|'
            screen += '|'

            # print each cell
            for j in i:
                screen += j.__str__() # transform j in type 'str' if j were a complex type
            
            # end line with a '|' and go to next line
            screen += '|\n'

        # last line
        screen += '└' + ''.join( ['─' for _ in range(self.nb_c)]) + '┘\n'

        # score
        screen += 'Score : ' + str(self.score) + '\n'

        return screen
    
    def tirer(self):

        for x in range(self.nb_l-2, -1, -1):

            # missile goes up
            if self.grille[x][self.canon.pos] == self.invader:
                self.score += 1
            self.grille[x][self.canon.pos] = self.missile
            # clean last position
            if x < self.nb_l-2:
                self.grille[x+1][self.canon.pos] = self.empty_cell

            print(self)
            time.sleep(0.5)

        # missile disappears
        self.grille[0][self.canon.pos] = self.empty_cell
        print(self)
    
    def tirer_avec_animation(self):
        self.grille[-2][self.canon.pos] = self.missile

    def move_canon(self, mvt):
        # Check if still moving in the grid
        if self.canon.pos + mvt >= 0 and self.canon.pos + mvt < self.nb_c:
            # clean last position
            self.grille[-1][self.canon.pos] = self.empty_cell
    
            # move
            self.canon.pos = self.canon.pos + mvt
            self.grille[-1][self.canon.pos] = self.canon

    def move_missiles(self):
        # last line : cleanup missiles from last run
        self.grille[0] = [ self.empty_cell if cell == self.missile else cell for cell in self.grille[0] ]

        # before last line : move missile
        for i in range(self.nb_l-1):
            for j in range(self.nb_c):
                if self.grille[i+1][j] == self.missile:
                    self.score += 1 if self.grille[i-1][j] == self.invader else 0
                    self.grille[i][j] = self.missile
                    self.grille[i+1][j] = self.empty_cell

    def move_invaders(self, invaders_speed):

        # move existing invaders
        for l in range(self.nb_l-1, -1, -1): # iterate on lines (reverse to avoid recursion)
            newl = l + invaders_speed
            for c in range(self.nb_c): # iterate on columns to inspect cells
                if self.grille[l][c] == self.invader: # only care about invaders
                    if newl >= self.nb_l -1: # overflow - an invader reached the floor
                        print('Game over ! Your score : ', self.score)
                        sys.exit(0)
                    else: # move the cell
                        previous_content = self.grille[newl][c]
                        self.grille[newl][c] = self.invader if previous_content == self.empty_cell else previous_content
                        self.grille[l][c] = self.empty_cell

        # add new invaders to fill the first lines
        for l in range(invaders_speed):
            self.grille[l] = [self.invader if previous_content == self.empty_cell else previous_content for _ in range(self.nb_c)]
                       

class Invader:
    def __init__(self, c='#'):
        self.c = c 
    
    def __str__(self) -> str:
        # On appelle la méthode __str__ de l'objet représentant l'envahisseur
        # pour permettre d'utiliser un type plus complexe qu'un simple caractère.
        # Ici, retourner simplement self.c aurait suffit
        return self.c.__str__()

class Canon:
    def __init__(self, pos):
        self.pos = pos
    
    def __repr__(self) -> str:
        return '_'

class GameEngine:
    def __init__(self, space:Space, invaders_speed=1, invaders_timer=1):
        self.space = space

        # Move invaders
        self.invaders_speed = invaders_speed
        self.invaders_timer = invaders_timer # a dedicated timer to slow the game (invaders move only every invaders_timer)
        self.timer = 0

    def play(self):
        print(self.space)
        while True:
            self._onkeypress(keyboard.read_key(suppress=True))
            time.sleep(0.1)
    
    def _onkeypress(self, key):
        if key == 'left' or key == 'q' or key == 'h':
            self.space.move_canon(-1)
            self._inc_timer()
        elif key == 'right' or key == 'd' or key == 'l':
            self.space.move_canon(+1)
            self._inc_timer()
        elif key == 'return' or key == 'space':
            self.space.tirer_avec_animation()
            self._inc_timer()
    
    def _inc_timer(self):
        self.timer += 1
        self.space.move_missiles()
        if (self.timer % self.invaders_timer == 0): # only move invaders every `invaders_timer`
            self.space.move_invaders(self.invaders_speed)
        print('\n',self.space) # add line break to partially fix keyboard bug printing key output on 1st line
    

if __name__ == '__main__':

    #space = Space(4, 10)
    #print(space.grille)
    #i = Invader()
    #print(i)
    #print(space)
    #space.tirer()       

    GameEngine(
        Space(20,10, missile='|', invader=Invader('"')),
        invaders_speed=2,
        invaders_timer=8
        ).play()