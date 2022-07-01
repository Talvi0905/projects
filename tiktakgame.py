while 1:
    print("""                           MENU
                  ****************************
                          1. START GAME
                          2. EXIT
            -- """)
    start=int(input("enter your choise -- " ))
    a,b,c,d,e,f,g,h,i=1,2,3,4,5,6,7,8,9
    print(f"{a} | {b} | {c}\n{d} | {e} | {f}\n{g} | {h} | {i}")
    if start==1:
        playerO="O"
        playerX="X"
        current_player=playerO
        while 1:
            
            player_1=int(input("player  turn--  "))
            if player_1==1 and a==1:
                a=current_player
            elif player_1==2 and b==2:
                b=current_player
            elif player_1==3 and c==3:
                c=current_player
            elif player_1==4 and d==4:
                d=current_player
            elif player_1==5 and e==5:
                e=current_player
            elif player_1==6 and f==6:
                f=current_player
            elif player_1==7 and g==7:
                g=current_player
            elif player_1==8 and h==8:
                h=current_player
            elif player_1==9 and i==9:
                i=current_player
            else:
                print("not consider")
                continue
            print(f"{a} | {b} | {c}\n{d} | {e} | {f}\n{g} | {h} | {i}")

            if current_player==playerO:
                current_player=playerX
            else:
                current_player=playerO

        
                
            #(WINNING SITUATION PLAYER 1)
            if playerO==a and playerO==b and playerO==c or playerO==a and playerO==d and playerO==g or playerO==a and playerO==e and playerO==i or playerO==b and playerO==e and playerO==h or playerO==a and playerO==b and playerO==c or playerO==c and playerO==f and playerO==i or playerO==c and playerO==e and playerO==g or playerO==d and playerO==e and playerO==f or playerO==g and playerO==h and playerO==i:
                print("PLAYER 1 IS WINNER ")
                break
           
            #(WINNING SITUATION PLAYER 2)
            elif playerX==a and playerX==b and playerX==c or playerX==a and playerX==d and playerX==g or playerX==a and playerX==e and playerX==i or playerX==b and playerX==e and playerX==h or playerX==a and playerX==b and playerX==c or playerX==c and playerX==f and playerX==i or playerX==c and playerX==e and playerX==g or playerX==d and playerX==e and playerX==f or playerX==g and playerX==h and playerX==i:
                print("PLAYER 2 IS WINNER ")
                break
            else:
                pass

            
                
        
            
    elif start==2:
        break
    else:
        print("enter valid no\n")
 
