# US-002 — Pruebas funcionales y de rendimiento

## 1. Identificación

- **Historia de usuario:** GC03-102 — US-002: Consultar vehículos disponibles.
- **Subtarea:** GC03-41 — T-011: Ejecutar/verificar pruebas funcionales y respuesta inferior a 2 segundos.
- **Responsable:** Borja Gómez Castaño.
- **Fecha:** 05/11/2026.
- **Estado:** Pruebas automatizadas superadas.

## 2. Objetivo

Verificar que el sistema consulta correctamente los vehículos disponibles para un rango de fechas determinado, excluyendo los vehículos que no puedan reservarse.

También se comprueba que el tiempo de ejecución de la consulta es inferior a 2 segundos en el entorno local de pruebas.

## 3. Componentes utilizados

Las pruebas se han realizado sobre los siguientes archivos:

- `disponibilidad.py`: consulta de vehículos disponibles y comprobación de reservas incompatibles.
- `fechas.py`: validación del rango de fechas.
- `tests/test_consulta_disponibilidad_rendimiento.py`: pruebas automatizadas realizadas.

Se ha utilizado Python y el módulo `unittest`, sin modificar la implementación existente.

## 4. Pruebas funcionales

| Caso | Descripción | Resultado |
|---|---|---|
| PT-01 | Búsqueda sin vehículos | Correcto |
| PT-02 | Vehículo disponible sin reservas | Correcto |
| PT-03 | Exclusión por reserva activa solapada | Correcto |
| PT-04 | Exclusión de vehículos inactivos o en mantenimiento | Correcto |
| PT-05 | Reserva fuera del rango consultado | Correcto |
| PT-06 | Reserva cancelada que no bloquea la disponibilidad | Correcto |
| PT-07 | Reserva correspondiente a otro vehículo | Correcto |
| PT-08 | Rechazo de un rango de fechas inválido | Correcto |
| PT-09 | Consulta con límite de respuesta inferior a 2 segundos | Correcto |

### 4.1. Consulta sin vehículos

Se realiza una búsqueda con una lista vacía de vehículos.

**Resultado esperado:** devolver una lista vacía.

**Resultado obtenido:** correcto.

### 4.2. Vehículo disponible

Se consulta un vehículo operativo sin reservas.

**Resultado esperado:** incluir el vehículo en los resultados.

**Resultado obtenido:** correcto.

### 4.3. Reserva incompatible

Se introduce una reserva activa cuyas fechas coinciden parcialmente con el periodo solicitado.

**Resultado esperado:** excluir el vehículo de los resultados.

**Resultado obtenido:** correcto.

### 4.4. Vehículos no disponibles

Se comprueban los estados `inactivo` y `mantenimiento`.

**Resultado esperado:** excluir el vehículo en ambos casos.

**Resultado obtenido:** correcto.

### 4.5. Reservas compatibles

Se comprueba el comportamiento cuando la reserva está fuera del periodo solicitado, está cancelada o pertenece a otro vehículo.

**Resultado esperado:** mantener el vehículo entre los disponibles.

**Resultado obtenido:** correcto en los tres casos.

### 4.6. Validación de fechas

Se realiza una consulta con la fecha de fin anterior a la de inicio.

**Resultado esperado:** lanzar una excepción `ValueError`.

**Resultado obtenido:** correcto.

## 5. Prueba de rendimiento

Se prepara un escenario de prueba compuesto por:

- 300 vehículos ficticios.
- 100 reservas activas.
- Un rango de fechas del 10/11/2026 al 14/11/2026.

Los vehículos se distribuyen en tres grupos: vehículos inactivos, vehículos con reservas solapadas y vehículos disponibles.

Se utiliza `perf_counter()` para medir el tiempo de ejecución de la función `consultar_vehiculos_disponibles()`.

Se verifica que:

- La consulta devuelve exactamente 100 vehículos disponibles.
- Los vehículos incluidos corresponden al grupo esperado.
- El tiempo de ejecución es inferior a 2 segundos.

**Resultado:** prueba superada.

## 6. Ejecución de las pruebas

Comando utilizado desde la raíz del proyecto:

```powershell
python -m unittest discover -s tests -p "test_consulta_disponibilidad_rendimiento.py" -v
```

Resultado obtenido:

```text
Ran 9 tests in 0.004s

OK
```

**Resumen:**

| Concepto | Resultado |
|---|---|
| Pruebas ejecutadas | 9 |
| Pruebas superadas | 9 |
| Fallos | 0 |
| Errores | 0 |
| Tiempo total del conjunto de pruebas | 0,004 segundos |
| Resultado global | OK |

## 7. Limitaciones

Las pruebas se han realizado directamente sobre funciones Python utilizando datos ficticios.

La comprobación de rendimiento mide una ejecución local de la función de consulta. No representa el tiempo completo de respuesta de una interfaz web ni incluye comunicación con una base de datos.

El tiempo de 0,004 segundos corresponde al conjunto de las nueve pruebas, no exclusivamente a la consulta de rendimiento.

No se han realizado pruebas de carga con solicitudes concurrentes ni pruebas de extremo a extremo.

## 8. Conclusión

Se han ejecutado nueve pruebas automatizadas, todas con resultado correcto.

Se ha comprobado que la consulta devuelve los vehículos adecuados al rango solicitado, excluye reservas activas incompatibles y vehículos no disponibles, y permite consultar vehículos con reservas que no afectan al periodo seleccionado.

La prueba de rendimiento también ha superado el límite de 2 segundos en el escenario local definido.

Por tanto, se consideran superadas las comprobaciones funcionales y de rendimiento realizadas para GC03-41, dentro del alcance del servicio y del entorno de pruebas utilizado.