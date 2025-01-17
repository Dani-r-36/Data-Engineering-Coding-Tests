# [TODO]: step 1
# Update the is_log_line function below to skip lines that are not valid log lines.
# Valid log lines have a timestamp, error type, and message. For example, lines 1, 3,
# 7 and 37 are all examples of lines (from sample.log) that would be filtered out.
# There's no perfect way to do this: just decide what you think is reasonable to get
# the test to pass. The only thing you are not allowed to do is filter out log lines
# based on the exact row numbers you want to remove.
from datetime import datetime
import time

INFO ="INFO"
TRACE = "TRACE"
WARNING = "WARNING"

def is_log_line(line):
    """sorts data and checks if required data is in list"""
    formated_row =[]
    row = line.split()
    if len(row) > 3:
        formated_datetime, log_level, message = formating(row)
        formated_row.append(formated_datetime)
        formated_row.append(log_level)
        formated_row.append(message)
        if len(formated_row) == 3 and formated_datetime != "":
            return True
    return False

def formating(row):
    """sorts data line to respective variables"""
    formated_datetime = ""
    date_string = f"{row[0]} {row[1]}"
    try:
        datetime_object = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S')
        formated_datetime = datetime_object.strftime('%d/%m/%y %H:%M:%S')
    except Exception as err:
        print(err)
        print("Not in datetime format")
    log_level = row[2]
    message = " ".join(row[3:])
    return formated_datetime, log_level, message

def get_dict(line):
    """checks sorted variables and assigns to dict"""
    row = line.split()
    formated_datetime, log_level, message = formating(row)
    if log_level != INFO or log_level != TRACE or log_level != WARNING:
        print("Invalid log_level")
    data = {
            "timestamp": formated_datetime,
            "log_level": log_level,
            "message": message,
        }
    return data


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))
        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
