power_kW = float(input("Upiši snagu uređaja: "))
use_time_h = 2
price_per_kWh = float(input("Upiši cijenu električne energije po kWh: "))
broj_dana = 30
consumption = power_kW * use_time_h * price_per_kWh * broj_dana
consumption_pdv = power_kW * use_time_h * (price_per_kWh * 1.25) * broj_dana
print(f"Trošak uporabe uređaja tijekom 30 dana iznosi: {round(consumption, 2)} kn bez PDV-a, odnosno: {round(consumption_pdv, 2)} kn s PDV-om.")
