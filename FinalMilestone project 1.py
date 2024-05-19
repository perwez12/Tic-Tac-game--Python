#!/usr/bin/env python
# coding: utf-8

# In[25]:


from IPython.display import clear_output
clear_output()


# In[26]:


def display(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])
    


# In[ ]:





# In[27]:


def player_input():
    mark=''
    while mark not in ['X','O']:
        mark=input("Take X or O ")
    if mark=='X':
        return ('X','O')
    else:
        return('O','X')


# In[28]:


def place_marker(board, marker, position):
    board[position]=marker
    


# In[29]:


def win_check(board, mark):
    return(board[1]==board[2]==board[3]==mark or
          (board[4]==board[5]==board[6]==mark)or
          (board[7]==board[8]==board[9]==mark)or
          (board[1]==board[4]==board[7]==mark)or
          (board[2]==board[5]==board[8]==mark)or
          (board[9]==board[6]==board[3]==mark)or
          (board[7]==board[5]==board[3]==mark)or
          (board[9]==board[5]==board[1]==mark))


# In[30]:


import random

def choose_first():
    k=random.randint(0,1)==0
    if k==0:
        return 'player_2'
    else:
        return 'player_1'


# In[ ]:





# In[31]:


def space_check(board, position):
    
    return board[position]==''


# In[32]:


def full_board_check(board):
    for i in range(1,10):
        return space_check(board,i)


# In[33]:


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("enter a number"))
    return position


# In[34]:


def replay():
    return input("Do you want to continue yes or no ")


# In[ ]:


print('Welcome to Tic Tac Toe!')
while True:
    test=['']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn,"will go first")
    play_game=input("you want to play the game y or n")
    if play_game[0]=='y':
        game_on=True
    else :
        game_on=False
    while game_on:
        if turn =='player_1':
            display(test)
            position=player_choice(test)
            place_marker(test,player1_marker,position)
            if win_check(test, player1_marker):
                display(test)
                print("you have won the game")
                game_on=False
            else:
                if full_board_check(test):
                    display(test)
                    print("game is tie")
                    break
                else:
                    turn='player_2'
        else:
            display(test)
            position=player_choice(test)
            place_marker(test,player2_marker,position)
            if win_check(test, player2_marker):
                display(test)
                print("you have won the game")
                game_on=False
            else:
                if full_board_check(test):
                    display(test)
                    print("game is tie")
                    break
                else:
                    turn='player_1'
                    
    if not replay():
        break


# In[ ]:





# In[ ]:




