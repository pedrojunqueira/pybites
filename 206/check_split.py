def str_to_money(value: str) -> float:
    return float(value.strip("$"))


def str_to_pct(value: str) -> float:
    return float(value.strip("%")) / 100


def truncate_float(num, digits):
    sp = str(num).split(".")
    return float(".".join([sp[0], sp[1][:digits]]))


def adjust_to_total(total: float, splits: list) -> list:
    length = len(splits)
    result = splits[: length - 1]
    reminder = total - sum(result)
    result.append(reminder)
    return [round(r, 2) for r in result]


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

    :param item_total: str (e.g. '$8.68')
    :param tax_rate: str (e.g. '4.75%')
    :param tip: str (e.g. '10%')
    :param people: int (e.g. 3)

    :return: tuple of (grand_total: str, splits: list)
             e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    total_n = str_to_money(item_total)
    tax_rate_n = str_to_pct(tax_rate)
    tip_n = str_to_pct(tip)
    total_after_tax = total_n + (total_n * tax_rate_n)
    split_total = truncate_float(total_after_tax + (total_after_tax * tip_n), 2)
    splits = list()
    for _ in range(people):
        each_share = round(split_total / people, 2)
        splits.append(each_share)
    return (f"${split_total:.02f}", adjust_to_total(split_total, splits))


testing_data = [
    (("$8.68", "4.75%", "10%", 3), "$10.00"),
    (("$8.44", "6.75%", "11%", 3), "$10.00"),
    (("$9.99", "3.25%", "10%", 2), "$11.34"),
    (("$186.70", "6.75%", "18%", 6), "$235.17"),
    (("$191.57", "6.75%", "15%", 6), "$235.18"),
    (("$0.00", "0%", "0%", 1), "$0.00"),
    (("$100.03", "0%", "0%", 4), "$100.03"),
    (("$141.86", "2%", "18%", 9), "$170.75"),
    (("$16.99", "10%", "20%", 1), "$22.43"),
    (("$16.99", "10%", "20%", 2), "$22.43"),
    (("$16.99", "10%", "20%", 3), "$22.43"),
]

for args, result in testing_data[:8]:
    grand_total, splits = check_split(*args)
    # print(splits)
    print(f"gt:{grand_total} re:{result} ttlsplits: ${sum(splits)} list:{splits}")
    # assert grand_total == result
    # assert grand_total == f"${sum(splits)}"

import math

r = f"${sum([3.34, 3.33, 3.33])}"
print(r)
