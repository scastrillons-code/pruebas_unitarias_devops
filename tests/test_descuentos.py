import pytest
from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado,
)


def test_aplicar_descuento_de_25_por_ciento():
    # Arrange
    precio, porcentaje = 200, 25
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 150


def test_aplicar_descuento_del_100_por_ciento_devuelve_cero():
    # Arrange
    precio, porcentaje = 100, 100
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0


def test_aplicar_descuento_con_porcentaje_mayor_a_100_lanza_error():
    # Arrange
    precio, porcentaje = 100, 101
    # Act y Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_con_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -50, 10
    # Act y Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_calcular_descuento_devuelve_el_monto_descontado():
    # Arrange
    precio, porcentaje = 200, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 20


def test_precio_final_aplica_el_impuesto_sobre_el_precio_con_descuento():
    # Arrange: 100 con 20% de descuento = 80; el 10% de impuesto va sobre 80
    precio, impuesto, descuento = 100, 10, 20
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(88)


def test_precio_final_sin_impuesto_ni_descuento_no_cambia_el_precio():
    # Arrange
    precio, impuesto, descuento = 100, 0, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 100


def test_descuento_por_volumen_en_el_limite_de_10_unidades_aplica_5_por_ciento():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(95)


def test_descuento_por_volumen_con_9_unidades_no_aplica_descuento():
    # Arrange
    cantidad, precio_unitario = 9, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 90


def test_descuento_por_volumen_con_100_unidades_aplica_20_por_ciento():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(800)


def test_descuento_cumulativo_aplica_cada_descuento_sobre_el_resultado_anterior():
    # Arrange: 100 -> 90 -> 81
    precio, descuentos = 100, [10, 10]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(81)


def test_descuento_apilado_suma_los_porcentajes():
    # Arrange: 10 + 10 = 20% sobre 100
    precio, descuentos = 100, [10, 10]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(80)


def test_descuento_apilado_que_supera_el_100_por_ciento_deja_el_precio_en_cero():
    # Arrange: 60 + 60 = 120%
    precio, descuentos = 100, [60, 60]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0


@pytest.mark.parametrize("precio, porcentaje", [(-1, 10), (100, -5), (100, 101)])
def test_calcular_descuento_con_datos_invalidos_lanza_error(precio, porcentaje):
    # Arrange: los datos llegan por parametrize
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


@pytest.mark.parametrize("precio, impuesto, descuento", [(-1, 0, 0), (100, -5, 0), (100, 0, 101)])
def test_calcular_precio_final_con_datos_invalidos_lanza_error(precio, impuesto, descuento):
    # Arrange: los datos llegan por parametrize
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


@pytest.mark.parametrize("cantidad, precio_unitario", [(-1, 10), (5, -10)])
def test_descuento_por_volumen_con_datos_negativos_lanza_error(cantidad, precio_unitario):
    # Arrange: los datos llegan por parametrize
    # Act y Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_por_volumen_con_50_unidades_aplica_15_por_ciento():
    # Arrange
    cantidad, precio_unitario = 50, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(425)


def test_descuento_por_volumen_con_20_unidades_aplica_10_por_ciento():
    # Arrange
    cantidad, precio_unitario = 20, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(180)


def test_descuento_cumulativo_con_lista_vacia_devuelve_el_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100


@pytest.mark.parametrize("precio, descuentos", [(-1, [10]), (100, [10, 150])])
def test_descuento_cumulativo_con_datos_invalidos_lanza_error(precio, descuentos):
    # Arrange: los datos llegan por parametrize
    # Act y Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_descuento_apilado_con_lista_vacia_devuelve_el_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_apilado_con_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -1, [10]
    # Act y Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)
