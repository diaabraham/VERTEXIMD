# feature_prioritization.py

class FeaturePrioritization:
    def __init__(self):
        self.features = {
            'Basic infrastructure status tracking': 1,
            'Simple cost projection model': 2,
            'Geographic visualization': 3,
            'Predictive analytics': 4,
            'Real-time monitoring': 5
        }

    def get_next_feature(self, priority):
        return next((feature for feature, value in sorted(self.features.items(), key=lambda item: item[1]) if
value == priority), None)

# Usage example:
feature_prioritization = FeaturePrioritization()
priority = 2
next_feature = feature_prioritization.get_next_feature(priority)
print(next_feature)  # Output: Simple cost projection model