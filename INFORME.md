# Informe: Análisis y mejora de pruebas unitarias

## 1. Datos

- **Nombre:** Santiago Castrillon Salazar
- **Fecha:** 17 de octubre de 2026
- **Repositorio:** https://github.com/scastrillons-code/pruebas_unitarias_devops
- **Módulos trabajados:** `calculadora` y `descuentos` (obligatorios) y `validador` (tercer módulo)

Todas las pruebas siguen la estructura AAA (Arrange-Act-Assert) y están en la carpeta `tests/`. En el historial de commits, cada módulo tiene primero un commit de pruebas (con los bugs en rojo) y después un commit `fix:` con la corrección.

## 2. Análisis por módulo

### calculadora
**Qué hace:** funciones matemáticas básicas: operaciones aritméticas (`sumar`, `restar`, `multiplicar`, `dividir`, `potencia`, `raiz_cuadrada`), estadísticos de listas (`promedio`, `maximo`, `minimo`) y geometría del rectángulo (área y perímetro).

**Qué probé y por qué:** elegí los casos por criterio y no por cantidad, buscando los valores donde una función suele romperse: el cero (multiplicar por 0, raíz de 0, exponente 0), los negativos (raíz de -4, base negativa, lista solo con negativos), las listas especiales (vacía y de un solo elemento) y la división por cero. También probé que el mínimo aparezca en cualquier posición de la lista, no solo al inicio, porque ahí es donde falló `minimo`.

### descuentos
**Qué hace:** calcula precios con descuentos e impuestos: descuento simple, monto del descuento, precio final con impuesto, descuento por volumen (por tramos), descuento cumulativo (cada uno sobre el resultado anterior) y descuento apilado (porcentajes sumados).

**Qué probé y por qué:** los bordes de cada tramo del descuento por volumen (9 y 10 unidades, y también 20, 50 y 100), porque los errores por tramos suelen estar justo en el límite. Probé el 100% y más del 100%, los precios e impuestos negativos y las listas vacías. Comparé de forma explícita el descuento cumulativo (100, 90, 81) con el apilado (100 con 20% da 80), porque confundirlos es un error conceptual clásico.

### validador
**Qué hace:** valida el formato de datos de entrada: email, teléfono, edad, contraseña, URL, fecha y cédula.

**Qué probé y por qué:** para cada validador, un caso válido y varios inválidos que representan cada regla (email sin arroba, con doble arroba o con dominio sin punto, contraseña sin mayúscula o sin número, etc.). Probé los límites de la edad (120 es válido, 121 no) y, en fechas, casos de calendario (31 de febrero, 29 de febrero en año bisiesto y no bisiesto). Elegí este módulo porque recibe datos simples, se prueba sin mocks y tiene un bug documentado que además da puntaje extra.

## 3. Tabla de bugs

1. **`minimo`**: con `[3, 5, 8]` devolvía `0` y debía devolver `3`. Lo corregí empezando con `min_val = lista[0]`.
2. **`raiz_cuadrada`**: con `-4` no lanzaba error y debía lanzar `ValueError`. Agregué la validación `numero < 0`.
3. **`calcular_precio_final`**: con `(100, 10, 20)` daba `90` y debía dar `88`. El impuesto se calculaba sobre el precio original; ahora se calcula sobre el precio con descuento.
4. **`descuento_apilado`**: con `(100, [60, 60])` lanzaba un `ValueError` y debía dar `0`. Limité la suma de los descuentos a 100.
5. **`validar_fecha`**: con `(31, 2, 2024)` daba `True` y debía dar `False`. Ahora usa `calendar.monthrange` para saber cuántos días tiene cada mes. Está en un módulo no obligatorio (punto extra).

## 4. Cobertura

Salida de `pytest tests/ -q --cov=src --cov-report=term-missing`:

```
........................................................................ [ 83%]
..............                                                           [100%]

---------- coverage: platform linux, python 3.13.5-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/__init__.py                0      0   100%
src/autenticacion.py          42     42     0%   6-77
src/calculadora.py            44      0   100%
src/conversor.py              56     56     0%   6-94
src/csv_parser.py             76     76     0%   6-127
src/descuentos.py             58      0   100%
src/fibonacci.py              42     42     0%   6-73
src/manipulador_texto.py      93     93     0%   6-156
src/procesador_texto.py       49     49     0%   6-84
src/utils.py                  53     53     0%   6-92
src/validador.py              66      0   100%
--------------------------------------------------------
TOTAL                        579    411    29%

86 passed in 0.18s
```
**Lectura de resultados:** los tres módulos trabajados (`calculadora.py`, `descuentos.py` y `validador.py`) superan la meta del 85%. La fila TOTAL aparece baja porque el comando mide todos los archivos de `src/`, y los otros siete módulos no hicieron parte de este trabajo; la meta aplica solo a los módulos trabajados.

## 5. Reflexión final

**¿Qué NO mide la cobertura?**

La cobertura mide qué líneas del código se ejecutaron mientras corrían las pruebas, pero no dice si los resultados fueron correctos ni si las pruebas verifican lo suficiente. Mi propio trabajo lo mostró de dos maneras. En `minimo`, la línea `min_val = 0` se ejecutaba y contaba como cubierta, aunque era justamente el bug: una línea puede estar cubierta y estar mal. En `validar_fecha`, una sola prueba con una fecha válida recorre casi toda la función sin detectar que acepta el 31 de febrero; el error solo apareció cuando probé fechas imposibles. Tampoco mide las entradas que nunca se me ocurrieron ni la lógica que le falta al código. Por eso, tener 100% de cobertura significa que cada línea se ejecutó al menos una vez, no que el código esté libre de bugs: la cobertura sirve para encontrar lo que todavía no he probado, no para demostrar que lo probado es correcto.

**¿Qué aprendí?**

Aprendí que una prueba en rojo no es un fracaso sino un hallazgo. Los dos primeros bugs de `calculadora` aparecieron porque me pregunté qué entrada rompería cada función: una lista de positivos para `minimo` y un número negativo para `raiz_cuadrada`. Esto cambió mi forma de probar: antes pensaba en comprobar que el código funciona con un caso normal, y ahora pienso primero en los casos límite (cero, negativos, listas vacías, el borde de cada tramo de descuento). También entendí por qué conviene hacer commit de la prueba en rojo antes de la corrección: el historial muestra primero el bug detectado y después el arreglo.

La estructura AAA hizo que cada prueba fuera corta, legible y fallara por un solo motivo, y `parametrize` me permitió cubrir varios casos inválidos sin repetir código. Medir la cobertura me mostró huecos reales: `calculadora` empezó en 52%, y entre las líneas sin cubrir estaba el camino normal de `promedio`. Por último, practiqué el flujo completo de trabajo de un DevOps: fork, clonar, entorno virtual, `.gitignore`, token de acceso, commits claros y `git push`. El error 403 al subir al repositorio equivocado me obligó a entender qué es `origin` y a cambiarlo para apuntar a mi fork.
