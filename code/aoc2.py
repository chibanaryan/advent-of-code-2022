first = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}
second = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
needed_result = {
    "X": "Lost",
    "Y": "Draw",
    "Z": "Won",
}

shape_score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}
result_score = {
    "Lost": 0,
    "Draw": 3,
    "Won": 6,
}


if __name__ == "__main__":
    with open('inputs/input2.txt') as f:
        lines = f.readlines()
    score_part1 = 0
    score_part2 = 0
    for line in lines:
        result = ""
        split_line = line.split(' ')
        f, s = split_line[0], split_line[1].removesuffix('\n')
        if first[f] == "Rock" and second[s] == "Paper" or (first[f] == "Paper" and second[s] == "Scissors") or (first[f] == "Scissors" and second[s] == "Rock"):
            result = "Won"
        elif first[f] == second[s]:
            result = "Draw"
        else:
            result = "Lost"
        
        score_part1 += shape_score[second[s]]
        score_part1 += result_score[result]

        target = needed_result[s]
        if target == "Draw":
            second_choice = first[f]
        elif target == "Won":
            if first[f] == "Rock":
                second_choice = "Paper"
            elif first[f] == "Paper":
                second_choice = "Scissors"
            else:
                second_choice = "Rock"
        else:
            if first[f] == "Rock":
                second_choice = "Scissors"
            elif first[f] == "Paper":
                second_choice = "Rock"
            else:
                second_choice = "Paper"
        score_part2 += shape_score[second_choice]
        score_part2 += result_score[target]
    print(score_part1)
    print(score_part2)