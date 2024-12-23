# visualization_dashboard.py

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VisualizationDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Infrastructure Status Tracker")

        # Create figure and axis
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax1 = self.figure.add_subplot(211)
        self.ax2 = self.figure.add_subplot(212)

        # Add canvas to the GUI
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_status(self, element, status):
        self.ax1.clear()
        self.ax2.clear()

        # Plot infrastructure status
        self.ax1.plot([status])

        # Plot maintenance cost prediction
        x = [10, 20, 30]
        y = [100, 200, 300]
        self.ax2.plot(x, y)

    def run(self):
        self.root.mainloop()

# Usage example:
visualization_dashboard = VisualizationDashboard()
visualization_dashboard.update_status('Road 1', 'Normal')
visualization_dashboard.run()