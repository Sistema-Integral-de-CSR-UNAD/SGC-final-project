# 🏢 Sistema Integral de Gestión — Software FJ
### Gestión de Clientes, Servicios y Reservas · POO · Python

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OOP](https://img.shields.io/badge/Paradigma-POO-green)
![DB](https://img.shields.io/badge/Base%20de%20datos-Ninguna-purple)

---

## 📋 Descripción

Sistema orientado a objetos que permite gestionar clientes, servicios y reservas para la empresa **Software FJ**, que ofrece reservas de salas, alquiler de equipos y asesorías especializadas.

Implementa rigurosamente abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones. No utiliza bases de datos; toda la gestión se realiza mediante objetos en memoria y un archivo de logs.

---

## 🚀 Características principales

- Clases abstractas (`Entidad`, `Servicio`) como base del sistema
- Tres servicios especializados con herencia y polimorfismo
- Clase `Reserva` con confirmación, cancelación y manejo de excepciones
- Métodos sobrecargados para cálculo de costos (con descuentos e impuestos)
- Excepciones personalizadas encadenadas
- Registro de eventos y errores en archivo `logs/sistema.log`
- 12 operaciones simuladas (casos válidos e inválidos)

---

## 📁 Estructura del proyecto
