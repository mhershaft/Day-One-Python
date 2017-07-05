import time
print "Wanna play Rock Paper Scissors? Awesome! Let's Do It!"
while True==True:
    your_pick=raw_input("Your Choice\n")
    import random
    my_pick=random.randint(0,2)
    if my_pick==0:
        print "My Choice is Rock!"
    elif my_pick==1:
        print "My Choice is Paper!"
    else:
        print "My Choice is Scissors!"
    if my_pick==0 and your_pick=="Scissors":
        print "I Win!"
    elif my_pick==0 and your_pick=="Paper":
        print "You Win!"
    elif my_pick==0 and your_pick=="Rock":
        print "Tie!"
    elif my_pick==1 and your_pick=="Rock":
        print "I Win!"
    elif my_pick==1 and your_pick=="Paper":
        print "Tie!"
    elif my_pick==1 and your_pick=="Scissors":
        print "You Win!"
    elif my_pick==2 and your_pick=="Rock":
        print "You Win!"
    elif my_pick==2 and your_pick=="Paper":
        print "I Win!"
    else:
        print "Tie!"
    time.sleep(2)
    print "Let's Play Again!"
    time.sleep(2)
