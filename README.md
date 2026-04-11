# UVSim
Group 3 CS-2450-X01-X03-Spring 2026-XLIST | Jorgensen

GitHub: https://github.com/lukesonne06/group3cs2450

Users:

  Zaxbyya - Georgia Allen
  
  millyballing - Milly Balling
  
  jorudolph1 - Jamie Rudolph
  
  lukesonne06 - Luke Sonne

To run our unit tests, type "python unit_tests.py" in your preferred command line

To run our application, type "python main.py" in your preferred command line. To run with a custom color scheme, type "python main.py colorTest.txt" where colorTest.txt is a file containing hex colors, one per line.

A new window with our application will open.

Color scheme:

    To use a custom color scheme, run main.py with a .txt file containing a primary and secondary color.
    e.x. "python main.py colors.txt"
    If no color file is presented, the GUI will default to the UVU colors #4C721D and #FFFFFF
    Our program uses hexadecimal colors, and will only accept such input. A color scheme file must be formatted like so:
    Line 1: #FF22CC
    Line 2: #1122DD

Features:
  
  A window to load in code from a .txt file, can be edited from our application
  
  Can run a BasicML file, outputting to the console and taking in user input at the bottom left of the window
  
  A reset button, allowing you to run multiple programs in one session
  
  A display of the value in the accumulator

  A save file button, allowing you to save your current program to any folder on your system.
  
  An edit toolbar with cut,copy, paste, delete line, and add line buttons for editing your program before running it. A line counter displays how many instructions are loaded out of the maximum 100. 

  Maximum program size increased form 100 to 250 lines

  Memory address now range from 000 yo 249

  Supports new 6-digit word format

  Updates can handle 6-digit values with overflow handling

  Prevents invalid memory access outside the 000-249 range

  Supports multiple files open at the same time within the application

  ## File Format Support

  This application supports both legacy 4-digit and new 6-digit file formats
  - 4-digit format: 2-digit opcode + 2-digit memory address
  - 6-digit format: 3-digit opcode + 3-digit memory address

  Files must contain only one format and cannot mix 4-digit and 6-digit instructions

 ## Memory Constraints

- Maximum of 250 instructions per program
- Valid memory addresses range from 000 to 249
- Programs exceeding this limit will not be loaded or executed

## Overflow Handling

All arithmetic operations support 6-digit values. Overflow behavior follows the same rules as the previous 4-digit implementation.

## Input Validation

- Only hexadecimal values are accepted for color files
- Only valid memory addresses (000–249) are allowed
- Instruction format must match either 4-digit or 6-digit standards


