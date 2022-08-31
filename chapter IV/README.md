# Learning About Layout Management

## Content :

>>* Learn about PyQt’s layout manager classes and apply them in numerous GUIs

>>* Consider which layout manager is best for your application

>>* Find out how to create complex layouts with nested layouts

>>* Explore a few different techniques for managing widgets in layout managers, such as adding spaces or working with size policies

>>* Use a variety of new classes, including QComboBox, QSpinBox, QDoubleSpinBox, QButtonGroup, QTextEdit, QDateEdit, and more, 
    to expand your toolkit and knowledge about creating incredible GUIs

>>* Expand your experience with previously learned widget classes while building practical applications

## Using Layout Managers in PyQt

Layout management is the useful practice of arranging widgets in GUIs

```python
#  This is because a layout manager will automatically take care of reparenting widgets 
# to be associated with the parent widget
label = QLabel("Name")
line_edit = QLineEdit()
```
```python

v_box = QVBoxLayout() # Create layout manager instance
v_box.addWidget(label) # Add widgets to the layout
v_box.addWidget(line_edit)
parent_widget.setLayout(v_box) # Set the layout for the parent
```
**NOTE**：
 >>The parent widget could be a widget, a window, or even a dialog. 
 >>Layout managers cannot be parents for widgets; only widgets can be parents for other widgets.

Instead of using setLayout(), you can also pass the parent widget to the layout manager, like so:
```python
v_box = QVBoxLayout(parent_widget)
```

**nested layout** :
```python
h_box = QHBoxLayout()
v_box.addLayout(h_box)
```

## Horizontal and Vertical Layouts with Box Layouts

• QHBoxLayout – Arranges widgets horizontally from left to right or vice versa

• QVBoxLayout – Arranges widgets vertically from top to bottom or vice versa

addWidget(widget, stretch, alignment)

The stretch parameter refers to the **stretch facto**r, or how much the widgets will stretch in relation to other widgets in the row or column. 
The value for stretch is an int, where 0 uses a widget's default parameters to set the stretch factor. 
Widgets are laid out proportionally, and ones with larger stretch values will use more space. 
Widgets can also be aligned in a row or column using the alignment argument.

### The QButtonGroup Class

 This can be helpful if you only want one checkbox to be checked at a time.

1. Create a QButtonGroup instance and make it a member of a class, meaning create an instance variable of the class, 
   that is, self. button_group, or pass a parent object as an argument, that is, button_group = QButtonGroup(self).

2. Create the button or checkbox objects that will be added to the button group from step 1.

3. Add the buttons from step 2 to the button group using the QButtonGroup method addButton().

4. Connect all buttons in a group to one signal, such as the QButtonGroup signal buttonClicked.

5. Add the widgets created in step 2 to a layout manager.

### The QSpinBox and QComboBox Widgets

**QSpinBox** creates an object that is similar to a text box but allows the user to select integer values by either typing a value into the widget or by clicking on up and down arrows. You can also edit the range of the values, set the step size when the arrow
is clicked, set a starting value, or even add prefixes or suffixes in the box. There are classes similar to QSpinBox that provide similar functionality for different situations. 

```python
self.price_sb1 = QSpinBox()
self.price_sb1.setRange(0, 100)
self.price_sb1.setPrefix("$")
self.price_sb1.valueChanged.connect(
    self.calculateTotal)
```

**QDoubleSpinBox** is used for selecting floating-point numbers. 

**QDateTimeEdit** or one of its variations is useful for selecting date and time values.

The **QComboBox** widget displays a drop-down list of options for the user to select when a user clicks on the widget’s arrow button. Combo boxes are handy for displaying a large amount of options in the least amount of space.

```python
food_combo1 = QComboBox()
food_combo1.addItems(food_list)
self.price_sb1.valueChanged.connect(self.calculateTotal)
```

**QRegularExpression**
```python
reg_opt = QRegularExpression()
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            reg_opt.PatternOption.CaseInsensitiveOption)
        self.email_edit.setValidator(
            QRegularExpressionValidator(regex))
```

The ***QDateEdit*** instance’s format for visualizing a date is set with ***setDisplayFormat()***. The maximum range of the widget is set to the date the user opens the application using ***QDate.currentDate()***. QDateEdit has a convenience function, ***setCalendarPopup()***, that will allow a calendar to appear whenever the arrow in the widget is clicked. The initial date that appears in the widget is set with ***setDate()***.
```python
self.birthdate_edit = QDateEdit()
        self.birthdate_edit.setDisplayFormat("MM/dd/yyyy")
        self.birthdate_edit.setMaximumDate(
            QDate.currentDate())
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setDate(QDate.currentDate())
```

*** QRegularExpression***

```python
reg_opt = QRegularExpression()
regex = QRegularExpression(
    "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
    reg_opt.PatternOption.CaseInsensitiveOption)
self.email_edit.setValidator(
    QRegularExpressionValidator(regex))

```

## Adding Widgets and Layouts to QFormLayout

```python
 main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(
            main_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        main_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | \
            Qt.AlignmentFlag.AlignTop)
        main_form.setLabelAlignment(
            Qt.AlignmentFlag.AlignLeft)
        main_form.addRow(header_label)
        main_form.addRow("Name", name_h_box)
        main_form.addRow("Gender", gender_combo)
        main_form.addRow("Date of Birth", self.birthdate_edit)
        main_form.addRow("Phone", self.phone_edit)
        main_form.addRow("Email", self.email_edit)
        main_form.addRow(QLabel("Comments or Messages"))
        main_form.addRow(extra_info_tedit)
        main_form.addRow(submit_h_box)
        # Set the layout for the main window
        self.setLayout(main_form)
```

## Explanation for QStackedLayout

```python
 # Create the stacked layout and add pages
    self.stacked_layout = QStackedLayout()
    self.stacked_layout.addWidget(profile_image)
    self.stacked_layout.addWidget(pg2_container)
    self.stacked_layout.addWidget(pg3_container)
    # Create the main layout
    main_v_box = QVBoxLayout()
    main_v_box.addWidget(page_combo)
    main_v_box.addLayout(self.stacked_layout)
    # Set the layout for the main window
    self.setLayout(main_v_box)
def switchPage(self, index):
    """Slot for switching between tabs."""
    self.stacked_layout.setCurrentIndex(index)
```
