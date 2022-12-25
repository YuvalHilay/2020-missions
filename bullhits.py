

from random import randint

def get_random():
    while True:
        rnd = randint(1000,9999)
        ones,tens,hundreds,thusands = (rnd%10),(rnd//10)%10,(rnd//100)%10,(rnd//1000)%10
        if ones!=tens and ones!=hundreds and ones!=thusands and tens!=hundreds and tens != thusands and hundreds!=thusands:
            return rnd


def get_num():
    while 1:
        num = int(input('Enter a four digit number with non recurring digits: '))
        ones,tens,hundreds,thusands = (num%10),(num//10)%10,(num//100)%10,(num//1000)%10
        if ones!=tens and ones!=hundreds and ones!=thusands and tens!=hundreds and tens != thusands and hundreds!=thusands:
            return num
        else:
            print('Improper input')
     
    
def count_bulls(guess,random_n):
    bull_count = 0
    while random_n:
        guess,random_n,remainder_guess,remainder_random = guess//10,random_n//10,guess%10,random_n%10
        if remainder_guess==remainder_random:
            bull_count += 1
    return bull_count

def count_hits(guess,random_n):
    temp_guess= guess
    hit_count = 0
    while temp_guess:
        temp_guess,guess_remainder = temp_guess//10,temp_guess%10
        tmp = random_n
        while tmp:
            tmp,remainder_tmp = tmp//10,tmp%10
            if remainder_tmp==guess_remainder:
                hit_count += 1
                break
    return hit_count - count_bulls(guess,random_n)

def main():
    random_n = get_random()
    try_count = 0
    guess = get_num()
    while guess!=random_n:
        bullc,hitc = count_bulls(guess,random_n),count_hits(guess,random_n)
        print('Your number: %d Bull count: %d Hits count: %d'%(guess,bullc,hitc))
        try_count += 1
        guess = get_num()
    print('You win, took you %d tries' %try_count)
    
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
