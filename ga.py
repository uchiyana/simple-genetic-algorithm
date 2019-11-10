import random
import string
from itertools import zip_longest


class DNA:
    def __init__(self, size):
        self.genes = random.choices(
            string.ascii_letters + string.digits + string.whitespace, k=size)

    def calc_fitness(self, target):
        self.fitness = sum([(g == t)
                            for g, t in zip_longest(self.genes, target)])

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if(random.random() < mutation_rate):
                self.genes[i] = random.choice(
                    string.ascii_letters + string.digits + string.whitespace)

    def crossover(self, partner):
        midpoint = random.randrange(0, len(self.genes)-1)
        child = DNA(len(self.genes))
        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]
        return child


def main():
    print("Hello")


if __name__ == "__main__":
    main()
