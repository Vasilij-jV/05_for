list_cars = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0

for car in list_cars:
    print('Я езжу на автомобиле марки ', car)
    if list_cars.index(car) > 0:
        cars_count += 10
        print(cars_count)