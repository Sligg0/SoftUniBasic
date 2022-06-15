budget = float(input())
gpu_pieces = int(input())
cpu_pieces = int(input())
ram_pieces = int(input())

gpu_price = 250
all_gpu_price = gpu_price * gpu_pieces

cpu_price = all_gpu_price * 0.35
all_cpu_price = cpu_price * cpu_pieces

ram_price = all_gpu_price * 0.10
all_ram_price = ram_price * ram_pieces

all_pc_parts_price = all_gpu_price + all_cpu_price + all_ram_price

if gpu_pieces > cpu_pieces:
    all_pc_parts_price = all_pc_parts_price * 0.85

budget_left = budget - all_pc_parts_price
budget_need = all_pc_parts_price - budget

if budget >= all_pc_parts_price:
    print(f"You have {budget_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budget_need:.2f} leva more!")
