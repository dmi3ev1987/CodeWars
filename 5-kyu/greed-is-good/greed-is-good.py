SCORE_DICT = {
    1:
        {
            1: 100,
            5: 50,
        },
    3:
        {
            1: 1000,
            6: 600,
            5: 500,
            4: 400,
            3: 300,
            2: 200,
        }
}
def score(dice):
    score = 0
    dice_set = set(dice)
    dice_dict = {}
    for number in dice_set:
        dice_dict[number] = dice.count(number)
    for key, value in dice_dict.items():
        triple = 0
        ones = value
        if value >= 3:
            triple = value // 3
            ones = value % 3
        if key in SCORE_DICT[1]:
            result = SCORE_DICT[1][key]
            score += result  * ones
        if key in SCORE_DICT[3]:
            result = SCORE_DICT[3][key]
            score += result  * triple
    return score