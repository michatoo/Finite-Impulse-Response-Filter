"""
Michael Toon
9/9/24

This program was originally part of the final exam for a course I took about Advanced
Programming Applications. I eventually noticed that it was generally applicable to some
other courses, so I added and modified it so I could use it for other classes.

"""

from numpy import pi, linspace, exp, sin, cos
from matplotlib.pyplot import plot, xlabel, ylabel, show

print('\nThis is a Finite Impulse Response (FIR) filter that will use the Fourier Transform Design Technique.')
fs = float(input('\nEnter the sampling frequency (fs): '))

proceed = False

while proceed == False:
    
    print('\n1. Lowpass')
    print('\n2. Highpass')
    print('\n3. Bandpass')
    print('\n4. Bandstop')
    
    filter_choice = int(input('\nPlease choose the corresponding number for the filter you want to use: '))

    if filter_choice == 1:
        fc = float(input("\nEnter the cutoff frequency, fc: "))
        omega_c = (2*pi*fc) / fs
        
        proceed = True
    
    elif filter_choice == 2:
        fc = float(input("\nEnter the cutoff frequency, fc: "))
        omega_c = (2*pi*fc) / fs 
        
        proceed = True
    
    elif filter_choice == 3:
        fl = float(input("\nEnter the lower cutoff frequency, fl: "))
        fh = float(input("\nEnter the upper cutoff frequency, fh: "))
        omega_h = (2*pi*fh) / fs
        omega_l = (2*pi*fl) / fs
        
        proceed = True
    
    elif filter_choice == 4:
        fl = float(input("\nEnter the lower cutoff frequency, fl: "))
        fh = float(input("\nEnter the upper cutoff frequency, fh: "))
        omega_h = (2*pi*fh) / fs
        omega_l = (2*pi*fl) / fs
        
        proceed = True
    
    else:
        print('\nYou have entered an invalid option. Please try again.')


proceed = False
while proceed == False:
    N = int(input("\nEnter the length of the filter, N. This value of N MUST be odd: "))
    if (N%2) == 0:
        print('\nYou have entered an invalid option. Please try again.')
    else:
        proceed = True

M = int((N-1) / 2)
b = []
h = []

if filter_choice == 1:
    for i in range((2*M+1)):
        m_coeffs = -M + i
        b.append(m_coeffs)
        h_values = sin(omega_c * m_coeffs) / (m_coeffs * pi)
        if m_coeffs == 0:
            h_values = omega_c / pi
        h.append(h_values)
        
elif filter_choice == 2:
    for i in range((2*M+1)):
        m_coeffs = -M + i
        b.append(m_coeffs)
        h_values = -1 * sin(omega_c * m_coeffs) / (m_coeffs * pi)
        if m_coeffs == 0:
            h_values = (pi - omega_c) / pi
        h.append(h_values)
        
elif filter_choice == 3:
    for i in range((2*M+1)):
        m_coeffs = -M + i
        b.append(m_coeffs)
        h_values = (sin(omega_h * m_coeffs) / (m_coeffs * pi)) - (sin(omega_l * m_coeffs) / (m_coeffs * pi))
        if m_coeffs == 0:
            h_values = (omega_h - omega_l) / pi
        h.append(h_values)
        
elif filter_choice == 4:
    for i in range((2*M+1)):
        m_coeffs = -M + i
        b.append(m_coeffs)
        h_values = -1 * (sin(omega_h * m_coeffs) / (m_coeffs * pi)) + (sin(omega_l * m_coeffs) / (m_coeffs * pi))
        if m_coeffs == 0:
            h_values = (pi - omega_h + omega_l) / pi
        h.append(h_values)

omega_range = linspace(0, pi, 1000)
z = []
for i in range(len(omega_range)):
    z_outputs = exp(omega_range*1j)
    z.append(z_outputs[i])

H = []

for i in range(len(z)):
    frequency_response = 0
    for j in range(len(b)):
        frequency_response += h[j]*z[i]**(-1*j)
    frequency_response = abs(frequency_response)
    H.append(frequency_response)

x = linspace(0, fs/2, 1000)

plot(x, H)
xlabel('Hz')
ylabel('Magnitude Response of the Original Filter')
show()
    
print('\n1. Triangular (Bartlett) window')
print('\n2. Hanning window')
print('\n3. Hamming window')
print('\n4. Blackman window')

w = []
h_new = []

window_function = int(input('\nSelect a window function from the choices above: '))

if window_function == 1:
    for i in range(len(b)):
        w_values = 1 - (abs(b[i])/M)
        w.append(w_values)
    
elif window_function == 2:
    for i in range(len(b)):
        w_values = 0.5 + 0.5*cos(b[i] * pi / M)
        w.append(w_values)
    
elif window_function == 3:  
    for i in range(len(b)):
        w_values = 0.54 + 0.46*cos(b[i] * pi / M)
        w.append(w_values)
    
elif window_function == 4:   
    for i in range(len(b)):
        w_values = 0.42 + 0.5*cos(b[i] * pi / M) + 0.08*sin(2* b[i] * pi / M)
        w.append(w_values)

for i in range(len(h)):
    h_values = h[i] * w[i]
    h_new.append(h_values)
    
H_new = []
    
for i in range(len(z)):
    frequency_response = 0
    for j in range(len(b)):
        frequency_response += h_new[j]*z[i]**(-1*j)
    frequency_response = abs(frequency_response)
    H_new.append(frequency_response)
    
plot(x, H_new)
xlabel('Hz')
ylabel('Magnitude Response of the Window-Treated Filter')
show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

