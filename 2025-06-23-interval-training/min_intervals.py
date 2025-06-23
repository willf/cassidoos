import queue

"""Interview question of the week



This week's question:
You’re given an array of siren objects, each with a start and end time in seconds,
representing when the siren is active.
Write a function to return the minimum number of sirens
you need to remove so that no two sirens overlap.

Example:

removeSirens([
  { start: 1, end: 5 },
  { start: 3, end: 7 },
  { start: 6, end: 9 },
  { start: 8, end: 10 }
]);
> 1

removeSirens([
  { start: 0, end: 3 },
  { start: 2, end: 4 },
  { start: 5, end: 7 },
  { start: 6, end: 8 },
  { start: 8, end: 10 }
])
> 2
"""

# Let's create some accessors and comparion functions.


def interval_start(interval):
    return interval["start"]


def interval_end(interval):
    return interval["end"]


def not_overlaps_one_way(int_a, int_b):
    return (
        interval_start(int_a)
        < interval_end(int_a)
        < interval_start(int_b)
        < interval_end(int_b)
    )


def not_overlaps(int_a, int_b):
    return not_overlaps_one_way(int_a, int_b) or not_overlaps_one_way(int_b, int_a)


# interval: {'start': 6, 'end': 9}; current: [{'start': 1, 'end': 5}]
def overlaps(int_a, int_b):
    return not not_overlaps(int_a, int_b)


# OK, let's define a 'state'.
# A state has
# - a current set of intervals, which do not overlap (could be empty)
# - a remaining set of intervals that must be considered
# If the remaining set is empty, the state is an end state


def create_state(current, remaining):
    return {"current": current, "remaining": remaining}


def state_current(state):
    return state["current"]


def state_remaining(state):
    return state["remaining"]


def is_complete(state):
    return not state_remaining(state)


## Ok, now we need a queue of states
## We will just use the queue.Queue class


# we can expand a state by adding new states
# to the queue:
# for each interval in the remainder,
# if it is non-overlapping with all states in current
# create a new state with the interval added to current
# and removed from remaining
def expand(state, q):
    for interval in state_remaining(state):
        # print(f"interval: {interval}; current: {state_current(state)}")
        if all([not overlaps(interval, c) for c in state_current(state)]):
            new_current = state_current(state).copy()
            new_remaining = state_remaining(state).copy()
            new_current.append(interval)
            new_remaining.remove(interval)
            new_state = create_state(new_current, new_remaining)
            # print(f"Adding new state: {new_state}")
            q.put(new_state)
        else:
            # print(f"Not adding...")
            pass


def initialize_problem(input):
    # the input is a list of siren intervals
    initial_state = create_state([], input)
    q = queue.SimpleQueue()
    q.put(initial_state)
    return q


def solve_returning_solutions(q):
    solutions = []
    # while the queue is not empty
    while not q.empty():
        state = q.get()
        solutions.append(state_current(state))
        # print(f"Expanding ... {state}")
        expand(state, q)
    return solutions


def solve(states):
    q = initialize_problem(states)
    solutions = solve_returning_solutions(q)
    max_length = max([len(solution) for solution in solutions])
    current_length = len(states)
    return current_length - max_length


def solve_verbosely(states):
    q = initialize_problem(states)
    solutions = solve_returning_solutions(q)
    for solution in solutions:
        print(f"A solution is: {solution}")
    max_length = max([len(solution) for solution in solutions])
    current_length = len(states)
    return current_length - max_length


problem_1 = [
    {"start": 1, "end": 5},
    {"start": 3, "end": 7},
    {"start": 6, "end": 9},
    {"start": 8, "end": 10},
]

# print(solve(problem_1))

problem_2 = [
    {"start": 0, "end": 3},
    {"start": 2, "end": 4},
    {"start": 5, "end": 7},
    {"start": 6, "end": 8},
    {"start": 8, "end": 10},
]
print(f"Searching for solutions to {problem_1}")
print(f"Need to remove {solve(problem_1)} siren(s).")
print(f"Searching for solutions to {problem_2}")
print(f"Need to remove {solve(problem_2)} siren(s).")
