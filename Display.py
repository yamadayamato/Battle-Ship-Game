import pygame

class Display:
    """Class to handle PyGame input and output"""
    colours = {
        "water": (	0, 105, 148, 1),
        "ship": (169, 169, 200,1),
        "hit": pygame.color.Color("red"),
        "miss": pygame.color.Color("black"),
        "background": pygame.image.load('img/background6.jpg'),
        "text": (255,255,255,1)
    }
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    hit1 = False
    hit2 = False
    def __init__(self, board_size=10, cell_size=20, margin=50):
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin


        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Helvetica", 13)
        self.font2 = pygame.font.SysFont("Helvetica", 20)



        screen_width = self.cell_size * board_size * 2 + 4 * margin
        screen_height = self.cell_size * board_size + 2 * margin
        self.screen = pygame.display.set_mode(
            [screen_width, screen_height])
        pygame.display.set_caption("Battleship Game")
        pygame.display.set_icon(pygame.image.load('img/logo.png'))

    def show(self, upper_board, lower_board, include_top_ships=False):
        """Requests appropriate Colour Grids from boards, and draws them"""
        if upper_board is not None:
            upper_colours = upper_board.colour_grid(
                self.colours, include_top_ships)

        if lower_board is not None:
            lower_colours = lower_board.colour_grid(
                self.colours)

        self.screen.blit(Display.colours["background"], (0 , 0))
        offset = self.margin * 2 + self.board_size * self.cell_size

        for y in range(self.board_size):
            for x in range(self.board_size):

                if upper_board is not None:
                    
                    pygame.draw.rect(self.screen, upper_colours[y][x],
                                     [offset+self.margin + x * self.cell_size,
                                     self.margin + y * self.cell_size,
                                      self.cell_size, self.cell_size])


                if lower_board is not None:
                    offsety=self.margin
                    pygame.draw.rect(self.screen, lower_colours[y][x],
                                     [self.margin + x * self.cell_size,
                                      y * self.cell_size+offsety,
                                      self.cell_size, self.cell_size])
            if lower_board is not None:
                # draws the vertical lines
                for x in range(0, (self.board_size + 1) * self.cell_size, self.cell_size):
                    pygame.draw.line(self.screen, (0, 0, 0, 0), (x + self.margin, self.margin),
                                     (x + self.margin, self.margin + self.cell_size * (self.board_size)))
                # draws the horizontal lines
                for y in range(0, self.board_size + 1):
                    pygame.draw.line(self.screen, (0, 0, 0, 0), (self.margin, self.margin + (y) * (self.cell_size)),
                                     (self.cell_size * self.board_size + self.margin,
                                      self.margin + self.cell_size * (y)))


                label1 = self.font2.render("My Ships", True, Display.colours["text"])
                label2 = self.font2.render("Opponent's Ships", True, Display.colours["text"])
            if upper_board is not None:
                for x in range(0, (self.board_size + 1) * self.cell_size, self.cell_size):
                    pygame.draw.line(self.screen, (0, 0, 0, 0), (x + self.margin +offset,self.margin),
                                     (x + self.margin+offset, self.margin + self.cell_size * (self.board_size)))
                # draws the horizontal lines
                for y in range(0, self.board_size + 1):
                    pygame.draw.line(self.screen, (0, 0, 0, 0), (self.margin +offset,self.margin + (y) * (self.cell_size)),
                                     (self.cell_size * self.board_size + self.margin +offset, self.margin+ self.cell_size * (y)))

                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     [(self.board_size*self.cell_size)/2+(2/3)*self.cell_size, self.margin / 2-5, label1.get_width(), label1.get_height()])
                    pygame.draw.rect(self.screen, (0, 0, 0), [(self.board_size*self.cell_size)/2+offset-self.cell_size/2-2, self.margin / 2 -5, label2.get_width(),label2.get_height()])
                    self.screen.blit(label1, ((self.board_size*self.cell_size)/2+(2/3)*self.cell_size, self.margin/2-5))
                    self.screen.blit(label2, ((self.board_size*self.cell_size)/2+offset-self.cell_size/2-2, self.margin/2-5))
                    if Display.hit1:
                        userhit = "Hits!"
                        color1 = (0,255,0,1)
                    else:
                        userhit = "Misses!"
                        color1 = (255, 0, 0, 1)
                    if Display.hit2:
                        opponenthit = "Hits!"
                        color2 = (0,255,0,1)
                    else:
                        opponenthit = "Misses!"
                        color2 = (255, 0, 0, 1)


                    label3 = self.font.render(f"User's Turn: ({Display.x1},{Display.y1})  {userhit}", True,color1)
                    label4 = self.font.render(f"Opponents's Turn: ({Display.x2},{Display.y2})  {opponenthit}", True,color2)


                    if Display.x2 != -1 and Display.y2 != -1:
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                         [self.margin,
                                          self.margin + (self.board_size * self.cell_size) + self.margin / 4,
                                          self.board_size * self.cell_size, label4.get_height()])
                        self.screen.blit(label4, (
                            self.margin,
                            self.margin + (self.board_size * self.cell_size) + self.margin / 4))

                    if Display.x1 != -1 and Display.y1 != -1:
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                         [(self.board_size * self.cell_size) + self.margin * 3,
                                          self.margin + (self.board_size * self.cell_size) + self.margin / 4,
                                          self.board_size * self.cell_size, label3.get_height()])

                        self.screen.blit(label3, (
                            (self.board_size * self.cell_size) + self.margin * 3,
                            self.margin + (self.board_size * self.cell_size) + self.margin / 4))


    def get_input(self):
        """Converts MouseEvents into board corrdinates, for input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Display.close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x=x-self.margin
                x = ( x % ( self.margin*2+ self.board_size * self.cell_size)) // self.cell_size
                y = (y - self.margin) // self.cell_size
                if x in range(self.board_size) and y in range(self.board_size):
                    return x, y
        return None, None
    def show_text(self, text, upper=False, lower=False):
        """Displays text on the screen, either upper or lower """
        x = self.margin
        y_up = x
        y_lo =self.margin/2
        label = self.font.render(text, True, Display.colours["text"])
        label2 = self.font.render("Instructions:", True, Display.colours["text"])
        if upper:
            self.screen.blit(label, (x, y_up))
        if lower:
            pygame.draw.rect(self.screen,(0,0,0),[self.margin,self.margin/2 -15,label2.get_width(),20])
            pygame.draw.rect(self.screen,(0,0,0),[self.margin,self.margin/2,label.get_width(),20])
            self.screen.blit(label, (x, y_lo))
            self.screen.blit(label2, (x, y_lo - 15))



    @classmethod
    def flip(cls):
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    @classmethod
    def close(cls):
        pygame.display.quit()
        pygame.quit()

