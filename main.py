from classes import Board, Human,AI, printScores



board = Board()
human = Human('',2)
a2 = AI('',1)

count = 2
move_counter = 0 
while move_counter < (7*6)- 1:

    

    board.prettyShowandAnimate()
    printScores(human,a2,board)
    if count ==1:
        #human.prompt(board)
        a2.play2(board)
        
    else:
        # board.modify(a.MTSimulation2(board),2)
        human.prompt(board)
        
    count = count % 2 +1
    move_counter +=1



board.prettyShowandAnimate()
printScores(human,a2,board)
