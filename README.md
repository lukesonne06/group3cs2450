# UVSim
Group 3 CS-2450-X01-X03-Spring 2026-XLIST | Jorgensen

GitHub: https://github.com/lukesonne06/group3cs2450

Users:

  Zaxbyya - Georgia Allen
  
  millyballing - Milly Balling
  
  jorudolph1 - Jamie Rudolph
  
  lukesonne06 - Luke Sonne

**Introduction:**
  The BasicML Application is a graphical program to load,edit, and execute BasicML code. It provides a user-friendly interfface for writing and testing       machine-level instructions, with support for both legacy and extended insturction format.

 **Getting Started**
  Running the application
  To run our unit tests, type "python unit_tests.py" in your preferred command line

  To run our application, type "python main.py" in your preferred command line. To run with a custom color scheme, type "python main.py colorTest.txt" where colorTest.txt is a file containing hex colors, one per line.

**User Interface Overview**

  When application launches, a new window will appear containing:
    - Code Editor Window-Load and edit BAsicML programs
    - Console Output Area-Displays program output
    - User Input Field-Accepts input during execution
    - Toolbar-Editing and file management tools
    - Accumulator Display-Shows the current accumulator value
    - Line Counter-Displays the number of instructions used

**Features & Functionality**

  *File Management:*
    - Load File: import a .txt file containing BasicML instructions
    - Save File: Save your current program to any directory
    - Multiple Files: Open and work with multiple files simultaneously
 
*Code Editing Tools:*

   The application includes a toolbar with the following opotions:
  - Cut
  - Copy
  - Paste
  - Delete Line
  - Add Line
  The editor also displays how many instructions are currently loaded.

*Program Execution*

  - Run BasicML programs directly within the application
  - View output in the sonsole panel
  - Provide input via the input field
 
*Reset Function*

  - The Reset button clears the current program state
  - Allows multiple programs to be run in a single session

*Accumulator Display*
 
  - Displays the current value of the accumulator in real time during execution
 
**Instruction Format Support**
  
This application supports two instruction formats:
 
  4-Digit Format (Legacy)
  - Structure
  -     00AA
  -     00 = Opcode
  -     AA = Memory
 
  6-Digit Format (Extended)
  -Structure
  000AAA
  -     000 = Opcode
  -     AAA = Memeory Address

**Important notes**

  - Files must use only one format (4-digit or 6-digit)
  - Mixing formats within a single file is not allowed
 
**Memory Constraints**
  
  -     Maximum program size: 250 instructions
  -     Valid memory address: 000-249

Programs that exceed these limits will not be loaded or executed

Arithmetic and Overglow Handling
  
  - Supports operations on 6-ditit values
  - Overflow behaivor follows the same rules as the origional 4-digit implementation

**Input Validation**
 
  The application enforces strict validation rules:

  *Color Files*

  - Must contain valid hexadecimal values only
  - Exavtly one color per line
  
*Memory Address*

  -     Must be within the 000-249 range

*Instruction Format*

  - Must match either 4-digit or 6-digit format
  - Mixed formats are not permitted

**Error Handling**
  
  The application prevents
  
  - Invalid memory access outsid allowed range
  - Incorrect instruction formats
  - Impoper color file inputs

**Summary**
The BasicML Application provides:

  - A complete enviromente for editing and running BasicML programs
  - Support for both legacy and extended instruction formats
  - Robust validation and error handling
  - Customizable user interface through color schemes

