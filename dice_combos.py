def pair(dice):   # One list
    dice_copy = dice.copy()
    list_set = set(dice_copy)
    if len(list_set) == len(dice_copy):
        return 0
    dice_copy.sort(reverse=True)
    k = 1
    while dice_copy[k] != dice_copy[k-1]:
        k += 1
        if k == len(dice_copy):
            break
    return 2*dice_copy[k]


def two_pair(dice):
    dice_copy = dice.copy()
    dice_copy.sort(reverse=True)
    list_set = set(dice_copy)
    if len(list_set) < 2 or len(list_set) > 3:
        return 0
    if len(list_set) == 2:
        return 2*dice_copy[0] + 2*dice_copy[-1]
    else:
        print('Vi har tre unika tal i listan')




    return 12


def three_of_a_kind(dice):
    if not len(set(dice)) == 3:
        if not len(set(dice)) == 2:

            print('We cannot get a tree of a kind')
            print(len(set(dice)))
            return 0

    copy = dice.copy()
    copy.sort()
    k = 1
    while k <= 3:
        if copy[k] == 1/3*(copy[k-1]+copy[k]+copy[k+1]):
            return 3*copy[k]
        else:
            k += 1




def four_of_a_kind(dice):
    if not len(set(dice)) == 2:
        print('Cannot get four of a kind')
        return 0
    copy = dice.copy()
    copy.sort()
    k = 1
    while k <= 2:
        if copy[k] == copy[k-1] and copy[k] == copy[k+2]:
            return 4 * copy[k]
        else:
            k += 1
    return 0


def small_straight(dice):
    copy = dice.copy()
    copy.sort(reverse=True)
    print(copy)
    return 1


if __name__ == '__main__':
    dice = [1, 2, 3, 4, 6]
    A = small_straight(dice)
    print(len(set(dice)))
    #print(A)





