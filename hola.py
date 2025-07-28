
def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso:
print(es_primo(7))  # Debería imprimir True
print(es_primo(10)) # Debería imprimir False