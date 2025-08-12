if __name__ == "__main__":
    scores = []
    names = []
    results = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        results[name] = score

    scores = list(set(scores))
    scores.sort()
    low2 = scores[1]

    lowersNames = []

    for i in names:
        if results[i] == low2:
            lowersNames.append(i)

    lowersNames.sort()

    for lower in lowersNames:
        print(lower)
