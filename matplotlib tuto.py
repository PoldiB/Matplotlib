from matplotlib import pyplot as plt

plt.style.use('ggplot')

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

py_dev_x = [25,26,27,28,29,30,31,32,33,34,35]

py_dev_y = [45372,48876,53850,57286,63016,
            65998,70003,70000,71496,75370,83640]
plt.plot(ages_x,py_dev_y,color='#5a7d9a',linewidth=3,label='Python Developers')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y,color='#adad3b',linewidth=3,label='Java Developers')

dev_y = [38496,42000,46752,49320,53200,
         56000,62316,64928,67317,68478,73752]
plt.plot(ages_x, dev_y,color='#444444',linestyle='--',label='All Developers')

plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')

plt.title('Median Salary (USD) by age')

plt.legend()

plt.tight_layout()

plt.savefig('/home/poldi/benniopa/plot.png')

plt.show()