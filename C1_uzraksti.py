# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā, kura nosaukums sākas ar līmeņa nosaukumu. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                     


import sys
if len(sys.argv) < 2:
    print("Nezinu ko man te uzrakstit, uzraksti vairak neka viekrasi faila nosaukumu, piemeram: python C1_uzraksti.py (WARNING vai INFO vai ERROR")
    sys.exit()
limenis = sys.argv[1]
skaits = 0
atrastas_rindas = []
with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        if limenis in rinda:
            skaits += 1
            atrastas_rindas.append(rinda)
print(f"Žurnala atrastas {skaits} rindas ar limeni {limenis}")
with open(f"{limenis}_izvade.txt", "w", encoding="utf-8") as f_out:
    for rinda in atrastas_rindas:
        f_out.write(rinda)
print(f"Rindas saglabatas in file {limenis}_izvade.txt")
