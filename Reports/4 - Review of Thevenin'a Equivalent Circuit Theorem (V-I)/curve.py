import matplotlib.pyplot as plt

# - Data
V_L = [0.088, 0.257, 0.335, 0.415, 0.462, 0.540, 0.584, 0.650, 0.730]
I_L = [590, 441, 388, 332, 298, 243, 212, 164, 105.4]
# - Convert Current to Amperes
I_L = [i / 1000 for i in I_L]
# - Plot
plt.figure(figsize = (8, 6))
plt.plot(I_L, V_L, marker = 'o', linestyle = '-', color = 'blue')
plt.title('Load Voltage $V_L$ vs Load Current $I_L$')
plt.xlabel('Load Current $I_L$ (A)')
plt.ylabel('Load Voltage $V_L$ (V)')
plt.grid(True)
plt.tight_layout()
# - Save figure
plt.savefig("if 2.png", dpi = 300)
plt.show()
