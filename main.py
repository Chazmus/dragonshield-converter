#! /bin/python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog, QTextEdit, QComboBox
import pandas as pd

from deckbox_converter import DeckboxConverter


def main():
    app = QApplication(sys.argv)
    converter = CSVConverter()
    sys.exit(app.exec_())


class CSVConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.info_text = None
        self.conversion_type_dropdown = None
        self.convert_button = None
        self.output_csv_field = None
        self.output_csv_label = None
        self.csv_file_display = None
        self.csv_button = None
        self.input_csv = ""
        self.output_csv = ""
        self.init_ui()

    def init_ui(self):
        # Create a "Select CSV file" button
        self.csv_button = QPushButton("Select CSV file", self)
        self.csv_button.clicked.connect(self.open_csv_file)
        self.csv_button.move(10, 10)

        # Create a QTextEdit for displaying the selected csv file name
        self.csv_file_display = QTextEdit(self)
        self.csv_file_display.setGeometry(150, 10, 200, 30)
        self.csv_file_display.setReadOnly(True)

        # Create an "Output CSV path" label
        self.output_csv_label = QLabel("Output CSV path", self)
        self.output_csv_label.move(10, 50)

        # Create a QLineEdit for the output_csv path
        self.output_csv_field = QLineEdit(self)
        self.output_csv_field.setGeometry(120, 50, 280, 30)
        self.output_csv_field.setPlaceholderText("Enter the path of output csv file")

        # Create a "Conversion Type" dropdown
        self.conversion_type_dropdown = QComboBox(self)
        options = ["Deckbox"]
        self.conversion_type_dropdown.addItems(options)
        self.conversion_type_dropdown.move(10, 90)

        # Create a "Convert" button
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_csv)
        self.convert_button.move(10, 130)

        # Create a QTextEdit for displaying the selected csv file name
        self.info_text = QTextEdit(self)
        self.info_text.move(10, 170)
        self.info_text.setReadOnly(True)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle("CSV Converter")
        self.show()

    def open_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.input_csv, _ = QFileDialog.getOpenFileName(self, "Select a CSV file", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if self.input_csv:
            print("Selected file:", self.input_csv)
            self.csv_file_display.setText(self.input_csv)

    def convert_csv(self):
        if not self.input_csv:
            self.info_text.setText("No input csv specified")
            return

        if not self.output_csv_field.text():
            self.info_text.setText("No output path specified")
            return

        self.output_csv = self.output_csv_field.text()
        try:
            # read the input csv file
            df = pd.read_csv(self.input_csv, skiprows=1)
            # Perform the conversion
            # df = your_conversion_function
        except:
            self.info_text.setText("Something went wrong reading the CSV")
            raise

        conversion_type = self.conversion_type_dropdown.currentText()
        converter = None
        if conversion_type == "Deckbox":
            converter = DeckboxConverter()
        elif conversion_type == "TODO":
            # Implement other converters if necessary
            pass
        output_df = converter.convert(df)
        output_df.to_csv(self.output_csv_field.text(), index=False)
        self.info_text.setText("Success!")


if __name__ == '__main__':
    main()
