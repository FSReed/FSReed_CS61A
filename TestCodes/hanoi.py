def move_disk(n, from_peg, end_peg):
    print(
        "Move disk " + str(n) + " from peg " + str(from_peg) + " to peg " + str(end_peg)
    )


def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move_disk(n, start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(n - 1, start_peg, spare_peg)
        move_disk(n, start_peg, end_peg)
        solve_hanoi(n - 1, spare_peg, end_peg)


solve_hanoi(4, 1, 3)
