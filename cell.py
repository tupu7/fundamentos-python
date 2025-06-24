def load_file():
    filepath = input("Enter the path to the file: ")

    file = open(filepath, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    return lines


def ser_environment(raw_file):
    env = []

    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env


def pri_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print("cuadrado_rojo", end="")
            else:
                print(" ", end="")
        print()


mi_file = load_file()
print(mi_file)
env = ser_environment(mi_file)
print(env)
pri_env(env)

def vecinos_cheque(env, x, y):
    count = 0
    L1 = [x-1, x, x+1]
    L2 = [y-1, y, y+1]
    for i in L1:
        for j in L2:
            if x == i and y == j:
                continue
            if env[i][j] == 1:
                cont += 1
    return count