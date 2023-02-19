microwawe_power_kW = 1.3
use_time_h = 2
price_per_kWh = 0.95
broj_dana = 30
consumption = microwawe_power_kW * use_time_h * price_per_kWh * broj_dana
consumption_pdv = microwawe_power_kW * use_time_h * (price_per_kWh * 1.25) * broj_dana
print(f"Trošak uporabe mikrovalne pećnice tijekom 30 dana iznosi: {consumption} kn bez PDV-a, odnosno: {consumption_pdv} kn s PDV-om.")

# ZADATAK: Obračunska jedinica za potrošnja električne energije je kilovat sat i označava se 1 kWh.
# Predstavlja umnožak snage trošila/uređaja izražene u kilovatima (kW)
# i vremena koje se taj uređaj koristi izraženog u satima (h). kW * h
# Ako je snaga mikrovalne pećnice 1.3 kW, a cijena el. energije za 1 kWh je 0.95 kn,
# koliko kuna, mjesečno, košta uporaba mikrovalne pećnice, ako se koristi 2 sata dnevno?
# Zbog jednostavnosti zaokružimo svaki mjesec na 30 dana
# Ispišite trošak bez i s uračunatim PDV-om.  