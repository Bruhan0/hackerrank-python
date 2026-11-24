def avg_score(student_marks ,query_name):
    marks = student_marks[query_name]
    print(f"{sum(marks)/3:.2f}")
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score(student_marks,query_name)
