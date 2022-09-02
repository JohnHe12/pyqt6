import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QGroupBox,
                            QButtonGroup,QLabel,QTabWidget,QPushButton,
                            QVBoxLayout,QHBoxLayout,QGridLayout,QMessageBox,QRadioButton)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import os
os.chdir(os.path.dirname(__file__))

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.initializUI()

    def initializUI(self):

        self.setMinimumSize(500,800)
        self.setWindowTitle("Pizza Order")
        self.setUpMainWindow()
        self.show()
    
    def setUpMainWindow(self):

        tab_wgt = QTabWidget()

        self.pizza_wgt = QWidget()
        self.wing_wgt = QWidget()

        tab_wgt.addTab(self.pizza_wgt,"Pizza")
        tab_wgt.addTab(self.wing_wgt,"Wings")

        self.createPizza()
        self.createWings()

        self.side_wgt = QWidget()
        order_label = QLabel("YOUR ORDER")
        self.side_grid_layout = QGridLayout()
        pizza_label = QLabel("Pizza Type: ")
        self.side_grid_layout.addWidget(pizza_label,0,0,Qt.AlignmentFlag.AlignLeft)
        self.crust_gp.checkedButton().text()
        topping_label = QLabel("Toppings")

    def createPizza(self):

        build_header = QLabel("BUILD YOUR OWN PIZZA")
        des_wgt = QWidget()
        pizza_image_path = "images/pizza.png"
        image=self.loadImage(pizza_image_path)
        pizza_des = QLabel()
        pizza_des.setText(
            """<p>Build a custom pizza for you. Start with 
            your favorite crust and add any toppings, plus 
            the perfect amount of cheese and sauce.</p>"""
        )
        pizza_des.setWordWrap(True)
        
        des_v_layout = QHBoxLayout()
        des_v_layout.addWidget(image)
        des_v_layout.addWidget(pizza_des,1)
        des_wgt.setLayout(des_v_layout)

        crust_box = QGroupBox()
        crust_box.setTitle("CHOOSE YOUR CRUST")

        crust_list = ["Hand-Tossed","Flat","Stuffed"]
        crust_v_layout = QVBoxLayout()
        self.crust_gp = QButtonGroup()
        
        for crust in crust_list:
            crust_rb = QRadioButton(crust)
            self.crust_gp.addButton(crust_rb)
            crust_v_layout.addWidget(crust_rb)
        
        crust_box.setLayout(crust_v_layout)

        toppings_gbox = QGroupBox()
        toppings_gbox.setTitle("CHOOSE YOUR TOPPINGS")

        # Set up button group for toppings radio buttons
        self.toppings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()

        toppings_list = ["Pepperoni", "Sausage", "Bacon", 
                        "Canadian Bacon", "Beef", "Pineapple", 
                        "Olive", "Tomato", "Green Pepper", 
                        "Mushroom", "Onion", "Spinach", "Cheese"]
        # Create radio buttons for the different toppings and 
        # add to layout
        for top in toppings_list:
            toppings_rb = QRadioButton(top)
            gb_v_box.addWidget(toppings_rb)
            self.toppings_group.addButton(toppings_rb)
        self.toppings_group.setExclusive(False)
        toppings_gbox.setLayout(gb_v_box)

        order_bnt = QPushButton("Add to Order")
        order_bnt.clicked.connect(self.displaySideWidgt)

        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(build_header)
        main_v_layout.addWidget(des_wgt)
        main_v_layout.addWidget(crust_box)
        main_v_layout.addWidget(toppings_gbox,2)
        main_v_layout.addWidget(order_bnt,1)
        self.pizza_wgt.setLayout(main_v_layout)

    def createWings(self):

        """Create the wings tab. Allows the user to select the 
        type of pizza and toppings using radio buttons."""
        # Set up widgets and layouts to display information 
        # to the user about the page
        tab_wings_label = QLabel("TRY OUR AMAZING WINGS")
        tab_wings_label.setObjectName("Header")
        description_box = QWidget()
        description_box.setObjectName("ImageBorder")
        wings_image_path = "images/wings.png"
        wings_image = self.loadImage(wings_image_path)
        wings_desc = QLabel()
        wings_desc.setObjectName("ImageInfo")
        wings_desc.setText(
            """<p>6 pieces of rich-tasting, white meat 
            chicken that will have you coming back for 
            more.</p>""")
        wings_desc.setWordWrap(True)
        wings_desc.setContentsMargins(10, 10, 10, 10)

        wings_h_box = QHBoxLayout()
        wings_h_box.addWidget(wings_image)
        wings_h_box.addWidget(wings_desc, 1)

        description_box.setLayout(wings_h_box)

        wings_gbox = QGroupBox()
        wings_gbox.setTitle("CHOOSE YOUR FLAVOR")

        self.wings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        flavors_list = ["Buffalo", "Sweet-Sour", "Teriyaki", "Barbecue"]

        # Create radio buttons for the different flavors and 
        # add to layout
        for fl in flavors_list:
            flavor_rb = QRadioButton(fl)
            gb_v_box.addWidget(flavor_rb)
            self.wings_group.addButton(flavor_rb)
          
        wings_gbox.setLayout(gb_v_box)

        # Create button to add information to side widget
        # when clicked
        add_to_order_button2 = QPushButton("Add To Order")
        add_to_order_button2.clicked.connect(self.displayWingsInOrder)
        
        # create layout for wings tab (page 2)
        page2_v_box = QVBoxLayout()
        page2_v_box.addWidget(tab_wings_label)
        page2_v_box.addWidget(description_box)
        page2_v_box.addWidget(wings_gbox)
        page2_v_box.addWidget(add_to_order_button2, 
            alignment=Qt.AlignmentFlag.AlignRight)
        page2_v_box.addStretch()

        self.wing_wgt(page2_v_box)


    def loadImage(self,pizza_image_path):

        try:
            with open(pizza_image_path):
                image_labe = QLabel()
                image = QPixmap(pizza_image_path)
                image_labe.setPixmap(image.scaled(
                    image_labe.size(),aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                    transformMode=Qt.TransformationMode.SmoothTransformation
                ))

                return image_labe
        except FileNotFoundError as error:
            QMessageBox.warning(
                self, "IMAGE NOT FIND",
                f"""<p>Error : {error}</p>
                <p>please check the direction</p>""",
                QMessageBox.StandardButton.Close
            )

    

if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
