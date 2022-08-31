# Menus, Toolbars, and More

A menu is a list of commands that a computer program can perform presented in a more manageable and organized fashion. Numerous devices and systems include menus for helping the user to navigate and select different options and tasks, and a well-organized menu will make a program easier to use.

• Find out how to create main windows that inherit from QMainWindow

• Create menus, submenus, and checkable menu items using PyQt classes such as QMenuBar and     QAction

• Discover how to set and change widget and main window icons

• Learn about PyQt’s built-in dialog classes, including QFileDialog,
  QInputDialog, QColorDialog, and more

• Set up and utilize an application’s status bar to provide feedback

• Use the QDockWidget class to build detachable widgets that can display common tools and operations

• Build practical applications that teach additional skills, such as manipulating images using QPixmap and QTransform classes and setting up applications that print images with the QPrinter class


## QMainWindow vs. QWidget

![](https://github.com/JohnHe12/pyqt6/blob/main/chapter%20V/images/截屏2022-08-31 23.12.01.png)

The QMainWindow class focuses on creating and managing the layout for the main window of an application. It allows you to set up a window with a status bar, a toolbar, dock widgets, or other menu features in predefined locations.

###  QAction

Take a look at how the Quit action, quit_act, is created and then added to file_menu.

```python
self.quit_act = QAction("&Quit")
self.quit_act.setShortcut("Ctrl+Q")
self.quit_act.triggered.connect(self.close)

self.menuBar().setNativeMenuBar(False)
# Create file menu and add actions
file_menu = self.menuBar().addMenu("File")
file_menu.addAction(self.quit_act)
```

## Using Icons and the QIcon Class

### QFileDialog

class can be used to open and select files or directories on your computer.

```python
file_name, ok = QFileDialog.getOpenFileName(self,
            "Open File", "/Users/user_name/Desktop/",
            "Image Files (*.png *.jpg *.bmp)")
```

Saving a file is done in a similar fashion using getSaveFileName():

```python
file_name, ok = QFileDialog.getSaveFileName(self,
            "Save File", "/Users/user_name/Desktop/",
            "Text Files (*.txt)")
```

```python
file_name, ok = QFileDialog.getOpenFileName(self,
            "Open File", "/Users/user_name/Desktop/",
            "Image Files (*.png *.jpg *.bmp)",
            options = QFileDialog.Option.DontUseNativeDialog)
```

### The QInputDialog Class

```python
find_text, ok = QInputDialog.getText(
            self, "Search Text", "Find:")
```

Other types of input can be collected using one of the following QInputDialog
methods:
• getMultiLineText() – Method to get a multiline string from the user
• getInt() – Method to get an integer from the user
• getDouble() – Method to get a floating-point number from the user
• getItem() – Method to let the user select an item from a list of strings


### The QFontDialog Class

```python
font, ok = QFontDialog.getFont()
```
![]()

```python
font, ok = QFontDialog.getFont(
            QFont("Helvetica", 10), self)
self.text_edit_widget.setCurrentFont(font)
```

### The QColorDialog Class

```java
color = QColorDialog.getColor()
 if color.isValid():
            self.text_field.setTextColor(color)
```

### The About QMessageBox

```php
QMessageBox.about(self, "About Notepad",
            """<p>Beginner's Practical Guide to PyQt</p>
            <p>Project 5.1 - Notepad GUI</p>""")
```