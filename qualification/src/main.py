from helpers import naive_solution, dead_streets_solution, most_traversed_weighted
from read_input import read_problem

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    context = read_problem(f'./input/b.txt')
    most_traversed_weighted(context, 'b')
