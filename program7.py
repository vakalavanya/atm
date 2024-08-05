import matplotlib.pyplot as plt
import numpy as np
def line_plot(x,y):
  plt.plot(x,y)
  plt.title("line plot")
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.show()
def scatter_plot(x,y):
  plt.scatter(x,y)
  plt.title("Scatter Plot")
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.show()
def bar_plot(x,y):
  plt.bar(x,y)
  plt.title("Bar Plot") 
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.show() 
x=np.array(input("enter x data(separated by spaces):").split(),dtype=int)
y=np.array(input("enter y data(separetd by spaces):").split(),dtype=int)
print("which type of plot would like you to  create?")
print("1.Line plot")
print("2.Scatter plot")
print("3.Bar plot")
choice=int(input("enter your choice(1,2,or 3):"))
if choice == 1:
        line_plot(x,y)
elif choice == 2:
        scatter_plot(x,y)
elif choice == 3:
        bar_plot(x,y)
else:
        print("invalid choice.please enter 1,2,or3")
 
