import random


def question():
    lottery = random.choice(numbers)
    print(lottery)
    return lottery


numbers = []
for i in range(3, 21):
    numbers.append(i)

sum_ = question()
answers = []
count = 0
while count < (sum_ // 2):
    for a in range(1, sum_):
        count += 1
        for b in range(1, sum_):
            if b <= a:
                continue
            if sum_ % (a + b) == 0:
              answers.append(a)
              answers.append(b)

print(*answers, sep='')