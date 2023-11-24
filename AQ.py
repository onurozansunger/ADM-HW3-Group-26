sol_found = False

def reports_generation(list_hours, sumHours, partial_solution=[], idx=0, report=[]):
    global sol_found

    #Stop if a solution is found
    if sol_found:
        return

    if idx == len(list_hours):
        if sum(partial_solution) == sumHours:
            report.append(partial_solution.copy())
            sol_found = True
        return

    for element in list_hours[idx]:
        partial_solution.append(element)
        #Prune the partial solutions with an amount of hours > sumHours
        if sum(partial_solution) <= sumHours:
            reports_generation(list_hours, sumHours, partial_solution, idx + 1, report)
        partial_solution.pop()

    reports_generation(list_hours, sumHours, partial_solution, idx + 1, report)

    return report

def main():
    global sol_found

    line1 = input().split()
    d = int(line1[0])
    sumHours = int(line1[1])

    min_max_hours = []
    list_hours = []

    for i in range(d):
        line = input().split()
        min_max_hours.append((int(line[0]), int(line[1])))
        list_hours.append(list(range(min_max_hours[-1][0], min_max_hours[-1][1] + 1)))

    sol_found = False
    reports = reports_generation(list_hours, sumHours)

    if len(reports) == 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, reports[0])))

main()