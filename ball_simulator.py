import matplotlib.pyplot as pyplot
import numpy as np
import math
from math import sqrt

## define constant
g = 9.81
num_data = 1000
x_pos = []
y_pos = []
V_x = []
V_y = []
a_x = []
a_y = []
F_x = []
F_y = []

print('enter in order (separated by space): ')
param = input('mass, dens_air, A_ref, Cd, Cl, X0, Y0, V0_x, V0_y, dur: \n').split()
print(param)
for i in range(0,10):
	param[i] = float(param[i])

mass = param[0]
dens_air = param[1]
A_ref = param[2]
Cd = param[3]
Cl = param[4]
X0 = param[5]
Y0 = param[6]
V0_x = param[7]
V0_y = param[8]
dur = param[9]
interval = dur / num_data


def calc_next(Vx, Vy, x, y):

	V = sqrt(Vx**2+Vy**2)
	b = math.atan2(Vy, Vx)
	b_deg = b*180/math.pi
	#print('V =', V, ' angle =', b)

	D = 0.5 * dens_air * V**2 * A_ref * Cd
	L = 0.5 * dens_air * V**2 * A_ref * Cl
	#print('D =', D, ' L=', L)

	Fx = - D * math.cos(b) - L * math.sin(b)
	Fy = - mass * g - D * math.sin(b) + L * math.cos(b)
	ax = Fx / mass
	ay = Fy / mass
	#print('Fx =', Fx, ' Fy =', Fy, ' ax =', ax, ' ay =', ay)

	Vx_nxt = Vx + interval * ax
	Vy_nxt = Vy + interval * ay
	x_nxt = x + interval * Vx
	y_nxt = y + interval * Vy

	if (y_nxt < 0):
		return 0, 0, 0, 0, 0, 0, 0, 0
	else:
		return Vx_nxt, Vy_nxt, x_nxt, y_nxt, Fx, Fy, ax, ay

def main():
	count = 0
	# mass = float(input('please enter the mass of the ball (in kg): '))
	# dens_air = float(input('please enter the density of the ball (in k/m^3): '))
	# A_ref = float(input('please enter the reference area of the ball (in m^2): '))
	# Cd = float(input('please enter the coeff of drag: '))
	# Cl = float(input('please enter the coeff of lift: '))

	# X0 = float(input('please enter the initial x position (m): '))
	# Y0 = float(input('please enter the initial y position (m) '))
	# V0_x = float(input('please enter the initial x velocity (m/s): '))
	# V0_y = float(input('please enter the initial y velocity (m/s): '))
	# dur = float(input('please enter the total time duration (second): '))

	# param = [mass, dens_air, A_ref, Cd, Cl, X0, Y0, V0_x, V0_y, dur]
	#global count

	print('your inputs are: ', param)

	Vx, Vy = V0_x, V0_y
	x, y = X0, Y0
	for i in range(0,num_data):
		count = count + 1
		Vx_temp, Vy_temp, x_temp, y_temp, Fx_temp, Fy_temp, ax_temp, ay_temp = calc_next(Vx, Vy, x, y)
		if (x_temp == 0 and y_temp == 0 and Vx_temp == 0 and Vy_temp == 0):
			count = count - 1
			break
		x_pos.append(x_temp)
		y_pos.append(y_temp)
		V_x.append(Vx_temp)
		V_y.append(Vy_temp)
		a_x.append(ax_temp)
		a_y.append(ay_temp)
		F_x.append(Fx_temp)
		F_y.append(Fy_temp)
		Vx, Vy, x, y = Vx_temp, Vy_temp, x_temp, y_temp
	print(count)
	t = np.arange(0., interval * count, interval)

	pyplot.figure(1)
	pyplot.subplot(2, 1, 1)
	pyplot.plot(x_pos, y_pos,'r--')
	pyplot.ylabel('y position (m)')
	pyplot.xlabel('x position (m)')
	pyplot.subplot(2, 1, 2)
	pyplot.plot(t, y_pos,'g--')
	pyplot.ylabel('y position (m)')
	pyplot.xlabel('time (sec)')

	pyplot.figure(2)
	pyplot.title('Time graphs')
	pyplot.subplot(3, 2, 1)
	pyplot.plot(t, V_x, 'b')
	pyplot.ylabel('X Velocity (m/s)')
	pyplot.grid(True)
	pyplot.subplot(3, 2, 2)
	pyplot.plot(t, V_y, 'b')
	pyplot.ylabel('Y Velocity (m/s)')
	pyplot.grid(True)

	pyplot.subplot(3, 2, 3)
	pyplot.plot(t, a_x, 'b')
	pyplot.ylabel('X Acceleration (m/s^2)')
	pyplot.grid(True)
	pyplot.subplot(3, 2, 4)
	pyplot.plot(t, a_y, 'b')
	pyplot.ylabel('Y Acceleration (m/s^2)')
	pyplot.grid(True)

	pyplot.subplot(3, 2, 5)
	pyplot.plot(t, F_x, 'b')
	pyplot.xlabel('Time (s)')
	pyplot.ylabel('Fx (N)')
	pyplot.grid(True)

	pyplot.subplot(3, 2, 6)
	pyplot.plot(t, F_y, 'b')
	pyplot.xlabel('Time (s)')
	pyplot.ylabel('Fy (N)')
	pyplot.grid(True)

	
	# fig, (ax1, ax2, ax3) = pyplot.subplots(3, 1)
	# pyplot.ylabel('Force (N)  Acceleration (m/s^2)  Velocity (m/s)')
	# pyplot.xlabel('time (sec)')
	# fig.suptitle('Time Graphs')
	# ax1.plot(t, V_x)
	# ax2.plot(t, a_x)
	# ax3.plot(t, F_x)

	
	print('graph done')
	print(t)
	pyplot.show()

if __name__ == '__main__':
	main()

