
# current_day -текущий день,
# day - возраст популяции, количество мух
def dec(current_day,pop_age, fly_count):
    print(current_day,pop_age, fly_count)
    if pop_age > fly_age:
        print(1)
        return 0 #все умерли
    elif current_day == max_day:
        print(2)
        return fly_count # мух на предельный момент
    elif current_day > max_day and pop_age == 0:
        print(3)
        return 0  # ещё не родившаяся популяция
    elif current_day > max_day and pop_age != 0:
        print(4)
        return fly_count # ещё не родившаяся популяция

    return dec(current_day + fly_refresh, pop_age + fly_refresh, fly_count) + \
           dec(current_day + fly_generation, 0, fly_count*50)

fly_age = 30
fly_refresh = 5
fly_generation = 5
max_day = 50


p_list = [0,0,0,0,1]
num = dec(0,0,1)
L = 45000000000
S = 4*3.1415*6400000**2
print(num, num/S, num/L)