## here i have defined some functions and at last i called them\n
## actually here start game is the first function that starts the game
def start_game():
    print("you are standing in dark room.\n There is a door to your left and right , which one do you take ? (l or r) ")
    ans1 = ''
    ans1 = input('<')
    if ans1.lower() == 'r':
        monster_room()
    elif ans1.lower() == 'l':
        snake_room()
    else :
        print('wrong input')
        print('game over\n wanna play again (y or n)')
        ans3 = ''
        ans3 = input('<')
        if ans3.lower() == 'y':
            start_game()
        else:
            print('WRONG  INPUT! \n Start again')
            start_game()
        
        
    

def monster_room():
    print('now you entered the room of monster!')
    print('\nThe monster is sleeping.')
    print('\nBehind the monster there is another door. What would you do? (1 or 2)')
    print('\n1). go through the door open silently')
    print("\n2). kill the monster and show your courage")
    ans2 = int(input('<'))
    if ans2 == 1:
        treasure_room()
    elif ans2 ==2:
        print('The monster was hungry , he/it ate you.')
        print('\ngame over\n wanna play again')
        ans3 =''
        ans3 =input('<')
        if ans3.lower() == 'y':
            start_game()
        else:
            print('game over')
    else:
        print('WRONG  INPUT! \n Start again')
        start_game()



def snake_room():
    print('There is a snake here. \n Behind the snake is another door.')
    print('\nThe snake is having eggs')
    print('\n1). Take the eggs.')
    print('\n2). Taunt the snake')
    ans2 = int(input(">"))
    if ans2 == 1:
        print('you want eggs not the teasure !! Thats why the snake killed you.')
        print('\ngame over\n wanna play again')
        ans3 = ''
        ans3 =input('<')
        if ans3.lower() == 'y':
            start_game()
        else:
            print('game over')
    elif ans2 ==2:
        treasure_room()
    else:
        print('WRONG  INPUT! \n Start again')
        start_game()
        
        
def treasure_room():
    print('You are now in room filled with diamonds !')
    print('\nAnd there is door too!')
    print('\nWhat would you do? (1 or 2) ')
    print('\n1). Take some diamonds and go through the door.')
    print('\n2). Just go through the door.')
    ans4 = int(input())
    if ans4 == 1:
        print('Game over')
        print('\nwanna play again')
        ans3 = ''
        ans3 =input('<')
        if ans3.lower() == 'y':
            start_game()
        else:
            print('game over')
    elif ans4 ==2:
        print('YAY !! WIN')
    else:
        print('WRONG  INPUT! \n Start again')
        start_game()
        
        
start_game()
    