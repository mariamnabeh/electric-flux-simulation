# Gauss Law VPython Simulation

This project is a 3D visualization and numerical simulation of **Gauss’s Law** using **VPython**.  
It computes the electric flux through a spherical Gaussian surface enclosing two point charges and verifies Gauss’s law:

Φ = Q_enclosed / ε₀
---

## 🔬 Project Description

The simulation models two point charges located inside a spherical surface.  
A discretized Gaussian sphere is created using small surface elements. For each surface element:

- The electric field **E** is calculated due to both charges
- The flux contribution \( d\Phi = \vec{E} \cdot \hat{n} \, dA \) is computed
- The total flux is obtained by summing all contributions

The code also visualizes:
- The Gaussian surface
- Electric field vectors
- Regions of positive and negative flux using color mapping

---

## 🧮 Physics Background

Gauss’s Law states:

\[
\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enclosed}}}{\varepsilon_0}
\]

Where:
- \( \vec{E} \) is the electric field
- \( d\vec{A} \) is an outward surface element
- \( Q_{\text{enclosed}} \) is the total charge inside the surface
- \( \varepsilon_0 \) is the permittivity of free space

This simulation numerically verifies this equation.

---

## 🖥️ Requirements

- Python 3.x  
- VPython  

Install VPython using:
git clone https://github.com/mariamnabeh/electric-flux-simulation.git




## 🙏 Credits

This project was inspired by the educational video:

**Gauss's Law Visualization and Simulation**
https://youtu.be/rQEBjzzYS7g

The video provided valuable insights into the visualization of electric flux and Gaussian surfaces using VPython.
Special thanks to the creator for the educational content and inspiration behind this project.



python gauss_simulation.py

```bash
pip install vpython

