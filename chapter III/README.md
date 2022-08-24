Adding More Functionality with Widgets
======================================

* Be introduced to event handling and Qt’s signals and slots mechanism

* Build GUIs using new widget classes, including QPushButton, QLineEdit, QCheckBox, and QMessageBox

* Learn about useful methods for aligning text and adjusting widget sizes

* Discover more about windows and dialog boxes and see how to create classes that inherit from QDialog

* Create an application that teaches how to handle multiple windows Before jumping into any code, let’s learn a little about event handling in PyQt.


Event Handlers and Signals and Slots
------------------------------------


 In Qt, events are objects created from the **QEvent** class.
 
 The communication between objects in Qt, such as widgets, is handled by signals and slots. **Signals** are generated whenever an event occurs, such as when a button is clicked or a checkbox is toggled on or off. Those signals then need to be handled in some way. **Slots** are the methods that are connected to an event and executed in response to the signal

```python
                    button.clicked.connect(self.buttonClicked)
```



The QPushButton Widget
----------------------

The **QPushButton** widget can be used to perform actions and make choices. When you click on the QPushButton widget, it sends out a signal that can be connected to a function


___________________________________________________________________________
**Note** there are different kinds of button classes with different usages, 
such as QToolButton for selecting items in toolbars and QRadioButton for 
creating groups of buttons where only a single selection can be made.
___________________________________________________________________________



