import time

def medir_tempo(func):
    """
    Decorador que mede o tempo de execução de uma função.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"[TIMING] Função '{func.__name__}' levou {fim - inicio:.4f}s para executar.")
        return resultado
    return wrapper