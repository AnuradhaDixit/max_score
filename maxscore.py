student_scores = input().split()
highest_score = 0
for n in range(0, len(student_scores)) :
    student_scores[n] = int(student_scores[n])
    for score in student_scores :
        if highest_score <= student_scores[n] :
            highest_score = student_scores[n]
print(highest_score)
