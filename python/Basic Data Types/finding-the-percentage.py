if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for name, score in student_marks.items():
        if query_name == name:
            Average = sum(score) / 3

    print(f"{Average:.2f}")
