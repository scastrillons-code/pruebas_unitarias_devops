import pytest
from src.calculadora import sumar, dividir, promedio, minimo, raiz_cuadrada


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
