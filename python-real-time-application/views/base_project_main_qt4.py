# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/base_project_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_EMG = QtGui.QWidget()
        self.tab_EMG.setObjectName(_fromUtf8("tab_EMG"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_EMG)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayoutGraphStatus = QtGui.QVBoxLayout()
        self.verticalLayoutGraphStatus.setObjectName(_fromUtf8("verticalLayoutGraphStatus"))
        self.verticalLayoutGraph = QtGui.QVBoxLayout()
        self.verticalLayoutGraph.setObjectName(_fromUtf8("verticalLayoutGraph"))
        self.label_replace = QtGui.QLabel(self.tab_EMG)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName(_fromUtf8("label_replace"))
        self.verticalLayoutGraph.addWidget(self.label_replace)
        self.verticalLayoutGraphStatus.addLayout(self.verticalLayoutGraph)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbl_status = QtGui.QLabel(self.tab_EMG)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_status.sizePolicy().hasHeightForWidth())
        self.lbl_status.setSizePolicy(sizePolicy)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.horizontalLayout_3.addWidget(self.lbl_status)
        self.cb_chart_emg_on_off = QtGui.QCheckBox(self.tab_EMG)
        self.cb_chart_emg_on_off.setChecked(True)
        self.cb_chart_emg_on_off.setObjectName(_fromUtf8("cb_chart_emg_on_off"))
        self.horizontalLayout_3.addWidget(self.cb_chart_emg_on_off)
        self.verticalLayoutGraphStatus.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayoutGraphStatus)
        self.tabWidget.addTab(self.tab_EMG, _fromUtf8(""))
        self.tab_features = QtGui.QWidget()
        self.tab_features.setObjectName(_fromUtf8("tab_features"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_features)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayoutGraphStatus_features = QtGui.QVBoxLayout()
        self.verticalLayoutGraphStatus_features.setObjectName(_fromUtf8("verticalLayoutGraphStatus_features"))
        self.verticalLayoutGraph_features = QtGui.QVBoxLayout()
        self.verticalLayoutGraph_features.setObjectName(_fromUtf8("verticalLayoutGraph_features"))
        self.horizontalLayout_features = QtGui.QHBoxLayout()
        self.horizontalLayout_features.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_features.setObjectName(_fromUtf8("horizontalLayout_features"))
        self.label_features = QtGui.QLabel(self.tab_features)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_features.sizePolicy().hasHeightForWidth())
        self.label_features.setSizePolicy(sizePolicy)
        self.label_features.setObjectName(_fromUtf8("label_features"))
        self.horizontalLayout_features.addWidget(self.label_features)
        self.cb_features = QtGui.QComboBox(self.tab_features)
        self.cb_features.setEditable(False)
        self.cb_features.setObjectName(_fromUtf8("cb_features"))
        self.horizontalLayout_features.addWidget(self.cb_features)
        self.checkBox = QtGui.QCheckBox(self.tab_features)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_features.addWidget(self.checkBox)
        self.verticalLayoutGraph_features.addLayout(self.horizontalLayout_features)
        self.label_replace_features = QtGui.QLabel(self.tab_features)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace_features.sizePolicy().hasHeightForWidth())
        self.label_replace_features.setSizePolicy(sizePolicy)
        self.label_replace_features.setObjectName(_fromUtf8("label_replace_features"))
        self.verticalLayoutGraph_features.addWidget(self.label_replace_features)
        self.verticalLayoutGraphStatus_features.addLayout(self.verticalLayoutGraph_features)
        self.horizontalLayout_status_features = QtGui.QHBoxLayout()
        self.horizontalLayout_status_features.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_status_features.setObjectName(_fromUtf8("horizontalLayout_status_features"))
        self.lbl_status_features = QtGui.QLabel(self.tab_features)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_status_features.sizePolicy().hasHeightForWidth())
        self.lbl_status_features.setSizePolicy(sizePolicy)
        self.lbl_status_features.setObjectName(_fromUtf8("lbl_status_features"))
        self.horizontalLayout_status_features.addWidget(self.lbl_status_features)
        self.cb_chart_features_on_off = QtGui.QCheckBox(self.tab_features)
        self.cb_chart_features_on_off.setChecked(True)
        self.cb_chart_features_on_off.setObjectName(_fromUtf8("cb_chart_features_on_off"))
        self.horizontalLayout_status_features.addWidget(self.cb_chart_features_on_off)
        self.verticalLayoutGraphStatus_features.addLayout(self.horizontalLayout_status_features)
        self.horizontalLayout_5.addLayout(self.verticalLayoutGraphStatus_features)
        self.tabWidget.addTab(self.tab_features, _fromUtf8(""))
        self.tab_classification = QtGui.QWidget()
        self.tab_classification.setObjectName(_fromUtf8("tab_classification"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_classification)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.graphicsView_classification = QtGui.QGraphicsView(self.tab_classification)
        self.graphicsView_classification.setObjectName(_fromUtf8("graphicsView_classification"))
        self.horizontalLayout_6.addWidget(self.graphicsView_classification)
        self.tabWidget.addTab(self.tab_classification, _fromUtf8(""))
        self.tab_controle_manuel = QtGui.QWidget()
        self.tab_controle_manuel.setObjectName(_fromUtf8("tab_controle_manuel"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_controle_manuel)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_f1 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_f1.setObjectName(_fromUtf8("groupBox_f1"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_f1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.h_slider_1 = QtGui.QSlider(self.groupBox_f1)
        self.h_slider_1.setMaximum(90)
        self.h_slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_1.setObjectName(_fromUtf8("h_slider_1"))
        self.verticalLayout_11.addWidget(self.h_slider_1)
        self.verticalLayout_6.addWidget(self.groupBox_f1)
        self.groupBox_f2 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_f2.setObjectName(_fromUtf8("groupBox_f2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_f2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.h_slider_2 = QtGui.QSlider(self.groupBox_f2)
        self.h_slider_2.setMaximum(90)
        self.h_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_2.setObjectName(_fromUtf8("h_slider_2"))
        self.verticalLayout_8.addWidget(self.h_slider_2)
        self.verticalLayout_6.addWidget(self.groupBox_f2)
        self.groupBox_f3 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_f3.setObjectName(_fromUtf8("groupBox_f3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_f3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.h_slider_3 = QtGui.QSlider(self.groupBox_f3)
        self.h_slider_3.setMaximum(90)
        self.h_slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_3.setObjectName(_fromUtf8("h_slider_3"))
        self.verticalLayout_9.addWidget(self.h_slider_3)
        self.verticalLayout_6.addWidget(self.groupBox_f3)
        self.groupBox_f4 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_f4.setObjectName(_fromUtf8("groupBox_f4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_f4)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.h_slider_4 = QtGui.QSlider(self.groupBox_f4)
        self.h_slider_4.setMaximum(90)
        self.h_slider_4.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_4.setObjectName(_fromUtf8("h_slider_4"))
        self.verticalLayout_10.addWidget(self.h_slider_4)
        self.verticalLayout_6.addWidget(self.groupBox_f4)
        self.groupBox_f5 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_f5.setObjectName(_fromUtf8("groupBox_f5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_f5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.h_slider_5 = QtGui.QSlider(self.groupBox_f5)
        self.h_slider_5.setMaximum(90)
        self.h_slider_5.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_5.setObjectName(_fromUtf8("h_slider_5"))
        self.verticalLayout_4.addWidget(self.h_slider_5)
        self.verticalLayout_6.addWidget(self.groupBox_f5)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_controle_manuel)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.btn_laser = QtGui.QPushButton(self.groupBox_4)
        self.btn_laser.setObjectName(_fromUtf8("btn_laser"))
        self.horizontalLayout_10.addWidget(self.btn_laser)
        self.btn_reset_position = QtGui.QPushButton(self.groupBox_4)
        self.btn_reset_position.setObjectName(_fromUtf8("btn_reset_position"))
        self.horizontalLayout_10.addWidget(self.btn_reset_position)
        self.btn_close_position = QtGui.QPushButton(self.groupBox_4)
        self.btn_close_position.setObjectName(_fromUtf8("btn_close_position"))
        self.horizontalLayout_10.addWidget(self.btn_close_position)
        self.btn_send_position = QtGui.QPushButton(self.groupBox_4)
        self.btn_send_position.setObjectName(_fromUtf8("btn_send_position"))
        self.horizontalLayout_10.addWidget(self.btn_send_position)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_controle_manuel, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_settings = QtGui.QWidget()
        self.tab_settings.setObjectName(_fromUtf8("tab_settings"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_settings)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_settings)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.cb_in_serial_port = QtGui.QComboBox(self.groupBox_10)
        self.cb_in_serial_port.setObjectName(_fromUtf8("cb_in_serial_port"))
        self.horizontalLayout_13.addWidget(self.cb_in_serial_port)
        self.horizontalLayout_11.addWidget(self.groupBox_10)
        self.groupBox_8 = QtGui.QGroupBox(self.tab_settings)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.cb_out_serial_port = QtGui.QComboBox(self.groupBox_8)
        self.cb_out_serial_port.setObjectName(_fromUtf8("cb_out_serial_port"))
        self.horizontalLayout_12.addWidget(self.cb_out_serial_port)
        self.horizontalLayout_11.addWidget(self.groupBox_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.btn_go = QtGui.QPushButton(self.tab_settings)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.btn_go.setFont(font)
        self.btn_go.setObjectName(_fromUtf8("btn_go"))
        self.verticalLayout_7.addWidget(self.btn_go)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.tab_settings)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_7.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_settings, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFunctions = QtGui.QMenu(self.menubar)
        self.menuFunctions.setObjectName(_fromUtf8("menuFunctions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayoutOptions = QtGui.QVBoxLayout()
        self.verticalLayoutOptions.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayoutOptions.setObjectName(_fromUtf8("verticalLayoutOptions"))
        self.lbl_options = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy)
        self.lbl_options.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_options.setFont(font)
        self.lbl_options.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_options.setObjectName(_fromUtf8("lbl_options"))
        self.verticalLayoutOptions.addWidget(self.lbl_options)
        self.verticalLayoutThreshould = QtGui.QVBoxLayout()
        self.verticalLayoutThreshould.setObjectName(_fromUtf8("verticalLayoutThreshould"))
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btn_record_raw_emg = QtGui.QPushButton(self.groupBox)
        self.btn_record_raw_emg.setObjectName(_fromUtf8("btn_record_raw_emg"))
        self.verticalLayout_2.addWidget(self.btn_record_raw_emg)
        self.label_file_name = QtGui.QLabel(self.groupBox)
        self.label_file_name.setObjectName(_fromUtf8("label_file_name"))
        self.verticalLayout_2.addWidget(self.label_file_name)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lbl_output_name = QtGui.QLabel(self.groupBox)
        self.lbl_output_name.setObjectName(_fromUtf8("lbl_output_name"))
        self.horizontalLayout_7.addWidget(self.lbl_output_name)
        self.lbl_output_value = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_output_value.sizePolicy().hasHeightForWidth())
        self.lbl_output_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_output_value.setFont(font)
        self.lbl_output_value.setObjectName(_fromUtf8("lbl_output_value"))
        self.horizontalLayout_7.addWidget(self.lbl_output_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.btn_generate_training_file = QtGui.QPushButton(self.groupBox)
        self.btn_generate_training_file.setObjectName(_fromUtf8("btn_generate_training_file"))
        self.verticalLayout_2.addWidget(self.btn_generate_training_file)
        self.btn_load_training_file = QtGui.QPushButton(self.groupBox)
        self.btn_load_training_file.setObjectName(_fromUtf8("btn_load_training_file"))
        self.verticalLayout_2.addWidget(self.btn_load_training_file)
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutThreshould.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_acquiring_status = QtGui.QLabel(self.groupBox_2)
        self.label_acquiring_status.setObjectName(_fromUtf8("label_acquiring_status"))
        self.verticalLayout_3.addWidget(self.label_acquiring_status)
        self.label_plotting_status = QtGui.QLabel(self.groupBox_2)
        self.label_plotting_status.setObjectName(_fromUtf8("label_plotting_status"))
        self.verticalLayout_3.addWidget(self.label_plotting_status)
        self.label_processing_status = QtGui.QLabel(self.groupBox_2)
        self.label_processing_status.setObjectName(_fromUtf8("label_processing_status"))
        self.verticalLayout_3.addWidget(self.label_processing_status)
        self.label_classification_status = QtGui.QLabel(self.groupBox_2)
        self.label_classification_status.setObjectName(_fromUtf8("label_classification_status"))
        self.verticalLayout_3.addWidget(self.label_classification_status)
        self.verticalLayoutThreshould.addWidget(self.groupBox_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayoutThreshould.addItem(spacerItem2)
        self.verticalLayoutCheckBoxes = QtGui.QVBoxLayout()
        self.verticalLayoutCheckBoxes.setObjectName(_fromUtf8("verticalLayoutCheckBoxes"))
        self.label_channels = QtGui.QLabel(self.dockWidgetContents)
        self.label_channels.setObjectName(_fromUtf8("label_channels"))
        self.verticalLayoutCheckBoxes.addWidget(self.label_channels)
        self.cb_ch1 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch1.setObjectName(_fromUtf8("cb_ch1"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch1)
        self.cb_ch3 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch3.setObjectName(_fromUtf8("cb_ch3"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch3)
        self.cb_ch4 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch4.setObjectName(_fromUtf8("cb_ch4"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch4)
        self.cb_ch2 = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_ch2.setObjectName(_fromUtf8("cb_ch2"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ch2)
        self.verticalLayoutThreshould.addLayout(self.verticalLayoutCheckBoxes)
        self.verticalLayoutOptions.addLayout(self.verticalLayoutThreshould)
        self.verticalLayout.addLayout(self.verticalLayoutOptions)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionSimples = QtGui.QAction(MainWindow)
        self.actionSimples.setObjectName(_fromUtf8("actionSimples"))
        self.actionIn_Plotter = QtGui.QAction(MainWindow)
        self.actionIn_Plotter.setObjectName(_fromUtf8("actionIn_Plotter"))
        self.actionThread = QtGui.QAction(MainWindow)
        self.actionThread.setObjectName(_fromUtf8("actionThread"))
        self.actionDesativado = QtGui.QAction(MainWindow)
        self.actionDesativado.setObjectName(_fromUtf8("actionDesativado"))
        self.actionStartAcquisition = QtGui.QAction(MainWindow)
        self.actionStartAcquisition.setCheckable(False)
        self.actionStartAcquisition.setObjectName(_fromUtf8("actionStartAcquisition"))
        self.actionStart_Recording = QtGui.QAction(MainWindow)
        self.actionStart_Recording.setObjectName(_fromUtf8("actionStart_Recording"))
        self.actionStop_Recording = QtGui.QAction(MainWindow)
        self.actionStop_Recording.setObjectName(_fromUtf8("actionStop_Recording"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionFind_Serial_Port = QtGui.QAction(MainWindow)
        self.actionFind_Serial_Port.setObjectName(_fromUtf8("actionFind_Serial_Port"))
        self.menuArquivo.addAction(self.actionStart_Recording)
        self.menuArquivo.addAction(self.actionStop_Recording)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFunctions.addAction(self.actionStartAcquisition)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionFind_Serial_Port)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.cb_features.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Main", None))
        self.label_replace.setText(_translate("MainWindow", "Here will be the chart", None))
        self.lbl_status.setText(_translate("MainWindow", "Status:", None))
        self.cb_chart_emg_on_off.setText(_translate("MainWindow", "Chart On/Off", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_EMG), _translate("MainWindow", "EMG", None))
        self.label_features.setText(_translate("MainWindow", "Feature:", None))
        self.checkBox.setText(_translate("MainWindow", "Visible", None))
        self.label_replace_features.setText(_translate("MainWindow", "Here will be another the chart", None))
        self.lbl_status_features.setText(_translate("MainWindow", "Status:", None))
        self.cb_chart_features_on_off.setText(_translate("MainWindow", "Chart On/Off", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_features), _translate("MainWindow", "Features", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_classification), _translate("MainWindow", "Classification", None))
        self.groupBox_f1.setTitle(_translate("MainWindow", "Finger 1: 0º", None))
        self.groupBox_f2.setTitle(_translate("MainWindow", "Finger 2: 0º", None))
        self.groupBox_f3.setTitle(_translate("MainWindow", "Finger 3: 0º", None))
        self.groupBox_f4.setTitle(_translate("MainWindow", "Finger 4: 0º", None))
        self.groupBox_f5.setTitle(_translate("MainWindow", "Finger 5: 0º", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "General", None))
        self.btn_laser.setText(_translate("MainWindow", "Laser", None))
        self.btn_reset_position.setText(_translate("MainWindow", "Open Hand", None))
        self.btn_close_position.setText(_translate("MainWindow", "Close Hand", None))
        self.btn_send_position.setText(_translate("MainWindow", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_controle_manuel), _translate("MainWindow", "Controle Manuel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Processing", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Input Serial Port", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Output Serial Port", None))
        self.btn_go.setText(_translate("MainWindow", "Go!", None))
        self.pushButton.setText(_translate("MainWindow", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "General Settings", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuFunctions.setTitle(_translate("MainWindow", "Options", None))
        self.lbl_options.setText(_translate("MainWindow", "Options", None))
        self.groupBox.setTitle(_translate("MainWindow", "Training", None))
        self.btn_record_raw_emg.setText(_translate("MainWindow", "Record raw EMG file", None))
        self.label_file_name.setText(_translate("MainWindow", "File: None", None))
        self.lbl_output_name.setText(_translate("MainWindow", "Output:", None))
        self.lbl_output_value.setText(_translate("MainWindow", "None", None))
        self.btn_generate_training_file.setText(_translate("MainWindow", "Generate Training File", None))
        self.btn_load_training_file.setText(_translate("MainWindow", "Load Training File", None))
        self.label.setText(_translate("MainWindow", "Not Trained", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status", None))
        self.label_acquiring_status.setText(_translate("MainWindow", "Acquiring: Off", None))
        self.label_plotting_status.setText(_translate("MainWindow", "Plotting: Off", None))
        self.label_processing_status.setText(_translate("MainWindow", "Processing: Off", None))
        self.label_classification_status.setText(_translate("MainWindow", "Classification: Off", None))
        self.label_channels.setText(_translate("MainWindow", "Channels:", None))
        self.cb_ch1.setText(_translate("MainWindow", "CH1", None))
        self.cb_ch3.setText(_translate("MainWindow", "CH2", None))
        self.cb_ch4.setText(_translate("MainWindow", "CH3", None))
        self.cb_ch2.setText(_translate("MainWindow", "CH4", None))
        self.actionSimples.setText(_translate("MainWindow", "Processamento", None))
        self.actionIn_Plotter.setText(_translate("MainWindow", "In Plotter", None))
        self.actionThread.setText(_translate("MainWindow", "Thread", None))
        self.actionDesativado.setText(_translate("MainWindow", "Desativado", None))
        self.actionStartAcquisition.setText(_translate("MainWindow", "Start Acquisition", None))
        self.actionStart_Recording.setText(_translate("MainWindow", "Start Recording", None))
        self.actionStop_Recording.setText(_translate("MainWindow", "Stop Recording", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionFind_Serial_Port.setText(_translate("MainWindow", "Find Serial Port", None))

