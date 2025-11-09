import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import gaussian_filter

# Style settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 1. FIGURE 2: Phase Map of Life-Threshold Region
print("Creating Figure 2...")
K0_range = np.linspace(0.1, 2.0, 50)
alpha_range = np.linspace(0.01, 1.0, 50)
K0_grid, alpha_grid = np.meshgrid(K0_range, alpha_range)

# Model function for mean coherence (⟨c⟩) (Synthetic)
# High K0 and alpha produce high coherence.
c_mean = np.minimum(1.0, 0.2 + 0.8 * (K0_grid / 2.0) * (alpha_grid / 1.0)**1.5)
c_mean = gaussian_filter(c_mean, sigma=1.2) # Smoothing

# Threshold contours for (T=0.2 and T=0.3)
# As temperature increases, higher K0 and alpha are needed to achieve the same coherence.
threshold_T02 = 0.15 + 0.5 * (1 - alpha_grid) * (1 - K0_grid/2.0)
threshold_T03 = 0.25 + 0.6 * (1 - alpha_grid) * (1 - K0_grid/2.0)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
im = ax.contourf(K0_grid, alpha_grid, c_mean, levels=15, cmap='hot_r', alpha=0.8)
contour_T02 = ax.contour(K0_grid, alpha_grid, threshold_T02, levels=[0.35], colors='white', linewidths=2)
contour_T03 = ax.contour(K0_grid, alpha_grid, threshold_T03, levels=[0.35], colors='blue', linestyles='dashed', linewidths=2)

ax.clabel(contour_T02, inline=True, fontsize=10, fmt='T=0.2')
ax.clabel(contour_T03, inline=True, fontsize=10, fmt='T=0.3')

ax.set_xlabel('Coupling Strength (K₀)', fontsize=12)
ax.set_ylabel('Resonance Sensitivity (α)', fontsize=12)
ax.set_title('Phase Map of Life-Threshold Region', fontsize=14)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Mean Coherence (⟨c⟩)', rotation=270, labelpad=15)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figure_2_phase_map.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. FIGURE 3: Energy and Entropy Evolution
print("Creating Figure 3...")
time = np.linspace(0, 100, 500)
# Energy: Increases initially, then balances with oscillations.
E_total = 12.3 / (1 + np.exp(-0.1*(time-30))) + 0.5 * np.sin(0.3*time) * np.exp(-0.02*time)
# Entropy: Inversely correlated with energy, decreases rapidly initially, then slows down.
S = 45.5 - 35 / (1 + np.exp(-0.1*(time-25))) + 2 * np.sin(0.25*time + 0.5) * np.exp(-0.015*time)

fig, ax1 = plt.subplots(figsize=(9, 5))

color = 'tab:red'
ax1.set_xlabel('Time (Arbitrary Units)', fontsize=12)
ax1.set_ylabel('Total Energy (E_total)', color=color, fontsize=12)
ax1.plot(time, E_total, color=color, linewidth=2, label='Energy')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(bottom=0)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Entropy (S)', color=color, fontsize=12)
ax2.plot(time, S, color=color, linestyle='--', linewidth=2, label='Entropy')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(top=60)

plt.title('Energy and Entropy Evolution', fontsize=14)
fig.tight_layout()
plt.savefig('figure_3_energy_entropy.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. FIGURE 4: Multi-Scale Resonance Hierarchy
print("Creating Figure 4...")
fig, ax = plt.subplots(1, 1, figsize=(9, 7))

# Generate random positions and sizes to mimic hierarchical structure
np.random.seed(42) # For reproducibility

# Micro-scale islands (Small, numerous)
n_micro = 50
x_micro = np.random.rand(n_micro)
y_micro = np.random.rand(n_micro)
size_micro = np.random.uniform(20, 60, n_micro)
color_micro = np.linspace(0.3, 0.6, n_micro) # From light blue to green

# Meso-scale structures (Medium size, fewer)
n_mezo = 15
x_mezo = np.random.rand(n_mezo) * 0.7 + 0.15
y_mezo = np.random.rand(n_mezo) * 0.7 + 0.15
size_mezo = np.random.uniform(80, 200, n_mezo)
color_mezo = np.linspace(0.5, 0.8, n_mezo) # From green to orange

# Macro-scale structures (Large, few)
n_macro = 5
x_macro = np.random.rand(n_macro) * 0.5 + 0.25
y_macro = np.random.rand(n_macro) * 0.5 + 0.25
size_macro = np.random.uniform(250, 400, n_macro)
color_macro = np.linspace(0.7, 0.9, n_macro) # From orange to red

# Draw all circles
scatter_micro = ax.scatter(x_micro, y_micro, s=size_micro, c=color_micro, cmap='viridis', alpha=0.7, edgecolors='darkblue', linewidth=0.5)
scatter_mezo = ax.scatter(x_mezo, y_mezo, s=size_mezo, c=color_mezo, cmap='viridis', alpha=0.7, edgecolors='darkgreen', linewidth=0.8)
scatter_macro = ax.scatter(x_macro, y_macro, s=size_macro, c=color_macro, cmap='viridis', alpha=0.7, edgecolors='darkred', linewidth=1.0)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
plt.title('Multi-Scale Resonance Hierarchy', fontsize=16, pad=20)

# Add text boxes for explanation
ax.text(0.02, 0.98, 'Micro', transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
ax.text(0.02, 0.90, 'Meso', transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
ax.text(0.02, 0.82, 'Macro', transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='salmon', alpha=0.7))

plt.tight_layout()
plt.savefig('figure_4_hierarchy.png', dpi=300, bbox_inches='tight')
plt.show()

print("All figures created successfully!")