import time
def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print('Время:', round(time.perf_counter() - start, 5))
        return result
    return wrapper



@decorator
def strcounter(s):
    for sym in set(s): #set() это набор уникальных элементов
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('abcabecnealjcbkjeabckjabeckaejkcbkjackjcakckckjakjcbkjbckj')
#O(n**2)
#=============================================================================

@decorator
def strcounter_new(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1
    for sym, count in sym_counter.items():
        print(sym, count)

strcounter_new('abcabecnealjcbkjeabckjabeckaejkcbkjackjcakckckjakjcbkjbckj')
#O(n)
#=============================================================================