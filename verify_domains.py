
import sys
import os
sys.path.append(os.getcwd())
from modules.orchestrator import DomainOrchestrator

orch = DomainOrchestrator()

print('--- Domain Module Verification ---')
res_agri = orch.route_request('agriculture', soil_moisture=15, temperature=38, humidity=12)
print(f'Agriculture (Extreme): {res_agri}')

res_climate = orch.route_request('climate', carbon_levels=420, sea_level_rise=3.5, avg_temp=22)
print(f'Climate (Normal): {res_climate}')

res_disaster = orch.route_request('disaster', sensor_type='flood', value=0.8, temperature=25, humidity=85)
print(f'Disaster (Normal): {res_disaster}')
