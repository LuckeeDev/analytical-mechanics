import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = 1
b = 1

# Function to update the animation frames
def update(frame):
    global x, y, vx, vy
    # Update position on the circle
    x = a * np.cos(np.radians(frame))
    y = b * np.sin(np.radians(frame))

    # Update velocity components (you can modify this based on your desired motion)
    vx = - a * np.sin(np.radians(frame))
    vy = b * np.cos(np.radians(frame))

    # Update the position of the point with a trace
    trace_x.append(x)
    trace_y.append(y)
    trace.set_data(trace_x, trace_y)

    # Update the position of the point
    point.set_data([x], [y])

    # Update the velocity graph with a trace
    vel_trace_x.append(vx)
    vel_trace_y.append(vy)
    vel_trace.set_data(vel_trace_x, vel_trace_y)

    # Update the velocity graph
    vel_point.set_data([vx], [vy])

    # Update the arrows
    arrow_pos.set_UVC(x, y)
    arrow_vel.set_offsets([x, y])
    arrow_vel.set_UVC(vx, vy)

    # Update the red arrow from the center to the red dot in the second graph
    center_arrow.set_UVC(vx, vy)

    return point, trace, vel_point, vel_trace, arrow_pos, arrow_vel, center_arrow

# Initialize variables
x, y = 1, 0  # Initial position on the circle
vx, vy = 0, 1  # Initial velocity components

# Set up the figure and axis for the animation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.set_title('Posizione nello spazio')

ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.grid(True)

ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect('equal')
ax2.set_title('Spazio delle velocità')

ax2.set_xlabel('$v_x$')
ax2.set_ylabel('$v_y$')
ax2.grid(True)

# Create the point on the circle with a trace
trace_x, trace_y = [x], [y]
trace, = ax1.plot(trace_x, trace_y, 'b-', alpha=0.3)

point, = ax1.plot(x, y, 'bo', markersize=4)  # Reduced size of the blue dot

# Create the velocity point with a trace
vel_trace_x, vel_trace_y = [vx], [vy]
vel_trace, = ax2.plot(vel_trace_x, vel_trace_y, 'r-', alpha=0.3)

vel_point, = ax2.plot([vx], [vy], 'ro', markersize=4)  # Reduced size of the red dot

# Create arrow objects for position and velocity
arrow_pos = ax1.quiver(0, 0, x, y, color='blue', angles='xy', scale_units='xy', scale=1, width=0.005, headwidth=3, headlength=4, label='Posizione')
arrow_vel = ax1.quiver(x, y, vx, vy, color='red', angles='xy', scale_units='xy', scale=1, width=0.005, headwidth=3, headlength=4, label='Velocità')

# Create a red arrow from the center to the red dot in the second graph
center_arrow = ax2.quiver(0, 0, vx, vy, color='red', angles='xy', scale_units='xy', scale=1, width=0.005, headwidth=3, headlength=4, label='Velocità')

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=10, blit=True)

# Add legends
ax1.legend()
ax2.legend()

plt.show()
