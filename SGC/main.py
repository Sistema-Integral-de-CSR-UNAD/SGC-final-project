from utilidades.logger import configurar_logger
from modelos.cliente import Cliente
from modelos.servicio import AlquilerEquipo, ReservaAsesoria
from modelos.reserva import Reserva
from excepciones.personalizadas import ReservaInvalidaError

log = configurar_logger()

def ejecutar():
    """Ejecutar las 10 simulaciones requeridas para Software FJ."""
    print ("---- INICIANDO SIMULACIONES SOFTWARE FJ ----\n")
    log.info("Inicio de sesión de pruebas.") #Registro de evento normal

    # --- SIMULACION CLIENTES ---

    #1. Creación de cliente (Exitoso)
    try:
        c1 = Cliente("101", "Emmanuel Cardenas", "emmanuel@unad.edu.co")
        print(f"Sim 1: Cliente {c1.nombre} creado.")
        log.info("Simulacion 1 exitosa.")
    except Exception as e:
        log.error(f"Error Sim 1: {e}")

    #2. Validar correo (Fallo esperado)
    try:
        print("Sim 2: Probando correo inválido...")
        c1.correo_electronico = "correo_sin_arroba"
    except ValueError as e:
        print(f" Capturado: {e}")
        log.warning(f"Simulacion 2 detectó error: {e}")

    # --- SIMULACION SERVICIOS ---

    #3. Creación de servicios (Exitoso)
    s1 = AlquilerEquipo("S01", "Laptop Pro", 50000)
    s2 = ReservaAsesoria("S02", "Asesoría en Sistemas", 80000)
    print("Sim 3: Servicio de alquiler y asesoría creados.")
    log.info("Simulacion 3: Servicios instanciados.")

    # --- SIMULACION RESERVAS ---

    #4. Procesar Reserva alquiler (Exitoso)
    try:
        r1 = Reserva(c1, s1, 3) #3 días de alquiler
        print(f"Sim 4: {r1.procesar()}")
        log.info("Simulacion 4 exitosa.")
    except Exception as e:
        log.error(f"Error Sim 4: {e}")

    #5. Procesar Reserva con duración inválida (Fallo esperado)
    try:
        print("Sim 5: Probando reserva con duración inválida...")
        r2 = Reserva(c1, s1, 0)
    except ReservaInvalidaError as e:
        print(f" Capturado: {e}")
        log.warning(f"Simulacion 5 detectó error: {e}")

    #6. Procesar Reserva asesoría (Exitoso - Polimorfismo)
    try:
        r3 = Reserva(c1, s2, 2) #2 horas de asesoría
        print(f"Sim 6: {r3.procesar()}")
        log.info("Simulacion 6 exitosa.")
    except Exception as e:
        log.error(f"Error Sim 6: {e}")

    #7. Simulación de erros génerico (Operación que podría generar un fallo)
    try:
        print("Sim 7: Ejecutando operación con objeto no definido...")
        #Intentamos procesar algo que no exiiste para forzar al log.error
        reserva_fantasma.procesar()
    except Exception as e:
        log.error(f"Error detectado en Sim 7: {e}")
        print("Sim 7: Ocurrió un error capturado (NameError), el programa continúa funcionando.")

    #8. Creación de segundo cliente (Exitoso)
    try:
        c2 = Cliente("102", "Sofia Martinez", "sofia@unad.edu.co")
        print(f"Sim 8: Cliente {c2.nombre} creado.")
        log.info("Simulacion 8 exitosa.")
    except Exception as e:
        log.error(f"Error Sim 8: {e}")

    #9. Reserva para segundo cliente (Exitoso)
    try:
        r4 = Reserva(c2, s1, 5) #5 días de alquiler
        print(f"Sim 9: {r4.procesar()}")
        log.info("Simulacion 9 exitosa.")
    except Exception as e:
        log.error(f"Error Sim 9: {e}")

    #10. Bloque Final (Prueba de estabilidad)
    try:
        print("Sim 10: Total de clientes en esta sesión: 2")
        log.info("Simulacion 10: Sesión finalizada con estabilidad.")
    finally:
        print("\n---- SIMULACIONES COMPLETADAS ----")

if __name__ == "__main__":
    ejecutar()
