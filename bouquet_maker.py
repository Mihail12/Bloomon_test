import os
import random
import re
import time


def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}


def filter_dict_with_flowers_gt_0(dictionary):
    return tuple(filter(lambda i: i[1] > 0 and i[0] != 'count', dictionary.items()))


def make_bouquet_if_possible(bouquet_orders, flowers):
    for bouquet in bouquet_orders:
        bouquet_stats = without_keys(bouquet, {'name', 'size', 'count'})

        if all([flowers.get(flower, 0) >= count for flower, count in bouquet_stats.items()]) \
                and flowers['count'] >= bouquet['count']:
            flowers_in_the_bouquet = 0
            for flower_stats, count__stats in bouquet_stats.items():
                flowers[flower_stats] -= count__stats
                flowers['count'] -= count__stats
                flowers_in_the_bouquet += count__stats

            if flowers_in_the_bouquet < bouquet['count']:
                for _ in range(bouquet['count'] - flowers_in_the_bouquet):
                    flower_name, _ = random.choice(filter_dict_with_flowers_gt_0(flowers))
                    bouquet_stats.setdefault(flower_name, 0)
                    flowers[flower_name] -= 1
                    flowers['count'] -= 1
                    bouquet_stats[flower_name] += 1
            bouquet_to_send = f"{bouquet['name']}{bouquet['size']}" \
                              f"{''.join([f'{count}{flower}' for flower, count in bouquet_stats.items()])}"
            with open('bouquet_shop/orders.txt', 'a+') as f:
                f.write(bouquet_to_send + '\n')
            print(bouquet_to_send)
            del bouquet_orders[bouquet_orders.index(bouquet)]
            break


def bouquet_to_dict(bouquet):
    bouquet = re.split('(\d+)', bouquet)[:-1]
    result = {
        'name': bouquet[0][0],
        'size': bouquet[0][1],
        'count': int(bouquet[-1]),
    }
    flower_stat = [bouquet[1:-1][x:x+2] for x in range(0, len(bouquet[2:-1]), 2)]
    result.update({key: int(value) for value, key in flower_stat})
    return result


def bouquet_maker(file_path):
    small_bouquet_orders = []
    large_bouquet_orders = []
    small_flowers = {'count': 0}
    large_flowers = {'count': 0}
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line and line[0].isupper():
                if line[1] == 'S':
                    small_bouquet_orders.append(bouquet_to_dict(line.strip()))
                else:
                    large_bouquet_orders.append(bouquet_to_dict(line.strip()))

            elif line and line[0].islower():
                if line[1] == 'S':
                    small_flowers.setdefault(line[0], 0)
                    small_flowers[line[0]] += 1
                    small_flowers['count'] += 1
                    make_bouquet_if_possible(small_bouquet_orders, small_flowers)
                else:
                    large_flowers.setdefault(line[0], 0)
                    large_flowers[line[0]] += 1
                    large_flowers['count'] += 1
                    make_bouquet_if_possible(large_bouquet_orders, large_flowers)


if __name__ == '__main__':
    for order in os.listdir('bouquet_orders'):
        with open('bouquet_shop/orders.txt', 'a+') as f:
            f.write(f'Orders of the {order} at {time.strftime("%b %d %Y %H:%M:%S", time.gmtime(time.time()))}\n')
        bouquet_maker(f'bouquet_orders/{order}')