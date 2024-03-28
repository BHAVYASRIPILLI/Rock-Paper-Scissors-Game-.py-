import random
def play():
    user=input("Enter your choice :r is rock,p is paper,s is scissors\n")
    comp=random.choice(['r','p','s'])
    if user==comp:
        return 'Its a tie'
    if is_win(user,comp):
        return 'you won'
    return 'you lost'
def is_win(player,sys):
    if (player=='r' and sys=='s') or (player=='p' and sys=='r') or (player=='s' and sys=='p'):
        return True
    
print(play())
    
