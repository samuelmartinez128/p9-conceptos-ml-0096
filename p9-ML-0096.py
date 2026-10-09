import pandas as pd

datos8 = {
    'distancia_km': [5.3, 1.9, 3.6, 2.7, 4.9],
    'trafico_nivel': [3, 2, 1, 3, 2],
    'edad_repartidor': [33, 28, 40, 22, 35],
    'tiempo_entrega_min': [50, 17, 24, 30, 42]
}
df = pd.DataFrame(datos8)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))