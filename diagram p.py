import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [20,16,12,8,4,0.5]

plt.barh(y_pos, performance, align='center', alpha=0.7,color='purple')
plt.yticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.xlabel('Languages')

plt.show()