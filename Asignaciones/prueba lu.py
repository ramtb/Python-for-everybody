from vpython import*

ventana = graph()
ventana1 = canvas (range=15)
puntos = gcurve(color=color.blue)

x = 10.0
v = 0.0
t = 0.0

m = 1.0
k = 0.3
dt = 0.1

E = sphere(color = color.red, radius = 1.0, pos = vec(x,0,0))
R = helix(pos=vec(-13,0,0),rad = 0.5,axis = vec(x+13,0,0),colis = 15)

puntos.plot(pos = (x,v))

while True:
    v = v+(-k/m*x-0.0*v)*dt
    x  = x+v*dt
    t = t+dt
    puntos.plot(pos = (x,v))
    E.pos = vec(x,0,0)
    R.axis = vec(x+13,0,0)
    sleep(0.01)