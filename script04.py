# 4th example from following website:
# https://appsilon.com/use-r-and-python-together/#:~:text=You%20can%20import%20any%20Python,and%20functions%20declared%20with%20R.&text=And%20that's%20how%20you%20can%20run,in%20R%20and%20R%20Markdown.
# producing a ggplot2 image
from rpy2.robjects.packages import importr, data
import rpy2.robjects.lib.ggplot2 as ggplot2


grdevices = importr('grDevices')
grdevices.png(file="/Users/JonMinton/repos/python-r-101/r-figures/mtcars.png", width=1024, height=512)
datasets = importr('datasets')
mtcars = data(datasets).fetch('mtcars')['mtcars']

pp = (ggplot2.ggplot(mtcars) +
      ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') +
      ggplot2.geom_point())
pp.plot()

grdevices.dev_off()

# This works, but with deprecation warnings!