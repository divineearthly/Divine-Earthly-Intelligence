
from .agriculture import AgricultureModule
from .climate_risk import ClimateRiskModule
from .disaster_prediction import DisasterPredictionModule

class DomainOrchestrator:
    def __init__(self):
        self.agri = AgricultureModule()
        self.climate = ClimateRiskModule()
        self.disaster = DisasterPredictionModule()

    def route_request(self, domain, **kwargs):
        if domain == 'agriculture':
            return self.agri.assess_crop_health(**kwargs)
        elif domain == 'climate':
            return self.climate.analyze_trends(**kwargs)
        elif domain == 'disaster':
            return self.disaster.identify_threats(**kwargs)
        else:
            return {'error': 'Unknown domain'}
