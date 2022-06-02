
#import pygame
import math
import numpy as np
from copy import deepcopy
import random
import time



class Board:

    def __init__(self) -> None:
        
        self.grid = np.zeros((6,7),'int8')
        self.last_played_pos = None # stores last played position on the board, could be red or yellow
        ''' then last_played_pos is used to check for possible connect 4 ie the check start from last_played_pos'''
        
        self.column_level = [5] * 7  # used for stacking chips on top of each other 
        

        self.ENCODING = {

            1: '\033[91m ⬤ \033[0m',

            2: "\033[92m ⬤ \033[0m",

            # 0: "\033[47m ⬤ \033[0m"

            0: ' ⬤ '

        }


        self.current = None 
        self.previous = None

        


    def prettyShow(self,ind = 0):
        space = ' ' * ind
        for i in range(6):
            print(space,end='')
            for j in range(7):
                
                print(f'{self.ENCODING[self.grid[i,j]]}', end='')

            print()

        print(space,end='')

        for i in range(7):
            print(f' {i+1} ', end='')
        print()



    def prettyShowandAnimate(self,ind = 0):

        if self.last_played_pos != None:

            col = self.last_played_pos[1]
            row = self.last_played_pos[0]

            grid_copy = deepcopy(self.grid)
            grid_copy[self.last_played_pos] = 0

            for p in range(row):
                #print(p)

                grid_copy[p,col] = self.grid[self.last_played_pos]
                
                space = ' ' * ind
                for i in range(6):
                    print(space,end='')
                    for j in range(7):
                        
                        print(f'{self.ENCODING[grid_copy[i,j]]}', end='')

                    print()

                print(space,end=' ')

                # for i in range(7):
                #     print(f' {i+1} ', end='')
                # print()

                grid_copy[p,col] = 0

                time.sleep(.45)

                for i in range(6):
                    print('\033[F',end='')


        self.prettyShow()





            


    def showgrid(self):

        print(self.grid)


    def helper_count(self):

        return np.count_nonzero(self.grid == 0)


   


    def modify(self,column, symbol) -> bool:
        column -= 1
        if column > 6:
            return False

            
        row = self.column_level[column]
        
        if row < 0:
            return False

        if self.grid[row, column] != 0:
            return False

        self.grid[row,column] = symbol
        self.last_played_pos = (row,column)
        self.column_level[column] -= 1
        return True



    def getAvailableMoves(self):

        moves = []

        for index, element in enumerate(self.column_level):
            if element >= 0:
                moves.append(index+1)


        return moves


    
    



    def checkWinner(self):
       
        count = 0

        # board.showgrid()
        
        cum_count = 0
        # x = (2,1)
       
        symbol = self.grid[self.last_played_pos]
        initial = self.last_played_pos

        self.previous = self.current
        self.current = initial


        if initial == None:
            return 0

        

        #horizontal check

        # ->
        
        current = list(initial)
        while count < 4: 

            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
            
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1
                    current[1]+=1 #move to the right
    
                else:
                    break

            else:
                break

        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 


        # <-
        current = list(initial)
        count = 0
        

        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1
                    current[1]-=1 #move to the left
            
                else:
                    break

            else:
                break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        cum_count = cum_count // 3 * 3



        
        # vertical

        # up

        '''this is prolly unnecessary you dont have to check up'''
        count = 0
        current = list(initial)
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1
                    current[0]-=1 #move up
                    

                else:
                    break

            else:
                    break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        
        # down
        current = list(initial)
        count = 0
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1

                    
                    current[0]+=1 #move down
                else:
                    break
            
            else:
                        break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        cum_count = cum_count // 3 * 3


        # diagonal \

        
        count = 0
        current = list(initial)
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1
                    current[0]-=1 #move up
                    current[1]-=1 #move to the left
                    

                else:
                    break

            else:
                    break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        
        
        
        current = list(initial)
        count = 0
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1

                    
                    current[0]+=1 #move down
                    current[1]+=1 #move to the right

                else:
                    break
            else:
                    break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        cum_count = cum_count // 3 * 3


        # diagonal /

        count = 0
        current = list(initial)
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1
                    current[0]-=1 #move up
                    current[1]+=1 #move to the right
                    

                else:
                    break

            else:

                break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 


        
        
        current = list(initial)
        count = 0
        while count < 4: 
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    count+=1
                    cum_count+=1

                    
                    current[0]+=1 #move down
                    current[1]-=1 #move to the left

                else:
                    break
            else:

                break


        cum_count -=1
        cum_count = 0 if cum_count < 0 else cum_count 

        cum_count = cum_count // 3 * 3
                
                


        score = cum_count//3
        # print(f'ss {score}')
        # if score < 0:
        #     score = 0
        return score 

    def CheckNeighbor(self, consec = 2, sym = None, pos : tuple = None, checkGive = False):

        if sym == None:
            symbol = self.grid[self.last_played_pos]

        else: 
            symbol = sym


        if pos == None:
            initial = self.last_played_pos

        else: 
            initial = pos

        
        if checkGive:
            if initial[0] == 0:
                return 0,0,0,0

            symbol = symbol%2 + 1
            temp = list(initial)
            temp[0]-=1
            initial = tuple(temp)
            #print(initial)

            


        # horizontal
        cum_count_horizontal = 0

        count = 0 
        current = list(initial)

        # left 
        current[1] -= 1
        while count < consec:
            if 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    cum_count_horizontal +=1
                    count+=1
                    current[1] -= 1


                else:
                    break

            else:
                break



        count = 0 
        current = list(initial)

        # right 
        current[1] += 1
        while count < consec:
            if 0 <= current[1] <= 6:
                if self.grid[tuple(current)] == symbol:
                    cum_count_horizontal +=1
                    count+=1
                    current[1] += 1



                else:
                    break

            else:
                break



        # vertical
        cum_count_vertical = 0

        # count = 0 
        # current = list(initial)

        # # up 
        # current[0] -= 1
        # while count < consec:
        #     if 0 <= current[0] <= 5:
        #         if self.grid[tuple(current)] == symbol:
        #             cum_count_vertical +=1
        #             count+=1
        #             current[0] -= 1

        #         else:
        #             break

        #     else:
        #         break



        count = 0 
        current = list(initial)

        # down 
        current[0] += 1
        while count < consec:
            if 0 <= current[0] <= 5:
                if self.grid[tuple(current)] == symbol:
                    cum_count_vertical +=1
                    count+=1
                    current[0] += 1



                else:
                    break

            else:
                break



        # diagonal 

        # / down
        cum_count_diagonal_r = 0
        count = 0
        current = list(initial)

         
        current[0] += 1
        current[1] -= 1

        #print(initial)
        while count < consec:
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                #print(tuple(current))

                if self.grid[tuple(current)] == symbol:
                    #print('ff')
                    cum_count_diagonal_r +=1
                    count+=1
                    current[0] += 1
                    current[1] -= 1



                else:
                    break

            else:
                break


        # / up
        
        count = 0
        current = list(initial)

            
        current[0] -= 1
        current[1] += 1

        #print(initial)
        while count < consec:
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                #print(tuple(current))

                if self.grid[tuple(current)] == symbol:
                    #print('ff')
                    cum_count_diagonal_r +=1
                    count+=1
                    current[0] -= 1
                    current[1] += 1



                else:
                    break

            else:
                break


    # diagonal 

        # \ down
        cum_count_diagonal_l = 0
        count = 0
        current = list(initial)

         
        current[0] -= 1
        current[1] -= 1

        #print(initial)
        while count < consec:
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                #print(tuple(current))

                if self.grid[tuple(current)] == symbol:
                    #print('ff')
                    cum_count_diagonal_l +=1
                    count+=1
                    current[0] -= 1
                    current[1] -= 1



                else:
                    break

            else:
                break


        # \ up
        
        count = 0
        current = list(initial)

            
        current[0] += 1
        current[1] += 1

        #print(initial)
        while count < consec:
            if 0 <= current[0] <= 5 and 0 <= current[1] <= 6:
                #print(tuple(current))

                if self.grid[tuple(current)] == symbol:
                    #print('ff')
                    cum_count_diagonal_l +=1
                    count+=1
                    current[0] += 1
                    current[1] += 1



                else:
                    break

            else:
                break


        






        return cum_count_vertical//consec , cum_count_horizontal//consec, cum_count_diagonal_r//consec, cum_count_diagonal_l//consec



    def get_board_copy(self):

        return deepcopy(self)




     


        





    



