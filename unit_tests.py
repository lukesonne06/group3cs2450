import unittest
from prototype1 import UVSimulator, detect_file_format, convert_four_digit_word_to_six
import sys
from io import StringIO


class TestUVSimStuff(unittest.TestCase):
    
    def setUp(self):
        # Runs before every test
        # Create a fresh simulator with default memory size
        self.sim = UVSimulator(memory_size=250)

    # Use Case 01

    def test_memory_starts_empty(self):
        # Memory is initialized with zeros
        self.assertEqual(len(self.sim.memory), 250)
        self.assertTrue(all(val == 0 for val in self.sim.memory))
        
    def test_memory_can_be_smaller(self):
        # Simulator should support custom memory sizes
        sim = UVSimulator(memory_size=50)
        self.assertEqual(len(sim.memory), 50)
        
    # Use Case 02
    
    def test_loading_test1_file(self):
        # Loading a valid file should populate memory correctly
        self.sim.file_name = "Test1.txt"
        self.sim.load_words()
        self.assertEqual(self.sim.memory[0], 10007)
        self.assertEqual(self.sim.memory[1], 10008)
        
    def test_sentinel_value_stops_loading(self):
        # Sentinel value should not be stored in memory
        self.sim.file_name = "Test1.txt"
        self.sim.load_words()
        self.assertNotEqual(self.sim.memory[10], -99999)
        
    def test_file_not_found_error(self):
        # Missing file should print an error message
        self.sim.file_name = "fake_file.txt"
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.load_words()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("not found", output)
        
    def test_memory_full_check(self):
        # Loading more words than memory allows should trigger warning
        sim = UVSimulator(memory_size=5)
        sim.file_name = "Test1.txt"
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        sim.load_words()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Memory full", output)
        
    # Use Case 03
        
    def test_read_puts_number_in_memory(self):
        # Read instruction should store user input at operand address
        self.sim.memory[0] = 10050    # Read into memory[50]
        self.sim.memory[1] = 43000    # halt
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO("42\n")
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[50], 42)
        
    def test_read_rejects_bad_input(self):
        # Read should reject invalid input before accepting valid input
        self.sim.memory[0] = 10050
        self.sim.memory[1] = 43000
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO("9999999\n42\n")
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[50], 42)
        
    # Use Case 04

    def test_write_prints_value(self):
        # Write instruction should print memory value
        self.sim.memory[0] = 11050
        self.sim.memory[1] = 43000
        self.sim.memory[50] = 789
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("789", output)
        
    def test_write_can_print_zero(self):
        # Write should correctly print zero values
        self.sim.memory[0] = 11025
        self.sim.memory[1] = 43000
        self.sim.memory[25] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("0", output)
        
    # Use Case 05

    def test_load_moves_to_accumulator(self):
        # Load followed by store should copy value correctly
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 21052
        self.sim.memory[2] = 43000
        self.sim.memory[50] = 1234
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 1234)
        
    def test_load_works_with_negatives(self):
        # Load should handle negative values
        self.sim.memory[0] = 20030
        self.sim.memory[1] = 21045
        self.sim.memory[2] = 43000
        self.sim.memory[30] = -5678
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[45], -5678)
        
    # Use Case 06

    def test_store_saves_accumulator(self):
        # Store should save accumulator to memory
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 21060
        self.sim.memory[2] = 43000
        self.sim.memory[50] = 999
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[60], 999)
        
    def test_store_zero_works(self):
        # Store should correctly save zero
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 21075
        self.sim.memory[2] = 43000
        self.sim.memory[50] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[75], 0)
        
    # Use Case 07

    def test_add_two_positives(self):
        # Load values at 50, add value at 51, store result in 52
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 30051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 10
        self.sim.memory[51] = 20
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 30)
        
    def test_add_makes_negative(self):
        # Addition resulting in a negative value
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 30051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = -50
        self.sim.memory[51] = 20
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], -30)
     
    # Use Case 08

    def test_subtract_basic(self):
        # Subtract should compute accumulator - operand
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 31051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 100
        self.sim.memory[51] = 30
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 70)
        
    def test_subtract_goes_negative(self):
        # Subtraction resulting in a negative value
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 31051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 30
        self.sim.memory[51] = 100
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], -70)
        
    # Use Case 09

    def test_divide_evenly(self):
        # Divide should perform integer division
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 32051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 100
        self.sim.memory[51] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 20)
        
    def test_divide_by_zero_error(self):
        # Division by zero should print an error and halt execution
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 32051
        self.sim.memory[2] = 43000
        self.sim.memory[50] = 100
        self.sim.memory[51] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Division by zero", output)
        
    # Use Case 10

    def test_multiply_normal(self):
        # Multiply should compute product correctly
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 33051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 12
        self.sim.memory[51] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 60)
        
    def test_multiply_by_zero(self):
        # Multiplication by zero should result in zero
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 33051
        self.sim.memory[2] = 21052
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 100
        self.sim.memory[51] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 0)
        
    # Use Case 11

    def test_branch_jumps_correctly(self):
        # Branch should jump to instruction 5, skipping input instruction
        self.sim.memory[0] = 40005
        self.sim.memory[1] = 11050
        self.sim.memory[2] = 43000
        self.sim.memory[5] = 11051
        self.sim.memory[6] = 43000
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertNotIn("Enter", output)
        
    def test_branch_to_end(self):
        # Branching directly to halt should stop execution
        self.sim.memory[0] = 40002
        self.sim.memory[1] = 11050
        self.sim.memory[2] = 43000
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Halting", output)
        
    # Use Case 12

    def test_branchneg_when_negative(self):
        # Branching should jump when accumulator is negative
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 41005
        self.sim.memory[2] = 11051
        self.sim.memory[3] = 43000
        self.sim.memory[5] = 11052
        self.sim.memory[6] = 43000
        self.sim.memory[50] = -10
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_branchneg_skips_when_positive(self):
        # Branchneg should not jump when accumulator is positive
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 41005
        self.sim.memory[2] = 11051
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 10
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    # Use Case 13

    def test_branchzero_when_zero(self):
        # Branchzero should jump when accumulator equals zero
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 42005
        self.sim.memory[2] = 11051
        self.sim.memory[3] = 43000
        self.sim.memory[5] = 11052
        self.sim.memory[6] = 43000
        self.sim.memory[50] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_branchzero_skips_when_not_zero(self):
        # Branchzero should not jump when accumulator is nonzero
        self.sim.memory[0] = 20050
        self.sim.memory[1] = 42005
        self.sim.memory[2] = 11051
        self.sim.memory[3] = 43000
        self.sim.memory[50] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    # Use Case 14
        
    def test_halt_stops_everything(self):
        # Halt should immediately stop execution
        self.sim.memory[0] = 43000
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Halting execution", output)
        
    def test_halt_ignores_after(self):
        # Instructions after halt should never execute
        self.sim.memory[0] = 43000
        self.sim.memory[1] = 10050
        self.sim.memory[2] = 43000
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertNotIn("Enter", output)
        
    # Use Case 15

    def test_bad_opcode_fails(self):
        # Invalid opcode should produce an error
        self.sim.memory[0] = 99000    # opcode 99 is invalid, operand 000 is valid
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Invalid opcode", output)
        
    def test_negative_instruction_fails(self):
        # Negative instruction values should halt execution with error
        self.sim.memory[0] = -1234
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Negative instruction", output)

    # Use Case 16 - Backward Compatibility

    def test_detect_four_digit_format(self):
        # Words within 4-digit range should be detected as four
        words = ["1099", "2007", "4300"]
        self.assertEqual(detect_file_format(words), "four")

    def test_detect_six_digit_format(self):
        # Words outside 4-digit range should be detected as six
        words = ["010099", "020007", "043000"]
        self.assertEqual(detect_file_format(words), "six")

    def test_convert_halt_instruction(self):
        # +4300 should become +043000
        self.assertEqual(convert_four_digit_word_to_six(4300), 43000)

    def test_convert_negative_data_unchanged(self):
        # Negative values should pass through untouched
        self.assertEqual(convert_four_digit_word_to_six(-50), -50)

    def test_four_digit_file_loads_correctly(self):
        # A 4-digit program should load the same as its 6-digit equivalent
        sim_four = UVSimulator(memory_size=250)
        sim_four.load_from_text("2007 3008 4300 0000 0000 0000 0000 0014 0006")
        sim_six = UVSimulator(memory_size=250)
        sim_six.load_from_text("020007 030008 043000 000000 000000 000000 000000 000014 000006")
        self.assertEqual(sim_four.memory[:9], sim_six.memory[:9])

    def test_old_sentinel_stops_loading(self):
        # Old sentinel -99999 should stop loading just like -999999
        sim = UVSimulator(memory_size=250)
        sim.load_from_text("43000 -99999 10099")
        self.assertEqual(sim.memory[1], 0)


if __name__ == "__main__":
    unittest.main()
