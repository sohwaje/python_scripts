def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
