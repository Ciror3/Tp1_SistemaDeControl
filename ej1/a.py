import control as ctrl
import matplotlib.pyplot as plt

# 1. Tu planta original a lazo abierto (Parte A)
G = ctrl.tf([0.25], [0.003, 0.0515, 0.2, 0]) 

# 2. Tu Controlador PI de prueba (Asumimos Kc = 1 para dibujar el Locus)
# Numerador: s + 0.1 -> [1, 0.1]
# Denominador: s -> [1, 0]
C = ctrl.tf([1, 0.1], [1, 0])

# 3. La nueva función a Lazo Abierto (Planta + Controlador)
G_nueva_abierta = C * G

# 4. Dibujamos el Root Locus
plt.figure(figsize=(10, 8))
ctrl.root_locus(G_nueva_abierta)
plt.title("Root Locus del Sistema con Controlador PI")
plt.grid(True)
plt.show()