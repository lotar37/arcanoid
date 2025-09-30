import turtle as черепаха
step = 5
черепаха.speed(20)
черепаха.color("black","red")
def multiangle(angle, size=5):
    черепаха.begin_fill()
    for i in range(angle):
        черепаха.forward(size)
        черепаха.left(360/angle)
    черепаха.end_fill()


for j in range(10):
    multiangle(3, 120)
    черепаха.left(36)
черепаха.backward(200)
for j in range(10):
    multiangle(3, 120)
    черепаха.left(36)

a = input()