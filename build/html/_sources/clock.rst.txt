clock
===================
.. automodule:: clock
   :members:
   :private-members:


Class Clock:
	Class that contains the clock widget and clock refresh.

Methods:
	def __init__(self, parent=None, seconds=True, colon=False):
        -  Create and place the clock widget into the parent element.

    def tick(self)
        -  Update the display clock every 200 milliseconds.

    def blink_colon(self)  -  Blink the colon every second.