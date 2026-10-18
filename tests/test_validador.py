import pytest
from src.validador import (
    validar_email, validar_telefono, validar_edad, validar_password,
    validar_url, validar_fecha, validar_cedula,
)


def test_validar_email_con_formato_correcto_es_valido():
    # Arrange
    email = "ana@correo.com"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is True


def test_validar_email_sin_arroba_es_invalido():
    # Arrange
    email = "anacorreo.com"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_email_con_dominio_sin_punto_es_invalido():
    # Arrange
    email = "ana@correo"
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


def test_validar_telefono_acepta_guiones_y_espacios():
    # Arrange
    telefono = "300-123 4567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is True


def test_validar_telefono_con_letras_es_invalido():
    # Arrange
    telefono = "300abc4567"
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False


def test_validar_edad_en_el_limite_de_120_es_valida():
    # Arrange
    edad = 120
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is True


def test_validar_edad_de_121_es_invalida():
    # Arrange
    edad = 121
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False


def test_validar_password_sin_mayuscula_es_invalido():
    # Arrange
    password = "clave1234"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_fecha_correcta_es_valida():
    # Arrange
    dia, mes, anio = 15, 6, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is True


def test_validar_fecha_31_de_febrero_es_invalida():
    # Arrange
    dia, mes, anio = 31, 2, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_29_de_febrero_en_anio_no_bisiesto_es_invalida():
    # Arrange
    dia, mes, anio = 29, 2, 2023
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


@pytest.mark.parametrize("email", ["", "a@b@correo.com", "@correo.com", "ana@"])
def test_validar_email_con_formato_roto_es_invalido(email):
    # Arrange: el email llega por parametrize
    # Act
    resultado = validar_email(email)
    # Assert
    assert resultado is False


@pytest.mark.parametrize("telefono", ["", "12345"])
def test_validar_telefono_vacio_o_muy_corto_es_invalido(telefono):
    # Arrange: el teléfono llega por parametrize
    # Act
    resultado = validar_telefono(telefono)
    # Assert
    assert resultado is False


@pytest.mark.parametrize("edad", ["25", -1])
def test_validar_edad_con_texto_o_negativa_es_invalida(edad):
    # Arrange: la edad llega por parametrize
    # Act
    resultado = validar_edad(edad)
    # Assert
    assert resultado is False


def test_validar_password_correcta_es_valida():
    # Arrange
    password = "Clave1234"
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is True


@pytest.mark.parametrize("password", ["", "Ab1", "CLAVE1234", "ClaveSegura"])
def test_validar_password_que_incumple_requisitos_es_invalida(password):
    # Arrange: vacía, corta, sin minúscula, sin número
    # Act
    resultado = validar_password(password)
    # Assert
    assert resultado is False


def test_validar_url_correcta_es_valida():
    # Arrange
    url = "https://www.ejemplo.com/ruta"
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is True


@pytest.mark.parametrize("url", ["", "ejemplo.com", "ftp://ejemplo.com"])
def test_validar_url_sin_http_o_vacia_es_invalida(url):
    # Arrange: la URL llega por parametrize
    # Act
    resultado = validar_url(url)
    # Assert
    assert resultado is False


@pytest.mark.parametrize("dia, mes, anio", [(15, 13, 2024), (0, 6, 2024), (15, 6, 1800), ("15", 6, 2024)])
def test_validar_fecha_con_valores_fuera_de_rango_es_invalida(dia, mes, anio):
    # Arrange: la fecha llega por parametrize
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is False


def test_validar_fecha_29_de_febrero_en_anio_bisiesto_es_valida():
    # Arrange
    dia, mes, anio = 29, 2, 2024
    # Act
    resultado = validar_fecha(dia, mes, anio)
    # Assert
    assert resultado is True


def test_validar_cedula_con_6_a_10_digitos_es_valida():
    # Arrange
    cedula = "1053123456"
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is True


@pytest.mark.parametrize("cedula", ["", "10A3456", "12345", "12345678901"])
def test_validar_cedula_con_letras_o_longitud_incorrecta_es_invalida(cedula):
    # Arrange: la cédula llega por parametrize
    # Act
    resultado = validar_cedula(cedula)
    # Assert
    assert resultado is False
