import operations

OPERATIONS = {
    "1": ("Sumar", operations.add),
    "2": ("Restar", operations.subtract),
    "3": ("Multiplicar", operations.multiply),
    "4": ("Dividir", operations.divide),
    "5": ("Potencia", operations.power),
    "6": ("Modulo", operations.modulus),
}


def get_operation():
    while True:
        print("\n--- Calculadora ---")
        for key, (name, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("0. Salir")

        choice = input("Selecciona una opcion: ").strip()

        if choice == "0":
            return None

        if choice not in OPERATIONS:
            print("Opcion invalida, intenta de nuevo.")
            continue

        return OPERATIONS[choice]


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada invalida, ingresa un numero.")


def run():
    while True:
        name, func = get_operation()
        if func is None:
            print("Hasta luego!")
            break

        print(f"\nOperacion seleccionada: {name}")
        a = get_number("Ingresa el primer numero: ")
        b = get_number("Ingresa el segundo numero: ")

        try:
            result = func(a, b)
            print(f"Resultado: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    run()
