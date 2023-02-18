import tkinter as tk

window = tk.Tk()
window.title("Circular Motion Calculator")

radius_label = tk.Label(text="Radius (m):")
radius_label.pack()
radius_field = tk.Entry()
radius_field.pack()

velocity_label = tk.Label(text="Velocity (m/s):")
velocity_label.pack()
velocity_field = tk.Entry()
velocity_field.pack()

angular_velocity_label = tk.Label(text="Angular velocity (rad/s):")
angular_velocity_label.pack()
angular_velocity_field = tk.Entry()
angular_velocity_field.pack()

time_label = tk.Label(text="Time (s):")
time_label.pack()
time_field = tk.Entry()
time_field.pack()

output_label = tk.Label(text="Result:")
output_label.pack()

output_field = tk.Label(text="")
output_field.pack()

def calculate():
    radius = float(radius_field.get())
    velocity = float(velocity_field.get())
    angular_velocity = float(angular_velocity_field.get())
    time = float(time_field.get())

    if radius == 0:
        radius = velocity / angular_velocity
    elif velocity == 0:
        velocity = radius * angular_velocity
    elif angular_velocity == 0:
        angular_velocity = velocity / radius
    elif time == 0:
        time = 2 * 3.14159 * radius / velocity

    output_field.config(text=f"Radius: {radius:.2f} m\nVelocity: {velocity:.2f} m/s\nAngular velocity: {angular_velocity:.2f} rad/s\nTime: {time:.2f} s")

calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.pack()

window.mainloop()
