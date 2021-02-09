import sys
# game --------------------
def game():
        print('Great! lets get started')
        print('your in a room. in this room there are no windows')
        print('there is a chest')
        print('there is a bed')
        print('and one door leading to the outside')
        print('type 1 to go to the chest')
        print('type 2 to  go to the bed and rest')
        print('or type 3 to go outside')
        answer = input()

        if answer == '1':
            print('in this chest there is a sword')
            print('type 1 to equip')
            print('type 2 to not')
            answer = input()
            if answer == '1':
                print('you got a sword out of the chest and went outside')
                print('fought off the goblins and wolves who tried to ambush you')
                print('escaped the forest and lived happily ever after')
                print(' type 1 to close')
                answer = input()
                if answer == '1':
                    sys.exit()
            elif answer == '2':
                print('you lose! you were ambushed by goblins and you had no sword to defend with')
                print('the captured you, and the fed you to the wolves')
                print('so basically your dead')

        elif answer == '2':
            print('you have gone to sleep')
            print('few hours later you woke')
            print('you went out, with a sword you got from the chest.')
            print('you were then ambushed by goblins and wolves but killed them all escaped the forest')
            print('and lived happily ever after')
            print('so you won! type 1 to close.')
            answer = input()
            if answer == '1':
                sys.exit()
        elif answer == '3':
            print('its night time')
            print('it appears you are in a forest. you hear a wolf howling and goblins roaring')
            print('type 1 to go out')
            print('type 2 to stay inside until dawn')
            answer = input()
            if answer == '1':
                print('you lose! you were ambushed by goblins and you had no sword to defend with')
                print('the captured you, and the fed you to the wolves')
                print('so basically your dead')
            elif answer == '2':
                print('you have waited a few hours and dawn has come.')
                print('type 1 to go to the chest or type 2 to go out')
                answer = input()
                if answer == '1':
                    print('you got a sword out of the chest and went outside')
                    print('fought off the goblins and wolves who tried to ambush you')
                    print('escaped the forest and lived happily ever after')
                    print(' type 1 to close')
                    answer = input()
                    if answer == '1':
                        sys.exit()
                elif answer == '2':
                    print('you were ambushed by goblins and died you lose')
        else:
            print('type error!')


# menu -------------------
print('welcome! would you like to play? yes/no')
answer = input()
if answer == 'yes':
    game()
elif answer == 'no':
    sys.exit()

# really bad way of doing things 