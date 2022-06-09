def rental_car_cost(d):
    if d >= 7:
        return (d*40)-50
    elif d >= 3:
        return(d*40)-20
    else:
        return d*40


print(rental_car_cost(8))
print(rental_car_cost(6))
print(rental_car_cost(1))
print(rental_car_cost(3))