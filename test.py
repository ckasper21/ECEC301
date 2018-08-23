from spirograph import Spirograph

myspirograph=Spirograph(500)
myspirograph.setSmallCircle(85)
myspirograph.setPen(.65,'red')
myspirograph.draw()
myspirograph.pause()

myspirograph.setSmallCircle(120)
myspirograph.setPen(.5,'blue')
myspirograph.draw()
myspirograph.pause()

myspirograph.clear()

myspirograph.setSmallCircle(20)
myspirograph.setPen(.8,'purple')
myspirograph.draw()
myspirograph.pause()

myspirograph.close()
