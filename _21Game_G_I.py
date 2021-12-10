from random import *
Ask_User=1
while True:
    while type(Ask_User)!=str:
        try:
            Ask_User=str(input("Желаете сыграть? Да \ Нет "))
        except:
            ValueError
            print("Ошибка вводе!")
    if Ask_User.lower()=="да":
        Desk_1=[6,7,8,9,10,2,3,4,11]
        Desk_all=Desk_1*4
        shuffle(Desk_all)
        Point_1=0
        Point_2=0
        Ask_User_2=1
        while type(Ask_User_2)!=str:
            try:
                Ask_User_2=str(input("С игроком или ботом устроить схватку? Бот \ Игрок "))
            except:
                ValueError
                print("Ошибка вводе!")
            if Ask_User_2.lower()=="бот":
                Ask_Money=" "
                Ask_Bet=" "
                while type(Ask_Money)!=int:
                    try:
                        Ask_Money=int(input("Сколько у вас денег? "))
                    except:
                        ValueError
                        print("Ошибка ввода!")
                while type(Ask_Bet)!=int:
                    try:
                        Ask_Bet=int(input("Какова ваша ставка? "))
                    except:
                        ValueError
                        print("Ощибка вводе!")
                while True:
                    if Point_1==21:
                        print("Бот выиграл! Вы проиграли. . .")
                        break
                    elif Point_1>21:
                        print("Вы выиграли! Бот проиграл. . .")
                        break
                    elif Point_2==21:
                        print("Вы выиграли! Бот проиграл. . .")
                        break
                    elif Point_2>21:
                        print("Бот выиграл! Вы проиграли. . .")
                        break
                    print("Ход бота!")
                    Point_1+=Desk_all.pop(0)
                    print(f"У противника {Point_1} очков!")
                    print("Ваш ход!")
                    Ask_User_3=1
                    Ask_Bet=""
                    print(f"У вас {Point_2} очков!")
                    while type(Ask_User_3)==int:
                        try:
                            Ask_User_3=str(input("Будете брать карту? Да \ Нет "))
                        except:
                            ValueError
                            print("Ощибка в воде!(пасхалка кака)")
                    if Ask_User_3.lower()=="да":
                        Point_2+=Desk_all.pop(0)
                    else:
                        print(f"У вас {Point_2} очков!")
            if Ask_User_2.lower()=="игрок":
                Ask_Money_1=" "
                Ask_Money_2=" "
                Ask_Bet_1= " "
                Ask_Bet_2=" "
                while type(Ask_Money_1)!=int:
                    try:
                        Ask_Money=int(input("Сколько у вас денег игрок номер 1? "))
                    except:
                        ValueError
                        print("Ошибка ввода!")
                while type(Ask_Money_2)!=int:
                    try:
                        Ask_Money_2=int(input("Сколько у вас денег игрок номер 2? "))
                    except:
                        ValueError
                        print("Ошибка ввода!")
                while type(Ask_Bet_1)!=int:
                    try:
                        Ask_Bet=int(input("Какова ваша ставка игрок номер 1? "))
                    except:
                        ValueError
                        print("Ошибка ввода!")
                    while type(Ask_Bet_2)!=int:
                        try:
                            Ask_Bet=int(input("Какова ваша ставка игрок номер 2? "))
                        except:
                            ValueError
                            print("Ошибка ввода!")
                if Ask_Bet_1!=Ask_Bet_2:
                    while type(Ask_Bet_1)!=int:
                        try:
                            Ask_Bet=int(input("Какова ваша ставка игрок номер 1? "))
                        except:
                            ValueError
                            print("Ошибка ввода!")
                    while type(Ask_Bet_2)!=int:
                        try:
                            Ask_Bet=int(input("Какова ваша ставка игрок номер 2? "))
                        except:
                            ValueError
                            print("Ошибка ввода!")
                else:
                    Ask_Money_1-=Ask_Bet_1
                    Ask_Money_2-=Ask_Bet_2
                while True:
                    if Point_1==21:
                        print("Выиграл игрок номер 1! Проиграл игрок номер 2. . .")
                        Ask_Money_1=Ask_Money_1+Ask_Bet_1*2
                        break
                    elif Point_1>21:
                        print("Выиграл игрок номер 2! Проиграл игрок номер 1. . .")
                        Ask_Money_2=Ask_Money_2+Ask_Bet_1*2
                        break
                    elif Point_2==21:
                        print("Выиграл игрок номер 2! Проиграл игрок номер 1. . .")
                        Ask_Money_2=Ask_Money_2+Ask_Bet_1*2
                        break
                    elif Point_2>21:
                        print("Выиграл игрок номер 1! Проиграл игрок номер 2. . .")
                        Ask_Money_1=Ask_Money_1+Ask_Bet_1*2
                        break
                    print("Ход Игрока номер 1!")
                    Ask_User_3=1
                    print(f"У игрока номер 1 {Point_1} очков!")
                    while type(Ask_User_3)==int:
                        try:
                            Ask_User_3=str(input("Будете брать карту игрок номер 1? Да \ Нет "))
                        except:
                            ValueError
                            print("Ощибка в воде!(пасхалка кака)")
                    if Ask_User_3.lower()=="да":
                        Point_1+=Desk_all.pop(0)
                        print(f"У игрока номер 1 {Point_1} очков!")
                    else:
                        print(f"У игрока номер 1 {Point_1} очков!")
                    print("Ход игрока номер 2!")
                    Ask_User_3=1
                    print(f"У игрока номер 2 {Point_2} очков!")
                    while type(Ask_User_3)==int:
                        try:
                            Ask_User_3=str(input("Будете брать карту? Да \ Нет "))
                        except:
                            ValueError
                            print("Ощибка в воде!(пасхалка кака)")
                    if Ask_User_3.lower()=="да":
                        Point_2+=Desk_all.pop(0)
                        print(f"У игрока номер 2 {Point_2} очков!")
                    else:
                        print(f"У игрока номер 2 {Point_2} очков!")


                
    else:
        print("Всего хорошего!")
        break

