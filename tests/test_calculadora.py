import pytest
from src.calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada, promedio, maximo, minimo, calcular_area_rectangulo, calcular_perimetro_rectangulo


def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act y Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act y Assert
    with pytest.raises(ValueError):
        promedio(lista)


def test_minimo_lista_de_positivos_devuelve_el_menor():
    # Arrange
    lista = [3, 5, 8]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3


def test_raiz_cuadrada_de_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act y Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)
def test_restar_con_resultado_negativo():
    # Arrange
    a, b = 3, 5
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -2


def test_multiplicar_por_cero_devuelve_cero():
    # Arrange
    a, b = 7, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0


def test_dividir_enteros_devuelve_decimal():
    # Arrange
    a, b = 7, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 3.5


def test_potencia_con_exponente_cero_devuelve_uno():
    # Arrange
    base, exponente = 5, 0
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 1


def test_raiz_cuadrada_de_cero_devuelve_cero():
    # Arrange
    numero = 0
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 0


def test_maximo_con_todos_negativos_devuelve_el_mayor():
    # Arrange
    lista = [-5, -2, -9]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == -2


def test_minimo_con_un_solo_elemento_devuelve_ese_elemento():
    # Arrange
    lista = [7]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 7


def test_area_rectangulo_con_base_negativa_lanza_error():
    # Arrange
    base, altura = -3, 4
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)


def test_perimetro_rectangulo_calcula_correctamente():
    # Arrange
    base, altura = 3, 4
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 14


def test_promedio_de_una_lista_devuelve_la_media():
    # Arrange
    lista = [2, 4, 6]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 4


def test_minimo_con_el_menor_al_final_de_la_lista_lo_encuentra():
    # Arrange
    lista = [8, 5, 3]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3


@pytest.mark.parametrize("funcion", [maximo, minimo])
def test_maximo_y_minimo_con_lista_vacia_lanzan_error(funcion):
    # Arrange: la función llega por parametrize
    lista = []
    # Act y Assert
    with pytest.raises(ValueError):
        funcion(lista)


def test_area_rectangulo_calcula_base_por_altura():
    # Arrange
    base, altura = 3, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 12


def test_perimetro_rectangulo_con_altura_negativa_lanza_error():
    # Arrange
    base, altura = 3, -4
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)
