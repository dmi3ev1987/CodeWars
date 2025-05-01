from collections import Counter
​
SCORE_RULES = {
    1: {1: 100, 5: 50},
    3: {
        1: 1000,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600,
    },
}
​
​
def score(dice):
    total_score = 0
    counts = Counter(dice)
​
    for die_value, count in counts.items():
        triples = count // 3
        singles = count % 3
​
        if die_value in SCORE_RULES[1]:
            total_score += SCORE_RULES[1][die_value] * singles
        if die_value in SCORE_RULES[3]:
            total_score += SCORE_RULES[3][die_value] * triples
    return total_score
​