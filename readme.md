# Gauss Law VPython Simulation

This project is a 3D visualization and numerical simulation of **Gauss's Law** using **VPython**.

It computes the electric flux through a spherical Gaussian surface enclosing two point charges and verifies Gauss's Law:

**Φ = Q<sub>enclosed</sub> / ε<sub>0</sub>**

---

## 🔬 Project Description

The simulation models two point charges located inside a spherical Gaussian surface.

A discretized Gaussian sphere is created using small surface elements. For each surface element:

* The electric field **E** is calculated due to both charges.
* The flux contribution **dΦ = E · n̂ dA** is computed.
* The total flux is obtained by summing all contributions.

The code also visualizes:

* The Gaussian surface
* Electric field vectors
* Regions of positive and negative flux using color mapping

---

## 🧮 Physics Background

Gauss's Law states:

**∮ E · dA = Q<sub>enclosed</sub> / ε<sub>0</sub>**

Where:

* **E** is the electric field
* **dA** is an outward surface element
* **Q<sub>enclosed</sub>** is the total charge inside the surface
* **ε<sub>0</sub>** is the permittivity of free space

This simulation numerically verifies Gauss's Law by comparing the calculated electric flux with the theoretical value **Q<sub>enclosed</sub> / ε<sub>0</sub>**.

---

## 🖥️ Requirements

* Python 3.x
* VPython

### Installation

```bash
pip install vpython

Install VPython using:
git clone https://github.com/mariamnabeh/electric-flux-simulation.git
cd electric-flux-simulation
python gauss_simulation.py




## 🙏 Credits

This project was inspired by the educational video:

**Gauss's Law Visualization and Simulation**
https://youtu.be/rQEBjzzYS7g

The video provided valuable insights into the visualization of electric flux and Gaussian surfaces using VPython.
Special thanks to the creator for the educational content and inspiration behind this project.




