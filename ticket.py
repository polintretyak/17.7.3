def calculate_ticket_cost():
    num_tickets = int(input("Введите количество билетов: "))

    total_cost = 0
    under_18_count = 0

    for i in range(num_tickets):
        age = int(input(f"Введите возраст посетителя {i+1}: "))

        if age < 18:

            under_18_count += 1
        elif age >= 18 and age < 25:
            total_cost += 990
        else:
            total_cost += 1390

    if num_tickets > 3:
        total_cost *= 0.9

    print(f"Сумма к оплате: {total_cost} руб.")

calculate_ticket_cost()
