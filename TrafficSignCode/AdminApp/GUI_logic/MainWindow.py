import yaml
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from GUI.MainWindow.MainWindow import Ui_MainWindow

from DataExchange.DataExchange import DataExchange
from DataExchange.Connection import Connection

from GUI_logic.SetSpeedLimitDialog import SetSpeedLimitDialog
from GUI_logic.SetAliasDialog import SetAliasDialog
from GUI_logic.DetailsDialog import DetailsDialog
from GUI_logic.SetWarningDialog import SetWarningDialog

# This class is responsible for:
#  - Defining the logic behind the "Traffic sign control application" main window
#  - Displaying the GUI of the window
#  - Displaying a list of available devices
#  - Displaying the appropriate dialog windows and handling their return data
class MainWindow(QMainWindow):

    # Constructor method
    def __init__(self):
        super().__init__()
        # Load the user defined device aliases
        self.LoadKnownDevices()
        # Create a UI object
        self.ui = Ui_MainWindow()
        # Setup and display the default GUI of the window
        self.ui.setupUi(self)
        # Setup the button functionality
        self.SetupButtons()
        # Alter the GUI as needed
        self.AdjustGUI()
        # Create a DataExchange() object
        self.dataExchange = DataExchange()
        # Initially update the device list
        self.UpdateDeviceList()

    # Connects the buttons to their appropriate methods
    def SetupButtons(self):
        self.ui.SetSpeedLimitButton.clicked.connect(self.ShowSetSpeedLimitDialog)
        self.ui.RefreshButton.clicked.connect(self.UpdateDeviceList)
        self.ui.SetListEntryAliasButton.clicked.connect(self.ShowSetAliasDialog)
        self.ui.DetailsButton.clicked.connect(self.ShowDetailsDialog)
        self.ui.SetWarningButton.clicked.connect(self.ShowSetWarningDialog)

    # Alters the required GUI elements
    def AdjustGUI(self):
        # Set the background color of the selected device from the list
        self.setStyleSheet(
            """ QListWidget:item:selected:active {
                                     background: dodgerblue;
                                     color: white;
                                }
                                QListWidget:item:selected:!active {
                                     background: dodgerblue;
                                     color: white;
                                }
                                """
        )
        # Set the appropriate window icon
        self.setWindowIcon(QIcon("./GUI/images/icon.png"))

    # Requests information from the web server and updates the devices in the displayed device list
    def UpdateDeviceList(self):
        # Request available devices from the web server
        self.dataExchange.GetDevices()
        # Disable and clear the currently displayed list of devices
        self.ui.DeviceList.setDisabled(True)
        self.ui.DeviceList.clear()
        # Generate the new display list with the appropriate device aliases
        displayList = self.GenerateDeviceList()
        # Add each device to the displayed list
        for device in displayList:
            self.ui.DeviceList.addItem(device)
        # Enable the displayed list
        self.ui.DeviceList.setDisabled(False)

    # Generates the device list that is to be displayed to the user
    def GenerateDeviceList(self):
        displayList = []
        # Loop through every device in the list
        for device in Connection().deviceList:
            # If the device is new and the IMEI is unknown:
            if device not in Connection().knownDevices.values():
                # Add it to the list of known devices
                Connection().knownDevices[device] = device  # Alias == IMEI (initially)

            # Find the device alias from its IMEI and add it to the list
            # (Search dictionary by value)
            displayList.append(
                list(Connection().knownDevices.keys())[
                    list(Connection().knownDevices.values()).index(device)
                ]
            )

        # Return the updated display list
        return displayList

    # Loads every known device alias from the user's .yaml file
    def LoadKnownDevices(self):
        # Open the DeviceAliases.yaml file as a readable stream
        with open("./GUI_logic/DeviceAliases.yaml", "r") as stream:
            try:
                # Convert the contents of the file to a python object
                loaded = yaml.safe_load(stream)
                # Add every loaded entry to the knownDevices dictionary
                for key, value in loaded.items():
                    Connection().knownDevices[key] = value

            # File loading failed
            except yaml.YAMLError as exc:
                print(exc)

    # Saves every known device alias to the user's .yaml file
    def SaveKnownDevices(self):
        # Open the DeviceAliases.yaml file as a writeable stream
        with open("./GUI_logic/DeviceAliases.yaml", "w", encoding="utf-8") as outfile:
            # Dump the contents of the knownDevices dictionary to the file in utf-8 format
            yaml.dump(
                Connection().knownDevices,  # Known devices dictionary
                outfile,  # Output stream
                default_flow_style=False,  # Save collection in block style
                allow_unicode=True,  # Save characters in unicode instead of binary
            )

    # Displays the "Set speed limit sign" dialog window for the selected device
    def ShowSetSpeedLimitDialog(self):
        # Get the device currently selected by the user
        selectedDevice = self.GetSelectedDevice()
        # If a device is selected:
        if selectedDevice:
            # Create a SetSpeedLimitDialog() object
            self.setSpeedLimitDialog = SetSpeedLimitDialog(selectedDevice)
            # Display the dialog and save the return result
            result = self.setSpeedLimitDialog.exec_()
            # If the dialog was rejected (The application lost connection to the server):
            if result == QDialog.Rejected:
                # Display an error message
                QMessageBox.critical(
                    self,
                    "Error",
                    "Lost connection to the web server, closing...",
                    QMessageBox.Ok,
                )
                # Exit the application
                self.Exit()
        # If a device is not selected:
        else:
            # Do nothing
            pass

    # Displays the "Set warning sign" dialog window for the selected device
    def ShowSetWarningDialog(self):
        # Get the device currently selected by the user
        selectedDevice = self.GetSelectedDevice()
        # If a device is selected:
        if selectedDevice:
            # Create a SetWarningDialog() object
            self.setWarningDialog = SetWarningDialog(selectedDevice)
            # Display the dialog and save the return result
            result = self.setWarningDialog.exec_()
            # If the dialog was rejected (The application lost connection to the server):
            if result == QDialog.Rejected:
                # Display an error message
                QMessageBox.critical(
                    self,
                    "Error",
                    "Lost connection to the web server, closing...",
                    QMessageBox.Ok,
                )
                # Exit the application
                self.Exit()
        # If a device is not selected:
        else:
            # Do nothing
            pass

    # Displays the "Set alias" dialog window for the selected device
    def ShowSetAliasDialog(self):
        # Get the device currently selected by the user
        selectedDevice = self.GetSelectedDevice()
        # If a device is selected:
        if selectedDevice:
            # Create a SetAliasDialog() object
            self.setAliasDialog = SetAliasDialog(selectedDevice)
            # Display the dialog and save the return result
            result = self.setAliasDialog.exec_()
            # If the dialog was accepted (The user changed an alias):
            if result == QDialog.Accepted:
                # Update the displayed device list to account for the change
                self.UpdateDeviceList()
        # If a device is not selected:
        else:
            # Do nothing
            pass

    # Displays the "Device details" dialog window for the selected device
    def ShowDetailsDialog(self):
        # Get the device currently selected by the user
        selectedDevice = self.GetSelectedDevice()
        # If a device is selected:
        if selectedDevice:
            # Get the IMEI for the alias from the knownDevices dictionary
            IMEI = Connection().knownDevices[selectedDevice]
            # Request details for the selected device
            incoming = self.dataExchange.GetDeviceDetails(IMEI)
            # If there is a problem with the server connection:
            if incoming == "nocon" or incoming == "timeout":
                # Display an error message
                QMessageBox.critical(
                    self,
                    "Error",
                    "Lost connection to the web server, closing...",
                    QMessageBox.Ok,
                )
                # Exit the application
                self.Exit()
            # If there is a problem with the device connection:
            elif incoming == "nosend":
                # Display a warning message
                QMessageBox.warning(
                    self, "Error", "Couldn't send message to device", QMessageBox.Ok
                )
            elif incoming == "notfound":
                # Display a warning message
                QMessageBox.warning(
                    self, "Error", "Requested device not found", QMessageBox.Ok
                )
            elif incoming == "noresp":
                # Display a warning message
                QMessageBox.warning(
                    self, "Error", "Device didn't respond", QMessageBox.Ok
                )
            else:
                # Split the response into separate items
                details = incoming.split(" ")
                # Convert the status to a human-readable message
                status = self.ConvertStatus(details[0])
                # Convert the value to a human-readable message
                value = self.ConvertValue(details[1])

                # Create a DetailsDialog() object
                self.detailsDialog = DetailsDialog(selectedDevice, IMEI, status, value)
                # Display the dialog
                self.detailsDialog.exec_()
                return True
        # If a device is not selected:
        else:
            # Do nothing
            pass

    # Converts the 3-letter status into a human-readable string
    def ConvertStatus(self, status):
        if status == "unk":
            return "No information"
        elif status == "spd":
            return "Speed limit"
        elif status == "wrn":
            return "Warning"

    # Converts the 3-letter value into a human-readable string
    def ConvertValue(self, value):
        if value == "stp":
            return "Stop sign"
        elif value == "gnr":
            return "General warning"
        elif value == "tfl":
            return "Traffic light"
        elif value == "nen":
            return "No entry"
        elif value == "fon":
            return "Forward only"
        elif value == "lon":
            return "Left only"
        elif value == "ron":
            return "Right only"
        elif value == "unk":
            return "No information"
        else:
            return value

    # Returns the currently selected device from the list
    def GetSelectedDevice(self):
        # Get a list of selected items (Should be just 1)
        deviceList = self.ui.DeviceList.selectedItems()
        # If a device is selected:
        if len(deviceList) > 0:
            # Return the selected device alias
            return deviceList[0].text()
        # If a device is not selected:
        else:
            return None

    # Handles key press shortcuts
    def keyPressEvent(self, event):
        # If [ESC] is clicked -> close the window
        if event.key() == Qt.Key_Escape:
            # Exit the application
            self.Exit()

    # Saves device aliases and closes the application
    def Exit(self):
        # Save all new and previous device aliases to the file
        self.SaveKnownDevices()
        # Close the connection
        Connection().Close()
        # Close the GUI window
        self.close()
