import streamlit as st
from core.memory_phi import measure_phi_m
from core.dissipation_phi import measure_phi_d
from core.coherence_phi import coherence

class TTUEngine:
    """Moteur de stabilité basé sur le Théorème de Minimalité Dimensionnelle (T1)"""
    
    @staticmethod
    def get_state_vector():
        phi_m = measure_phi_m() # Mémoire
        phi_d = measure_phi_d() # CPU/Dissipation
        phi_c = coherence.phi() # Utilité/Cohérence
        return phi_m, phi_c, phi_d

    @staticmethod
    def compute_flow():
        """Calcule le flux informationnel d'après dΦ/dt"""
        m, c, d = TTUEngine.get_state_vector()
        # Loi de Fast-Charge : I_cmd = I_max(0.6 + 0.3Φc - 0.5Φd)
        throttle = 0.6 + (0.3 * c) - (0.5 * d)
        return max(0.1, min(1.0, throttle))

    @staticmethod
    def stabilize():
        """Force l'attracteur de Morse-Smale pour éviter la mise en veille"""
        phi_m, phi_c, phi_d = TTUEngine.get_state_vector()
        # Inégalité de l'Annexe B : Stabilité si λMλCλD > κ
        if (phi_m * phi_c * phi_d) < 0.001:
            # Injection d'un 'Quantum de Cohérence' pour réveiller le système
            coherence.record(useful=True)
