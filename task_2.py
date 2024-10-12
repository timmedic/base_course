import math
import phys_consts as pc

h = 100
α = 45
β = 35

V = math.sqrt( (pc.g * h * math.pow(math.tan(β), 2)) / (2 * math.pow(math.cos(α), 2) * (1 - math.tan(β) * math.tan(α))) )
print(V)

T = 200
ε = 300

N = (2 / math.sqrt(math.pi)) * (pc.ℏ / math.pow(pc.k * T, 3 / 2)) * math.pow(pc.e, -1 * ε / (pc.k * T)) * math.pow(ε, T / 2)
print(N)