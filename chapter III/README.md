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

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/push_3.png)

The QLineEdit Widget
--------------------

It is often necessary for a user to input a single line of text, such as a username or a password. With the **QLineEdit** widget, you can collect data from someone

___________________________________________________________________________
**Tip** if you need multiple lines for a user to enter text, 
use the QTextEdit widget instead.
___________________________________________________________________________

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/lineEdit.png)


The QCheckBox Widget
--------------------

The **QCheckBox** widget is a selectable button that generally has two states: on and off. This makes them perfect for representing features in your GUI that can either be enabled or disabled, or for selecting from a list of options like in a survey.

```python
                        after_cb.toggled.connect(self.printSelected)
```
___________________________________________________________________________
**Note** the checkboxes in QCheckBox are not mutually exclusive, 
meaning you can select more than one checkbox at a time. 
to make them mutually exclusive, add the checkboxes to a QButtonGroup object 
or consider using QRadioButton.
___________________________________________________________________________
![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/checkBox.png)


## The QMessageBox Dialog

When a user closes an application or saves their work, or an error occurs, they will typically see a dialog box pop up and display some sort of key information. The user can then interact with that dialog box, often by clicking a button to respond to the prompt. Dialog boxes are a very important form of **feedback**, or methods of monitoring and communicating changes back to the user.

The **QMessageBox** class can be used to not only alert the user to a situation but also to decide how to handle the matter. For example, when closing a document you just modified, you might get a dialog box with buttons asking you to Save, Don’t Save, or Cancel. 

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/QMessageBox.png)

There are two kinds of dialog boxes. 
* **Modal dialogs**  :   block user interaction from the rest of the program until the dialog box is closed. 

* **Modeless dialogs** : allow the user to interact with both the dialog and the rest of the application.
                         Explanation for Using QMessageBox


```python
                        QMessageBox.information(self,"Author Found",
                                            "Author found in catalogue!",
                                            QMessageBox.StandardButton.Ok
                                        )  

```
the first argument is parent,second is title and third is content, last is the button


## Designing the Login GUI and Registration Dialog

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/login.png)

The setEchoMode() method provided by QLineEdit is very useful for hiding text as it is being input. 

hidden the passwords : 
```python
self.password_edit = QLineEdit(self)
self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
```

show the passwords :

```python
self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
```

## Using Event Handlers to Close a Window

In order to change how the closeEvent() method is handled, 
in this case, for the LoginWindow class, you will need to reimplement the closeEvent()
An example of this is shown in Listing

```python
def closeEvent(self, event):

    """Reimplement the closing event to display a
    QMessageBox before closing."""
```

## Explanation for Creating the Registration Dialog

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20III/image/registration.png)