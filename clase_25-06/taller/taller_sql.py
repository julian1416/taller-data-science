#Estudiante: Julián David Rojas Román
import sqlite3
import pandas as pd

def ejecutar_taller():
    # PARTE 1: Configuración de Base de Datos y Carga
    db_name = "ejercicios.db"
    conn = sqlite3.connect(db_name)
    
    try:
        # Carga del dataset y creación de tabla manual (vía pandas para eficiencia)
        df = pd.read_csv('FuelConsumptionCo2.csv')
        df.to_sql('fuel_consumption', conn, if_exists='replace', index=False)
        print(f"Base de datos '{db_name}' creada y dataset cargado.\n")

        # PARTE 2: Requerimientos Analíticos
        
        def query(sql, desc):
            print(f">>> {desc}")
            print(pd.read_sql_query(sql, conn))
            print("-" * 50)

        # 1. Verificación de importación exitosa
        query("SELECT * FROM fuel_consumption", "Verificación de registros")

        # 2. Optimización de memoria (Primeras 15 filas)
        query("SELECT * FROM fuel_consumption LIMIT 15", "Optimización con LIMIT 15")

        # 3. Listado limpio de fabricantes (DISTINCT)
        query("SELECT DISTINCT MAKE FROM fuel_consumption ORDER BY MAKE", "Marcas disponibles")

        # 4. Análisis de alto cilindraje (> 3.0L)
        query("SELECT MAKE, MODEL, ENGINESIZE FROM fuel_consumption WHERE ENGINESIZE > 3.0", 
              "Motores > 3.0 Litros")

        # 5. Filtrado por año analizado (Basado en el dataset 2014)
        query("SELECT * FROM fuel_consumption WHERE MODELYEAR = 2014", "Vehículos del año analizado")

        # 6. Conteo por marca específica (FORD)
        query("SELECT COUNT(*) AS total_ford FROM fuel_consumption WHERE MAKE = 'FORD'", 
              "Conteo de vehículos FORD")

        # 7. Filtros de consumo extremo (Bajo < 8 o Alto > 20 en ciudad)
        query("""
            SELECT MAKE, MODEL, FUELCONSUMPTION_CITY 
            FROM fuel_consumption 
            WHERE FUELCONSUMPTION_CITY < 8.0 OR FUELCONSUMPTION_CITY > 20.0
        """, "Consumo en ciudad (Inusualmente bajo o alto)")

    except Exception as e:
        print(f"Error en el proceso: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    ejecutar_taller()