import time
def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start
def example_function():
    time.sleep(1)
    return "Функція виконана"
result, execution_time = measure_time(example_function)
print(f"Результат: {result}")
print(f"Час виконання: {execution_time:.5f} секунд")
