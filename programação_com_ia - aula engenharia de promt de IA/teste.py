def media(lista):
    if not isinstance(lista, list):
        raise TypeError("O argumento deve ser uma lista.")
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    numeros = [x for x in lista if isinstance(x, (int, float))]
    if not numeros:
        raise TypeError("A lista não contém nenhum número válido.")
    return sum(numeros) / len(numeros)


import unittest

class TestMedia(unittest.TestCase):

    def _checar(self, lista, esperado):
        resultado = media(lista)
        self.assertAlmostEqual(resultado, esperado, places=2)
        return resultado

    def _rodar(self, nome, lista, esperado):
        resultado = self._checar(lista, esperado)
        print(f"  → média = {resultado:.2f}")

    def test_lista_inteiros(self):
        print(f"\ntest_lista_inteiros", end=" ")
        self._rodar("", [2, 4, 6], 4.0)

    def test_lista_floats(self):
        print(f"\ntest_lista_floats", end=" ")
        self._rodar("", [1.5, 2.5, 3.0], 2.333)

    def test_um_elemento(self):
        print(f"\ntest_um_elemento", end=" ")
        self._rodar("", [7], 7.0)

    def test_numeros_negativos(self):
        print(f"\ntest_numeros_negativos", end=" ")
        self._rodar("", [-2, -4, -6], -4.0)

    def test_positivos_e_negativos(self):
        print(f"\ntest_positivos_e_negativos", end=" ")
        self._rodar("", [-3, 3], 0.0)

    def test_zeros(self):
        print(f"\ntest_zeros", end=" ")
        self._rodar("", [0, 0, 0], 0.0)

    def test_lista_grande(self):
        print(f"\ntest_lista_grande", end=" ")
        self._rodar("", list(range(1, 101)), 50.5)

    def test_ignora_strings(self):
        print(f"\ntest_ignora_strings", end=" ")
        self._rodar("", [1, "dois", 3], 2.0)

    def test_ignora_none(self):
        print(f"\ntest_ignora_none", end=" ")
        self._rodar("", [2, None, 4], 3.0)

    def test_lista_vazia(self):
        print(f"\ntest_lista_vazia", end=" ")
        with self.assertRaises(ValueError):
            media([])
        print("  → erro esperado: ValueError ✓")

    def test_argumento_string(self):
        print(f"\ntest_argumento_string", end=" ")
        with self.assertRaises(TypeError):
            media("123")
        print("  → erro esperado: TypeError ✓")

    def test_argumento_none(self):
        print(f"\ntest_argumento_none", end=" ")
        with self.assertRaises(TypeError):
            media(None)
        print("  → erro esperado: TypeError ✓")

    def test_argumento_tupla(self):
        print(f"\ntest_argumento_tupla", end=" ")
        with self.assertRaises(TypeError):
            media((1, 2, 3))
        print("  → erro esperado: TypeError ✓")

    def test_lista_so_strings(self):
        print(f"\ntest_lista_so_strings", end=" ")
        with self.assertRaises(TypeError):
            media(["a", "b", "c"])
        print("  → erro esperado: TypeError ✓")

    def test_resultado_e_float(self):
        print(f"\ntest_resultado_e_float", end=" ")
        self.assertIsInstance(media([1, 2, 3]), float)
        print(f"  → média = {media([1, 2, 3]):.2f}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
# ```

# A saída vai ficar assim no terminal:
# ```
# test_lista_inteiros
#   → média = 4.00 ... ok
# test_lista_floats
#   → média = 2.33 ... ok
# test_numeros_negativos
#   → média = -4.00 ... ok
# test_lista_vazia
#   → erro esperado: ValueError ✓ ... ok
# ...