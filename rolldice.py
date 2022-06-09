import itertools
import random

def score(dice):
    set_dice = set(dice)
    sorted_dice = sorted(dice)
    group_nums = sorted([len(list(grp)) for i, grp in itertools.groupby(sorted_dice)], reverse=True)

    small_straights =  (set([1,2,3,4]), set([2,3,4,5]), set([3,4,5,6]))
    scores = [
        ("JACKPOT!", lambda: group_nums[0] == 5),
        ("FOUR OF A KIND", lambda: group_nums[0] == 4),
        ("FULL HOUSE", lambda: group_nums == [3, 2]),
        ("STRAIGHT", lambda: sorted_dice in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])),
        ("SMALL STRAIGHT", lambda: any(seq <= set_dice for seq in small_straights)),  #>
        ("THREE OF A KIND", lambda: group_nums[0] == 3),
        ("TWO PAIR", lambda: group_nums[:2] == [2, 2]),
        ("PAIR", lambda: group_nums[0] == 2),
        ("CHANCE", lambda: True),
    ]

    return next(score for score, cond in scores if cond())

# accessor to DOM object for outputting results
display_results = Element("display-results")

# some helpful strings
dice = "_\N{DIE FACE-1}\N{DIE FACE-2}\N{DIE FACE-3}\N{DIE FACE-4}\N{DIE FACE-5}\N{DIE FACE-6}"
popper = "\N{PARTY POPPER}"
br = "<br>"

def roll_dice(evt):
    """Event handler for clicking on Roll! button"""
    dice_roll = [random.randint(1, 6) for _ in range(5)]
    jackpot = len(set(dice_roll)) == 1
    dice_score = score(dice_roll)

    dice_output = " ".join(dice[i] for i in dice_roll)
    display_results.write(f"{dice_output}{br}{dice_score}{br}Total: {sum(dice_roll)}{(br + popper*3) if jackpot else ''}")

# start off with a roll when first showing page
roll_dice(None)
