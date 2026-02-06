import unittest
from prototype1 import UVSimulator
import sys
from io import StringIO



class TestUVSimStuff(unittest.TestCase):
    
    def setUp(self):
        self.sim = UVSimulator(memory_size=100)
        
    def test_memory_starts_empty(self):
        self.assertEqual(len(self.sim.memory), 100)
        self.assertTrue(all(val == 0 for val in self.sim.memory))
        
    def test_memory_can_be_smaller(self):
        sim = UVSimulator(memory_size = 50)
        self.assertEqual(len(sim.memory), 50)
        
    def test_loading_test1_file(self):
        self.sim.file_name = "Test1.txt"
        self.sim.load_words( )
        self.assertEqual(self.sim.memory[0], 1007)
        self.assertEqual(self.sim.memory[1],1008)
        
    def test_sentinel_value_stops_loading(self):
        self.sim.file_name = "Test1.txt"
        self.sim.load_words()
        self.assertNotEqual(self.sim.memory[10], -99999)
        
    def test_file_not_found_error(self):
        self.sim.file_name = "fake_file.txt"
        old_stdout = sys.stdout
        sys.stdout =StringIO()
        self.sim.load_words()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("not found",output)
        
    def test_memory_full_check(self):
        sim = UVSimulator(memory_size=5)
        sim.file_name= "Test1.txt"
        old_stdout = sys.stdout
        sys.stdout = StringIO( )
        sim.load_words()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Memory full", output)
        
        
    def test_read_puts_number_in_memory(self):
        self.sim.memory[0] = 1050
        self.sim.memory[ 1] = 4300
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO("42\n")
        sys.stdout =StringIO()
        self.sim.execute_program()
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[50],42)
        
    def test_read_rejects_bad_input(self):
        self.sim.memory[0] = 1050
        self.sim.memory[1] = 4300
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO("99999\n42\n")
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[50], 42)
        
    def test_write_prints_value(self):
        self.sim.memory[0] = 1150
        self.sim.memory[1] = 4300
        self.sim.memory[50]=789
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output= sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("789", output)
        
    def test_write_can_print_zero(self):
        self.sim.memory[0] = 1125
        self.sim.memory[1] = 4300
        self.sim.memory[25] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("0", output)
        
    def test_load_moves_to_accumulator(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 2152
        self.sim.memory[2] = 4300
        self.sim.memory[50] = 1234
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 1234)
        
    def test_load_works_with_negatives(self):
        self.sim.memory[0] = 2030
        self.sim.memory[1] = 2145
        self.sim.memory[2] = 4300
        self.sim.memory[30] = -5678
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[45], -5678)
        
    def test_store_saves_accumulator(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 2160
        self.sim.memory[2] = 4300
        self.sim.memory[50] = 999
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[60], 999)
        
    def test_store_zero_works(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 2175
        self.sim.memory[2] = 4300
        self.sim.memory[50] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[75], 0)
        
    def test_add_two_positives(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3051
        self.sim.memory[2]= 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 10
        self.sim.memory[51] =20
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 30)
        
    def test_add_makes_negative(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3051
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = -50
        self.sim.memory[51] = 20
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], -30)
        
    def test_subtract_basic(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3151
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 100
        self.sim.memory[51] = 30
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 70)
        
    def test_subtract_goes_negative(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3151
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 30
        self.sim.memory[51] = 100
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], -70)
        
    def test_divide_evenly(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3251
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 100
        self.sim.memory[51] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 20)
        
    def test_divide_by_zero_error(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3251
        self.sim.memory[2] = 4300
        self.sim.memory[50] =100
        self.sim.memory[51] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO( )
        self.sim.execute_program()
        output = sys.stdout.getvalue( )
        sys.stdout = old_stdout
        self.assertIn("Division by zero", output)
        
    def test_multiply_normal(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3351
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 12
        self.sim.memory[51] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 60)
        
    def test_multiply_by_zero(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 3351
        self.sim.memory[2] = 2152
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 100
        self.sim.memory[51] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        sys.stdout = old_stdout
        self.assertEqual(self.sim.memory[52], 0)
        
    def test_branch_jumps_correctly(self):
        self.sim.memory[0] = 4005
        self.sim.memory[1] =1150
        self.sim.memory[2] = 4300
        self.sim.memory[5] = 1151
        self.sim.memory[6]=4300
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertNotIn("Enter",output)
        
    def test_branch_to_end(self):
        self.sim.memory[0] = 4002
        self.sim.memory[1] = 1150
        self.sim.memory[2] = 4300
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Halting", output)
        
    def test_branchneg_when_negative(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 4105
        self.sim.memory[2] = 1151
        self.sim.memory[3] = 4300
        self.sim.memory[5] = 1152
        self.sim.memory[6] = 4300
        self.sim.memory[50] = -10
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_branchneg_skips_when_positive(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 4105
        self.sim.memory[2] = 1151
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 10
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_branchzero_when_zero(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 4205
        self.sim.memory[2] = 1151
        self.sim.memory[3] = 4300
        self.sim.memory[5] = 1152
        self.sim.memory[6] = 4300
        self.sim.memory[50] = 0
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_branchzero_skips_when_not_zero(self):
        self.sim.memory[0] = 2050
        self.sim.memory[1] = 4205
        self.sim.memory[2] = 1151
        self.sim.memory[3] = 4300
        self.sim.memory[50] = 5
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    def test_halt_stops_everything(self):
        self.sim.memory[0] =4300
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program( )
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Halting execution",output)
        
    def test_halt_ignores_after(self):
        self.sim.memory[0] = 4300
        self.sim.memory[1] = 1150
        self.sim.memory[2] = 4300
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertNotIn("Enter", output)
        
    def test_bad_opcode_fails(self):
        self.sim.memory[0] = 9999
        old_stdout = sys.stdout
        sys.stdout =StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Invalid opcode",output)
        
    def test_negative_instruction_fails(self):
        self.sim.memory[0] =-1234
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sim.execute_program()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        self.assertIn("Negative instruction", output)


if __name__ =="__main__":
    unittest.main()