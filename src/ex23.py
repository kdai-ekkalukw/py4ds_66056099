"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(qty):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    #beer_new_qty = qty - 1
    beer_zero_qty = 'No more'
    beer_part1 = 'bottles of beer on the wall,\n'
    beer_part2 = 'bottles of beer.\n'
    beer_part3 = 'Take one down, pass it around,\n'
    beer_part4 = 'bottles of beer on the wall'
    beer_last_nonzero_residual = '.'
    beer_last_zero_residual = '!'

    beer_new_qty = qty #initial value

    beer_new_qty = beer_new_qty - 1
    #while beer_new_qty != 0:
    if beer_new_qty != 0:
        #beer_new_qty = beer_new_qty - 1
        out_txt = str(qty) + ' ' + beer_part1 + str(qty) + ' ' + beer_part2 + \
            beer_part3 + str(beer_new_qty) + ' ' + beer_part4 + beer_last_nonzero_residual
        #print(out_txt)
        return out_txt
    else:
        out_txt = str(qty) + ' ' + beer_part1 + str(qty) + ' ' + beer_part2 + \
            beer_part3 + beer_zero_qty + ' ' + beer_part4 + beer_last_zero_residual
        #print(out_txt)
        return out_txt



def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    #loop_bottles_of_bears(5)
    bottles_of_beer(1)
