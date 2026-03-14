import streamlit as st
import psutil

def measure_phi_m():

    mem = psutil.virtual_memory()

    return mem.percent / 100


class HierarchicalMemory:

    def store(self, key, value):

        st.session_state[key] = value

    def get(self, key):

        return st.session_state.get(key)


memory = HierarchicalMemory()
