"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(pplen):
    # TODO : complete this
    #at least 12 char regardless of input
    #must have at least one for each category

    eligible_char = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    len_eligible = len(eligible_char)
    random_pos = random.randint(0,len_eligible-1)

    plen = pplen
    if(plen < 12):
        plen = 12

    random_pos_upper = random.randint(0,plen - 1)
    random_pos_lower = random.randint(0,plen - 1)
    random_pos_numbers = random.randint(0,plen - 1)
    random_pos_special = random.randint(0,plen - 1)

    s_random_pos_mandatory = {-1}
    while len(s_random_pos_mandatory) < 5:
        random_pos_mandatory = random.randint(0,plen - 1)
        s_random_pos_mandatory.add(random_pos_mandatory)

    rand_pos_upper = s_random_pos_mandatory.remove(-1)
    gen_pass = []
    for i in range(0,plen):
        gen_pass.insert(i,'_')

    rand_pos_upper = s_random_pos_mandatory.pop()
    rand_passpos_upper = random.randint(0,len(UPPER_LETTERS)-1)
    gen_pass[rand_pos_upper] = UPPER_LETTERS[rand_passpos_upper]

    rand_pos_lower = s_random_pos_mandatory.pop()
    rand_passpos_lower = random.randint(0,len(LOWER_LETTERS)-1)
    gen_pass[rand_pos_lower] = LOWER_LETTERS[rand_passpos_lower]

    rand_pos_num = s_random_pos_mandatory.pop()
    rand_passpos_num = random.randint(0,len(NUMBERS)-1)
    gen_pass[rand_pos_num] = NUMBERS[rand_passpos_num]

    rand_pos_spe = s_random_pos_mandatory.pop()
    rand_passpos_spe = random.randint(0,len(SPECIAL)-1)
    gen_pass[rand_pos_spe] = SPECIAL[rand_passpos_spe]

    random_passpos_eligible = 0
    for i in range(0,plen):
        if i not in s_random_pos_mandatory:
            random_passpos_eligible = random.randint(0,len_eligible-1)
            gen_pass[i] = eligible_char[random_passpos_eligible]

    gen_pass_str = str(gen_pass)
    gen_pass_str = "".join(gen_pass)
    #testlen = len(gen_pass_str) #ok, but outside assert NOK
    #gen_pass_str = 'abcdefghijklm' #ok
    gen_pass_str = ''
    for i in gen_pass:
        gen_pass_str = gen_pass_str + i
    return gen_pass_str
