name = ("your name, enter your age, enter your add")
is_pos1 = name.find("enter")
is_pos2 = name.find("enter", is_pos1 + 1)
print(is_pos2)