class Player:
    
    def __init__(self,name) -> None:
        self.name = name
        self.score = 0

    def getTotalcore(self):
        return self.score


class Human(Player):

    def __init__(self, name, symbol = 1) -> None:
        super().__init__(name)
        self.symbol = symbol


    def prompt(self,board: Board):

        while True:
            try:
                col = int(input('Enter column: '))
                # col-=1
                # row = board.column_level[col]
                if board.modify(col,self.symbol):
                    break

                else:
                    print('Invalid column value\n You have to enter it again')

                    

            except: 
                print('Illegal column value')


        score = board.checkWinner() 
        
        self.score += score
           



class AI(Player):

    def __init__(self, name, symbol = 2) -> None:
        super().__init__(name)
        self.symbol = symbol
        self.global_minimax = 0



    def evalFunc(self, board: Board):

        if board.last_played_pos[1] == 3:
            centre = 50
        else:
            centre = 0

        verdict = board.checkWinner(board)

        if verdict > 1:
            return 10000 * verdict

        three_cons = sum(board.CheckNeighbor()) *80

        two_cons = 0
        if not three_cons:
            two_cons = sum(board.CheckNeighbor(consec=1)) * 30



        opp_symbol = board.grid[board.last_played_pos] %2 +1
        # print(opp_symbol)
        board_copy = deepcopy(board)
        verdict_block_win = board.checkWinner(symb= opp_symbol,board = board_copy) *400

        board_copy = deepcopy(board)
        temp = list(board_copy.last_played_pos)
        temp[0] -= 1
        if temp[0] != 0:
            print(temp)
            print(opp_symbol)
            board_copy.last_played_pos = tuple(temp)
            board_copy.grid[tuple(temp)] = opp_symbol
            print(board_copy.grid)
            give_win = board.checkWinner(symb= opp_symbol,board = board_copy) * -425

        else:
            print('h')
            give_win = 0


        
        G_three_cons = sum(board.CheckNeighbor(checkGive=True)) * -80

        G_two_cons = 0
        if not three_cons:
            G_two_cons = sum(board.CheckNeighbor(consec=1, checkGive= True)) * -30



        
        print(f'two in a row: {two_cons}')
        print(f'three in a row: {three_cons}')
        print(f'giving two in a row: {G_two_cons}')
        print(f'giving three in a row: {G_three_cons}')
        print(f'block win: {verdict_block_win}')
        print(f'giving win: {give_win}')
        print(f'centre: {centre}')






        return two_cons +three_cons + G_three_cons + G_two_cons + verdict_block_win + give_win + centre





    def play(self,board: Board):

        board.modify(self.MTSimulation2(board,self.symbol),self.symbol)

        score = board.checkWinner() 
        
        
        self.score += score


    def play2(self,board: Board):

        b_copy = deepcopy(board)
        b_copy.last_played_pos = None

        m, eval = self.minimax(0,b_copy,True,-math.inf,math.inf,69)
        

        if m == None:
            print('err')
            input()

        board.modify(m,self.symbol)

        score = board.checkWinner() 
        
        
        self.score += score



        

        




    def MTSimulation(self, board_instance: Board, symbol = 2, N = 2500, lim = 10, opponent = 1):


        map = {}

        for i in range(N):
            # for y in range(5):
            #     print()
            copy_inst = deepcopy(board_instance)
            av_move = copy_inst.getAvailableMoves()
            count = 0
            current_sym = symbol
            seqnc = ''
            score = 0

            while count < lim and len(av_move):
                # print(av_move)
                # copy_inst.prettyShow(ind=i*2)

                chosen_move = random.choice(av_move)
                seqnc += str(chosen_move)

                copy_inst.modify(chosen_move,current_sym)
                verdict = copy_inst.checkWinner()
                # space = (i * 2) * ' '
                # print(space + ' ' + str(verdict))
                # print()

                if  verdict > 0:
                    # count+=1
                    # print(verdict, copy_inst.helper_count())
                    score+= (verdict * (copy_inst.helper_count() +1))

                    if current_sym == opponent:
                        score *= -1
                    

                
                count +=1

                av_move = copy_inst.getAvailableMoves()
                current_sym = (current_sym % 2) +1

            if seqnc == '':
                continue

            
            if seqnc in map:

                map[seqnc] += score

            else:

                map[seqnc] = score


        sc = -1000000000
        best_move = ''
        
        for k,v in map.items():

            if v > sc:
                sc = v
                best_move = k


        # from pprint import pprint
        # pprint(map, width=10)



        return int(best_move[0])


    def MTSimulation2(self, board_instance: Board, N = 10, lim = math.inf, opponent = 1): #prev n = 15k , lim = inf

        # N simulations will be done whereby lim moves will be played


        map = {}

        for i in range(N):
            # for y in range(5):
            #     print()
            copy_inst = deepcopy(board_instance)
            av_move = copy_inst.getAvailableMoves()
            count = 0
            current_sym = self.symbol
            seqnc = ''
            score = 0
            opp_score = 0



            while count < lim and len(av_move):
                # print(av_move)
                # copy_inst.prettyShow(ind=i*2)

                chosen_move = random.choice(av_move)
                seqnc += str(chosen_move)

                copy_inst.modify(chosen_move,current_sym)
                verdict = copy_inst.checkWinner()
                # space = (i * 2) * ' '
                # print(space + ' ' + str(verdict))
                # print()

                if  verdict > 0:

                    if current_sym == opponent:
                        opp_score += verdict

                    else:
                        score+= verdict
                    

                
                count +=1

                av_move = copy_inst.getAvailableMoves()
                current_sym = (current_sym % 2) +1

            if seqnc == '':
                continue

            
            score = score - opp_score

            if seqnc in map:

                pass

                # map[seqnc] += score

            else:

                map[seqnc] = score


        sc = -1000000000
        best_move = ''
        # print(map)
        for k,v in map.items():

            if v > sc:
                sc = v
                best_move = k


        # from pprint import pprint
        # pprint(map, width=10)



        return int(best_move[0])

    def minimax(self, depth, board: Board, maximizingPlayer,alpha, beta, move):

        
        
        depth += 1
        score = board.checkWinner()

        


       # print(f'current: {board.current}\n previous: {board.previous}')

        if depth == 5 or score > 0 or board.helper_count() == 0:

            

            
            space = ' ' * count
            
            if board.grid[board.last_played_pos] == self.symbol:

                # board.prettyShow()

                

                # print((f'{space}eval = {(board.helper_count() + 1) * score}'))
                
                return move, (board.helper_count() + 1) * score

            elif  board.grid[board.last_played_pos] == self.symbol % 2 +1:

                # board.prettyShow()

                

                # print((f'{space}eval = {(board.helper_count() + 1) * score * -1}'))

                

                return move, (board.helper_count() + 1) * score * -1

            else:
            

                return move, 0

        #print('here')
        if maximizingPlayer:
            best_move = None
            maxEval = -math.inf
            list_P_move = board.getAvailableMoves()
          
            for e_move in list_P_move:

                board_copy = board.get_board_copy()
                board_copy.modify(e_move,self.symbol)

                m, eval = self.minimax(depth,board_copy,False,alpha, beta, e_move)

                if eval > maxEval:
                    maxEval = eval
                    best_move = e_move


                if eval > alpha:
                    alpha = eval


                if beta <= alpha:
                    break



            return best_move, maxEval


        else:
            best_move = None
            minEval = math.inf
            list_P_move = board.getAvailableMoves()
            for e_move in list_P_move:

                board_copy = board.get_board_copy()
                board_copy.modify(e_move,(self.symbol % 2 + 1))

                m, eval = self.minimax(depth,board_copy,True,alpha, beta, e_move)

                if eval < minEval:
                    minEval = eval
                    best_move = e_move

                if eval < beta:
                    beta = eval


                if beta <= alpha:
                    break


            return best_move, minEval



def printScores(player1: Player, player2: Player, board: Board):
    print()

    print(f'{board.ENCODING[player1.symbol]} : {player1.score}', end = '')
    print(f'\t{board.ENCODING[player2.symbol]} : {player2.score}')

    print()










class Communication:
    pass





g = Board()
p = Human('',2)
f = Human('',2)
a = AI('')
a2 = AI('',1)

count = 2
move_counter = 0 
while move_counter < 7*6:

    

    g.prettyShowandAnimate()
    printScores(p,a2,g)
    if count ==1:
        #p.prompt(g)
        a2.play2(g)
        
    else:
        # g.modify(a.MTSimulation2(g),2)
        p.prompt(g)
        
    count = count % 2 +1
    move_counter +=1



g.prettyShowandAnimate()
printScores(p,a,g)

    






# print(a.evalFunc(g))


