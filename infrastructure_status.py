# infrastructure_status.py

class InfrastructureStatus:
    def __init__(self):
        self.data = {}

    def add_status(self, element, status):
        if element in self.data:
            self.data[element]['status'] = status
        else:
            self.data[element] = {'status': status}

    def get_status(self, element):
        return self.data.get(element, {}).get('status', 'Unknown')

    def update_status(self, element, new_status):
        if element in self.data:
            self.data[element]['status'] = new_status
        else:
            print(f"Element '{element}' not found.")

# Usage example:
infrastructure_status = InfrastructureStatus()
infrastructure_status.add_status('Road 1', 'Normal')
infrastructure_status.add_status('Bridge 2', 'Under Maintenance')

print(infrastructure_status.get_status('Road 1'))  # Output: Normal
print(infrastructure_status.get_status('Bridge 2'))  # Output: Under Maintenance

infrastructure_status.update_status('Road 1', 'Failed')
print(infrastructure_status.get_status('Road 1'))  # Output: Failed