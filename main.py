import pygame
import sys
import os

# Define constants for the board size and cell size
BOARD_SIZE = 8
CELL_SIZE = 60
WINDOW_SIZE = (CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

class OthelloGame:
    def __init__(self):
        self.board = [[2] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.board[3][3] = 0  # White circle
        self.board[3][4] = 1  # Black circle
        self.board[4][3] = 1  # Black circle
        self.board[4][4] = 0  # White circle
            
    def switch_player(self, player):
        return 0 if player == 1 else 1

    def is_valid_move(self, row, col,player):
        valid_moves = self.get_valid_moves(player)
        return [row, col] in valid_moves

        # Check if the cell is empty and the move flips at least one opponent's piece
        # Implement the logic here

    def make_move(self, row, col,player):
        self.board[row][col]=player
        #right
        l=[]
        for r in range(row+1,8):
            
            if self.board[r][col]==1-player:
                l.append(r)
            if self.board[r][col]==2:
                l=[]
                break
            if self.board[r][col]==player:
                for x in l:
                    self.board[x][col]=player
                l=[]
                break
        #left 
        l=[]
        for r in range(row-1,-1,-1):
            
            if self.board[r][col]==1-player:
                l.append(r)
            if self.board[r][col]==2:
                l=[]
                break
            if self.board[r][col]==player:
                for x in l:
                    self.board[x][col]=player
                l=[]
                break
        #up     
        l=[]
        for c in range(col-1,-1,-1):
            
            if self.board[row][c]==1-player:
                l.append(c)
            if self.board[row][c]==2:
                l=[]
                break
            if self.board[row][c]==player:
                for x in l:
                    self.board[row][x]=player
                l=[]
                break
        #down  
        l=[]
        for c in range(col+1,8):
            
            if self.board[row][c]==1-player:
                l.append(c)
            if self.board[row][c]==2:
                l=[]
                break
            if self.board[row][c]==player:
                for x in l:
                    self.board[row][x]=player
                l=[]
                break
        #right and up
        r=row-1
        c=col+1
        l=[]
        while r>=0 and c<8:
            if self.board[r][c]==1-player:
                l.append((r,c))
                r-=1
                c+=1
            if r>=0 and c<8 and self.board[r][c]==2:
                l=[]
                break
            if r>=0 and c<8 and self.board[r][c]==player:
                for a,b in l:
                    self.board[a][b]=player
                l=[]
                break
        #right and down
        r=row+1
        c=col+1
        l=[]
        while r<8 and c<8:
            if self.board[r][c]==1-player:
                l.append((r,c))
                r+=1
                c+=1
            if r<8 and c<8 and self.board[r][c]==2:
                l=[]
                break
            if r<8 and c<8 and self.board[r][c]==player:
                for a,b in l:
                    self.board[a][b]=player
                l=[]
                break
        #left and up
        r=row-1
        c=col-1
        l=[]
        while r>=0 and c>=0:
            if self.board[r][c]==1-player:
                l.append((r,c))
                r-=1
                c-=1
            if r>=0 and c>=0 and self.board[r][c]==2:
                l=[]
                break
            if r>=0 and c>=0 and self.board[r][c]==player:
                for a,b in l:
                    self.board[a][b]=player
                l=[]
                break
        #left and down
        r=row+1
        c=col-1
        l=[]
        while r<8 and c>=0:
            if self.board[r][c]==1-player:
                l.append((r,c))
                r+=1
                c-=1
            if r<8 and c>=0 and self.board[r][c]==2:
                l=[]
                break
            if r<8 and c>=0 and self.board[r][c]==player:
                for a,b in l:
                    self.board[a][b]=player
                l=[]
                break
        player=self.switch_player(player)
        # Place the player's piece on the board and flip opponent's pieces
        # Implement the logic here

    def get_valid_moves(self, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == player:  
                    #right
                    if row+1<8 and self.board[row+1][col]==1-player and not self.board[row+1][col]==2:
                        for r in range(row+1,8):
                            if self.board[r][col]==player:
                                break
                            if self.board[r][col]==2:
                                valid_moves.append([r,col])
                                break
                    #left
                    if row-1>=0 and self.board[row-1][col]==1-player and not self.board[row-1][col]==2:
                        for r in range(row-1,-1,-1):
                            if self.board[r][col]==player:
                                break
                            if self.board[r][col]==2:
                                valid_moves.append([r,col])
                                break
                    #up
                    if col-1>=0 and self.board[row][col-1]==1-player and not self.board[row][col-1]==2:
                        for c in range(col-1,-1,-1):
                            if self.board[row][c]==player:
                                break
                            if self.board[row][c]==2:
                                valid_moves.append([row,c])
                                break
                    #down
                    if col+1<8 and self.board[row][col+1]==1-player and not self.board[row][col+1]==2:
                        for c in range(col+1,8):
                            if self.board[row][c]==player:
                                break
                            if self.board[row][c]==2:
                                valid_moves.append([row,c])
                                break
                    #left and down
                    if row-1>=0 and col+1<8 and self.board[row-1][col+1]==1-player and not self.board[row-1][col+1]==2:
                    # if row-1>=0 and col+1<8 and self.board[row-1][col+1]==1-player:
                        r=row-1
                        c=col+1
                        while r-1>=0 and c+1<8:
                            if self.board[r][c]==player:
                                break
                            if self.board[r][c]==2:
                                valid_moves.append([r,c])
                                break
                            if self.board[r][c]==1-player:
                                r=r-1
                                c=c+1
                    #left and up
                    if row-1>=0 and col-1>=0 and self.board[row-1][col-1]==1-player and not self.board[row-1][col-1]==2:
                    # if row-1>=0 and col-1>=0 and self.board[row-1][col-1]==1-player:
                        r=row-1
                        c=col-1
                        while r-1>=0 and c-1>=0:
                            if self.board[r][c]==player:
                                break
                            if self.board[r][c]==2:
                                valid_moves.append([r,c])
                                break
                            if self.board[r][c]==1-player:
                                r-=1
                                c-=1
                    #right and down
                    if row+1<8 and col+1<8 and self.board[row+1][col+1]==1-player and not self.board[row+1][col+1]==2:
                    # if row+1<8 and col+1<8 and self.board[row+1][col+1]==1-player:
                        r=row+1
                        c=col+1
                        while r+1<8 and c+1<8:
                            if self.board[r][c]==player:
                                break
                            if self.board[r][c]==2:
                                valid_moves.append([r,c])
                                break  
                            if self.board[r][c]==1-player:
                                r+=1
                                c+=1          
                    #right and up
                    if row+1<8 and col-1>=0 and self.board[row+1][col-1]==1-player and not self.board[row+1][col-1]==2:
                    # if row+1<8 and col-1>=0 and self.board[row+1][col-1]==1-player:
                        r=row+1
                        c=col-1
                        while r+1<8 and c-1>=0:
                            if self.board[r][c]==player:
                                break
                            if self.board[r][c]==2:
                                valid_moves.append([r,c])
                                break
                            if self.board[r][c]==1-player:
                                r+=1
                                c-=1
        return valid_moves

    def is_game_over(self,player):
        return not self.get_valid_moves(player) and not self.get_valid_moves(1 - player)

        # Check if the game is over (no valid moves for both players)
        # Implement the logic here

    def get_winner(self):
        black_count = sum(row.count(1) for row in self.board)
        white_count = sum(row.count(0) for row in self.board)

        if black_count > white_count:
            return 1  # Black wins
        elif white_count > black_count:
            return 0  # White wins
        else:
            return -1  # Tie
        
        # Return the winner of the game or None if it's a tie
        # Implement the logic here

class OthelloGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Othello")
        self.clock = pygame.time.Clock()
        self.game = OthelloGame()

    def draw_board(self,player):
        self.screen.fill(GREEN)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                pygame.draw.rect(self.screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)  
            
                if self.game.board[row][col] == 1:
                    pygame.draw.circle(self.screen, BLACK, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)  
                elif self.game.board[row][col] == 0:
                    pygame.draw.circle(self.screen, WHITE, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)  
                if self.game.is_valid_move(row, col, player):
                    pygame.draw.circle(self.screen, (0, 0, 255, 100), (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 10)  
                
        # Draw the game board, including circles and valid move indicators
        # Implement the drawing logic here

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        running = True
        player=1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row = event.pos[1] // CELL_SIZE
                    col = event.pos[0] // CELL_SIZE
                    
                    for inner in self.game.board:
                        print(inner)
                    print(row)
                    print(col)
                    
                    if self.game.is_valid_move(row,col,player):
                        self.game.make_move(row,col,player)
                        player=self.game.switch_player(player)
                        print('Yes , a valid move')
                        if player==0:
                            print("White ki baari hai")
                        else:
                            print("Black ki baari hai")
                        if not self.game.get_valid_moves(player):
                            player=self.game.switch_player(player)
                            
                        if self.game.is_game_over(player):
                            winner=self.game.get_winner()
                            if winner == 0:
                                winner_text = "White wins!"
                            elif winner == 1:
                                winner_text = "Black wins!"
                            else:
                                winner_text = "It's a tie!"
                            
                            self.screen.fill(GREEN)
                            pygame.display.update()
                            
                            # Display the winner message for 3 seconds
                                  
                            font = pygame.font.Font(None, 36)
                            text_surface = font.render(winner_text, True, BLACK)
                            text_rect = text_surface.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
                            self.screen.blit(text_surface, text_rect)
                            pygame.display.update()
                            self.clear_terminal()
                            pygame.time.wait(3000)
                            
                            # Reset the game and continue
                            
                            self.game = OthelloGame()
                            player = 1    
                        
                    # print(self.game.get_valid_moves(player))
                self.draw_board(player)
                
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    gui = OthelloGUI()
    gui.run()
