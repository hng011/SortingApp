from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from random import randint
import random
import cpuinfo,platform,psutil,sorting_function,time
# perf_counter for time

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting App")
        tab_widget = QTabWidget(self)
        self.setFixedWidth(350)
        self.setWindowIcon(QIcon("img/icon.png"))        

        #### Tab 1
        #Inputing data
        generate_page = QWidget()
        label_amountOfData = QLabel("Define the size of data:")
        self.input = QSpinBox(self)
        self.maxValue = 99999
        self.input.setRange(0,self.maxValue)
        max_info = QLabel(f"Max-size = {self.maxValue} ✌️")
        
        #generate button
        generate_button = QPushButton("Hit !!! 👊👊👊")
        generate_button.clicked.connect(self.start_generate)
        response = QLabel("Response: ")

        #success label
        self.label_successGenerate = QLabel()

        #layouting
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(label_amountOfData)
        Hlayout.addWidget(self.input)        
        
        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(max_info)
        Vlayout.addWidget(generate_button)
        Vlayout.addWidget(response)
        Vlayout.addWidget(self.label_successGenerate)

        generate_page.setLayout(Vlayout)

        #tab 2
        sort_page = QWidget()
        
        #TODO : get the file resource
        self.name_file_label = QLabel("File :")
        select_file_button = QPushButton("Select File 👀")
        select_file_button.clicked.connect(self.select_file_button)

        #TODO : make a dropdown for each sorting algorithm!! 
        self.algorithm_selection = QComboBox(self)
        self.algorithm_selection.addItem("Bubble Sort")
        self.algorithm_selection.addItem("Insertion Sort")
        self.algorithm_selection.addItem("Selection Sort")
        self.algorithm_selection.addItem("Native Sort")

        label_sorting_algorithm = QLabel("Sorting Algorithm")
        
        Hlayout = QHBoxLayout()
        Vlayout = QVBoxLayout()

        Vlayout.addWidget(self.name_file_label)
        Vlayout.addWidget(select_file_button)
        Hlayout.addWidget(label_sorting_algorithm)
        Hlayout.addWidget(self.algorithm_selection)

        #BUTTON FOR start sorting
        sorting_button = QPushButton("Lets GO !!! 👊👊👊")
        sorting_button.clicked.connect(self.start_sorting_button)

        ##SHOW device specification
        self.system_info_show = QLabel()
        
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(sorting_button)
        Vlayout.addWidget(self.system_info_show)
        sort_page.setLayout(Vlayout)

        #Add tabs to widget
        tab_widget.addTab(generate_page,"Generate 🪄")
        tab_widget.addTab(sort_page,"Sorting ⚒️")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def start_generate(self):
        try:
            val = int(self.input.value())
            if val != 0:
                ##start generating
                f = open("unsorted_data/unsorted_data.txt","w")
                new_num = []
                s = time.perf_counter()
                for i in range(val):
                    random_num = random.random()*val
                    val_length = len(str(val))
                    num = str(round(random_num,val_length))
                    length_num = len(num)
                    if length_num == val_length+2:
                        new_num.append(int(num[0]))
                    else:
                        new_num.append(round(random_num,1))

                f.write(",".join(str(mynum) for mynum in new_num))
                f.close()
                e = time.perf_counter()

                s_time = (e-s)
                ms_time = s_time*1000
                self.label_successGenerate.setText(f'''
Success generating {val} number👌
Generating time : {round(ms_time,5)} ms | {round(s_time,5)} s
File name: unsorted.txt
Your file was stored in the 'source' folder!!
                ''')
            else:
                warn = QMessageBox.critical(self,"Warning!",f"Input must be greater than 0 and lower than {self.maxValue + 1} 😠",QMessageBox.Ok)
            
            #reset spinner
            self.input.setValue(0)

        except Exception as e:
            self.label_successGenerate.setText("Something wrong")
            print(e)
    
    def select_file_button(self):
        self.file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 "/V1.0/",
                                 "Text(*.txt)")
        if((self.file_name == "")):
            return
        self.name_file_label.setText("File : " + self.file_name)
    
    #Start sorting
    def start_sorting_button(self):
        try:
            # Pop up when no files selected
            if(self.name_file_label.text() == "File :"):
                warn = QMessageBox.critical(self,"Warning!","No file selected 😒",QMessageBox.Ok)
            else:
                try:
                    # #For bubble sort
                    if(self.algorithm_selection.currentIndex() == 0):
                        print("You choose " + self.algorithm_selection.currentText())
                        file = self.file_name
                        s = time.perf_counter()
                        sorting_function.bubble_sort(file)
                        e = time.perf_counter()
                        s_time = (e-s)
                        ms_time = s_time*1000
                        print(f"{self.algorithm_selection.currentText()} : {round(ms_time,5)} ms | {round(s_time,5)} s")

                    #for Insertion sort
                    elif(self.algorithm_selection.currentIndex() == 1):
                        print("You choose " + self.algorithm_selection.currentText())
                        file = self.file_name
                        s = time.perf_counter()
                        sorting_function.insertion_sort(file)
                        e = time.perf_counter()
                        s_time = (e-s)
                        ms_time = s_time*1000
                        print(f"{self.algorithm_selection.currentText()} : {round(ms_time,5)} ms | {round(s_time,5)} s")

                    # #for selection sort
                    elif(self.algorithm_selection.currentIndex() == 2):
                        print("You choose " + self.algorithm_selection.currentText())
                        file = self.file_name
                        s = time.perf_counter()
                        sorting_function.selection_sort(file)
                        e = time.perf_counter()
                        s_time = (e-s)
                        ms_time = s_time*1000
                        print(f"{self.algorithm_selection.currentText()} : {round(ms_time,5)} ms | {round(s_time,5)} s")
                    
                    # #for native sort
                    elif(self.algorithm_selection.currentIndex() == 3):
                        print("You choose " + self.algorithm_selection.currentText())
                        file = self.file_name
                        s = time.perf_counter()
                        sorting_function.native_sort(file)
                        e = time.perf_counter()
                        s_time = (e-s)
                        ms_time = s_time*1000
                        print(f"{self.algorithm_selection.currentText()} : {round(ms_time,5)} ms | {round(s_time,5)} s")

                    ##When all success!!
                    self.system_info_show.setText(f"""
- Sorting with '{self.algorithm_selection.currentText().upper()}' was successful 👌-
Execution Program : {round(ms_time,5)} ms | {round(s_time,5)} s
your sorted file was stored in the 'source' folder!!

=== System Information ===
System : {platform.system()}
Processor : {cpuinfo.get_cpu_info()["brand_raw"]}
Memory : {round(psutil.virtual_memory().total/1000000000, 2)} GB
""")
                except Exception as e:
                    warn = QMessageBox.critical(self,"Warning!",f"{e}",QMessageBox.Ok)
                    print(e)

        except Exception as e:
            warn = QMessageBox.critical(self,"Warning!",f"{e}",QMessageBox.Ok)
            print(e)