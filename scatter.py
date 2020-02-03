import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("file directory")

plt.scatter(df.x_axis, df.y_axis)
plt.xlabel('x')
plt.ylabel('y')

plt.xlim(0,1000)
plt.ylim(0,1000)
#plt.axis('off') you dont want no axis png, check this code!

plt.show()
#plt.savefig <---- save the pic
