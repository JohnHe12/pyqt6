# Handling Events in PyQt

## Handling Key Events

• keyPressEvent() – Handles a key event when the key is pressed

• keyReleaseEvent() – Handles a key event when the key is released

Some key names include Key_Escape, Key_Return, Key_Up, Key_Down, Key_Space, Key_0, Key_1, and so on. A full list of Qt.Key enum keyboard codes can be found at

[link](https://doc.qt.io/qt-6/qt.html#Key-enum)


## Handling Mouse Events

• mousePressEvent() – Handles events when the mouse button is
  pressed.

• mouseReleaseEvent() – Handles events when the mouse button is released.

• mouseMoveEvent() – Handles events when the mouse button is pressed and moved. Turn on mouse tracking to enable move events even if a mouse button is not pressed with QWidget. setMouseTracking(True).

• mouseDoubleClickEvent() – Handles events when the mouse button is double-clicked.

• enterEvent() – Handles when the mouse cursor enters a widget

• leaveEvent() – Handles when the mouse cursor leaves a widget