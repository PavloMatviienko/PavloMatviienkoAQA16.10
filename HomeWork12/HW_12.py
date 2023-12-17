from functools import wraps


def lru_cache(max_size=128):
    cache = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]

            result = func(*args, **kwargs)
            if len(cache) >= max_size:
                # Видаляємо найменш використовуваний елемент
                cache.pop(next(iter(cache)))

            cache[key] = result
            return result

        return wrapper

    return decorator


@lru_cache(max_size=3)
def example_function(x):
    print(f"Calculating for {x}")
    return x * 2


def main():
    print(example_function(2))  # Виклик функції, результат буде закешований
    print(example_function(3))  # Виклик функції, результат буде закешований
    print(example_function(2))  # Результат буде взято з кеша, не буде повторного обчислення
    print(example_function(4))  # Виклик функції, результат буде закешований


if __name__ == "__main__":
    main()
