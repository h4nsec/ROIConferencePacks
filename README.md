**2. Develop a simple application**

### Specification

Staff members are attending a conference. The conference runs for two days and staff members can attend either day, or both days.

- If they&#39;re attending for at least one day they will receive a conference pack.
- If they are attending for two days, they will also receive the bonus pack.
- Not all staff members will be attending.

The application must display:

- the date that the report was run at the top of the list
- a list of attendees and which packs they will receive.

Use the following format to display the information:

Report date: [dd/mm/yyyy]

Attendee: [Surname, first name] Pack/s: [1 or 2 days pack], [both days pack]

Two text files are provided as follows:

The confpack text file has two values on separate lines:

- Line 1 lists what the attendees will receive for attending either one or two days.
- Line 2 lists what the attendees will receive for attending both days.

The employees text file has values separated by commas. Each employee is on a new line.

- Values are surname,firstName,day1,day2
- The fields day1 and day2 will either have a value of Y or no value.

### Tasks

1. Develop an algorithm using pseudocode or a flowchart to:

- access the confpack text file and read the records into an array
- access the employees text file and loop through the records (checking for the end of file)
- use logical operators to select the appropriate conference attendees
- display the required information.
- Code the algorithm in Python, using a suitable library function for the date and appropriate variables and expressions.

