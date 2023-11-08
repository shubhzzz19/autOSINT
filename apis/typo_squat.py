# from ..gui.main import e_Domain
import subprocess


def run_dnstwist(e_Domain):
    try:
        result = subprocess.check_output(
            ["dnstwist", e_Domain], stderr=subprocess.STDOUT, text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        return e.output
