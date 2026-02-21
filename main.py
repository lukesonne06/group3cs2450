import tkinter as tk
from tkinter import filedialog
import threading
import queue
import sys
from prototype1 import UVSimulator    # Import UVUSimlator class


class WindowSimulator:

    def __init__(self, win):
        # Get the file name from the command-line arguments
        # sys.argv[1] is the first argument after the script name
        #file_name = sys.argv[1]

        self.main_tkinter_window =win
        self.main_tkinter_window.title("UVSim")
        self.main_tkinter_window.configure(bg ="#f0f0f0")

        self.main_tkinter_window.geometry("800x600")
        self.messaging_queue=queue.Queue()

        self.inputting_main_windowueue =queue.Queue()
        self.uv_sim_instanceRunning=False
        self.widget_creator()
        self.main_tkinter_window.after(100 ,self.queue_checker)


    def widget_creator(self):
                

                green_header =tk.Frame(self.main_tkinter_window ,bg="#5a9e47",height=60)
                
                green_header.pack(fill="x")
                green_header.pack_propagate(False )

                tk.Label(green_header ,
                    text="UVSim",font= ("Arial",18,"bold"),
                    bg="#5a9e47" ,fg="white"
                    ).pack(side ="left",padx=15,pady=10)
                button_row_frame=tk.Frame(self.main_tkinter_window,bg ="#f0f0f0",pady=6)
                button_row_frame.pack(fill ="x",padx=10)

                self.loading_button =tk.Button(button_row_frame ,text="Load File",
                    font=("Arial" ,10),bg="#5a9e47",fg="white",
                    padx=10 ,pady=4,relief="flat",command=self.file_picker)
                
                self.loading_button.pack(side="left" ,padx=(0,8))

                self.go_button=tk.Button(button_row_frame,text ="Run",
                                     
                    font=("Arial",10) ,bg="#5a9e47",fg="white",
                    padx =10,pady=4,relief ="flat",command=self.sim_starter)
                self.go_button.pack(side ="left",padx=(0,8))

                self.resetting_button =tk.Button(button_row_frame ,text="Reset",
                                         
                    font=("Arial",10),bg ="#888888",fg="white",
                    padx=10,pady =4,relief="flat",command=self.clear_everything)
                
                self.resetting_button.pack(side ="left")
                main_body_frame =tk.Frame(self.main_tkinter_window ,bg="#f0f0f0")
                main_body_frame.pack(fill="both" ,expand=True,padx=10,pady=(0,10))
                left_panel_frame=tk.Frame(main_body_frame ,bg="#f0f0f0")
                left_panel_frame.pack(side="left" ,fill="both",expand =True,padx=(0,8))
                right_panel_frame =tk.Frame(main_body_frame,bg="#f0f0f0")
                right_panel_frame.pack(side ="right",fill="both",expand=True)
                acc_and_entry_frame=tk.Frame(left_panel_frame ,bg="#f0f0f0")
                acc_and_entry_frame.pack(fill ="x",pady=(0,8))
                tk.Label(acc_and_entry_frame ,text="Accumulator:",font=("Arial",11),bg="#f0f0f0").pack(side="left")

                self.accumulator_box =tk.StringVar()

                self.accumulator_box.set("0")

                tk.Entry(acc_and_entry_frame ,textvariable=self.accumulator_box,
                    font=("Courier New",11) ,width=12,
                    state="readonly" ,relief="solid",bd=1).pack(side="left" ,padx=(8,0))
                
                tk.Label(left_panel_frame ,text="Console:",font=("Arial",11),
                    bg ="#f0f0f0",anchor="w").pack(fill="x")

                self.outputting_box =tk.Text(left_panel_frame,
                    font=("Courier New" ,10),bg="white",fg="black",
                        relief ="solid",bd=1,state="disabled",wrap="word")

                self.outputting_box.pack(fill ="both",expand=True)
                console_scrollbar=tk.Scrollbar(self.outputting_box )
                console_scrollbar.pack(side ="right",fill="y")

                self.outputting_box.config(yscrollcommand =console_scrollbar.set)
                console_scrollbar.config(command=self.outputting_box.yview )

                self.outputting_box.tag_config("output" ,foreground= "green")

                self.outputting_box.tag_config("error",foreground ="red")


                self.outputting_box.tag_config("info" ,foreground="blue")

                self.outputting_box.tag_config("normal" ,foreground= "black")

                self.typeRow =tk.Frame(left_panel_frame,bg="#f0f0f0")

                self.typeRow.pack(fill ="x",pady=(6,0))

                tk.Label(self.typeRow ,text="Enter value:",font=("Arial",10),bg="#f0f0f0").pack(side ="left")

                self.user_typed_string =tk.StringVar()

                self.int_entry_box=tk.Entry(self.typeRow ,textvariable=self.user_typed_string,
                    font=("Courier New" ,10),width=10,relief="solid",bd=1)

                self.int_entry_box.pack(side ="left",padx=6)

                self.int_entry_box.bind("<Return>" ,self.input_sender)

                tk.Button(self.typeRow ,text="Submit",font=("Arial",10),
                          
                    bg ="#5a9e47",fg="white",padx=8,pady=2,
                        relief="flat" ,command=self.input_sender).pack(side="left")

                self.typeRow.pack_forget()

                tk.Label(right_panel_frame ,text="Program: (enter or paste here)",
                    font=("Arial",11) ,bg="#f0f0f0",anchor="w").pack(fill="x")

                self.code_box=tk.Text(right_panel_frame ,
                    font=("Courier New",10) ,bg="white",fg="black",
                    relief="solid" ,bd=1,wrap="none",width=22)

                self.code_box.pack(fill ="both",expand=True)
                code_editor_scrollbar =tk.Scrollbar(self.code_box)
                code_editor_scrollbar.pack(side="right" ,fill="y")

                self.code_box.config(yscrollcommand=code_editor_scrollbar.set )
                code_editor_scrollbar.config(command =self.code_box.yview)

                self.code_box.insert("end" ,"+1007\n+1008\n+2007\n+3008\n+2109\n+1109\n+4300\n+0000\n+0000\n+0000\n-99999")
                tk.Label(right_panel_frame ,text="One instruction per line. End with -99999.",
                         
                    font=("Arial",8) ,bg="#f0f0f0",fg="#888888").pack(anchor="w")







    def file_picker(self):
        file_dialog_path =filedialog.askopenfilename(
            title="Open BasicML File",
                filetypes=[("Text files","*.txt") ,("All files","*.*")])
        
        if not file_dialog_path:
                return
        try:
            with open(file_dialog_path ,"r") as f:
                    loaded_file_contents =f.read()
            self.code_box.delete("1.0" ,"end")

            self.code_box.insert("end" ,loaded_file_contents)

            self.box_print(f"Loaded: {file_dialog_path}\n" ,"info")

        except:
                self.box_print("Couldnt open that file\n" ,"error")


    def sim_starter(self):
            if self.uv_sim_instanceRunning ==True:

                self.box_print("Already running.\n" ,"error")

                return
            program_editor_text_pull =self.code_box.get("1.0","end").strip()
            if not program_editor_text_pull:
                    self.box_print("Nothing to run.\n","error")

                    return
            self.output_wiper()

            self.box_print("Starting...\n" ,"info")

            # Create the simulator instance using the input file

            self.uv_sim_instance =UVSimulator(memory_size=100)
            # Take user input for program words and load them into memory

            self.uv_sim_instance.load_from_text(program_editor_text_pull )
            # Execute the program stored in memory

            self.uv_sim_instanceRunning=True

            self.go_button.config(state ="disabled")

            background_sim_thread =threading.Thread(target=self.background_running ,daemon=True)
            background_sim_thread.start()


    def background_running(self):

        save_stdout_before_replace =sys.stdout
        save_stdin_before_replace=sys.stdin
        sys.stdout =PrintCallInterceptor(self.messaging_queue)

        sys.stdin =InputInterceptor(self.inputting_queue ,self.messaging_queue)

        try:
                self.uv_sim_instance.execute_program()
        except Exception as crash_exeption_object:

            self.messaging_queue.put(("error" ,f"Crashed: {crash_exeption_object}\n"))

        finally:
                sys.stdout=save_stdout_before_replace
                sys.stdin =save_stdin_before_replace

                self.messaging_queue.put(("done",""))


    def queue_checker(self):
        try:
                while True:
                    message_queue_object_exeption ,message_content=self.messaging_queue.get_nowait()
                    if message_queue_object_exeption =="print":
                        self.box_print(message_content ,"normal")

                    elif message_queue_object_exeption=="output":
                            self.box_print(message_content,"output")

                    elif message_queue_object_exeption =="error":
                        self.box_print(message_content ,"error")

                    elif message_queue_object_exeption=="info":
                            self.box_print(message_content,"info")

                    elif message_queue_object_exeption =="need_input":
                        self.typeRow.pack(fill="x" ,pady=(6,0))


                        self.int_entry_box.focus()

                    elif message_queue_object_exeption=="done":
                        self.uv_sim_instanceRunning =False

                        self.go_button.config(state="normal")

                        self.typeRow.pack_forget()

                        self.box_print("Done.\n" ,"info")

        except queue.Empty:
            pass
        self.main_tkinter_window.after(100 ,self.queue_checker)




    def input_sender(self ,event=None):
            user_string =self.user_typed_string.get().strip()

            try:
                user_int =int(user_string)
                if user_int < -9999 or user_int > 9999:
                        self.box_print("Need a 4 digit integer.\n" ,"error")
                        return
            except ValueError:
                    self.box_print("Thats not an integer.\n","error")
                    return
            self.user_typed_string.set("")

            self.typeRow.pack_forget()

            self.box_print(f"Got: {user_int}\n" ,"info")

            self.inputting_queue.put(user_string +"\n")


    def clear_everything(self):
        if self.uv_sim_instanceRunning ==True:
                
                self.box_print("Cant reset while running.\n" ,"error")
                return
        self.output_wiper()


        self.accumulator_box.set("0")

        self.typeRow.pack_forget()
        
        self.box_print("Reset.\n" ,"info")


    def box_print(self ,txt,colorTag ="normal"):
            self.outputting_box.config(state="normal")

            self.outputting_box.insert("end" ,txt,colorTag)

            self.outputting_box.see("end")

            self.outputting_box.config(state ="disabled")


    def output_wiper(self):

        self.outputting_box.config(state ="normal")

        self.outputting_box.delete("1.0","end")


        self.outputting_box.config(state="disabled")


class PrintCallInterceptor:

    def __init__(self ,q):
            
            self.q=q

    def write(self ,s):

        if not  s.strip():
                return
        if "Error" in s  or "Invalid" in s or "Division" in  s or "Negative" in s:
                self.q.put(("error" ,s)) 


        elif "Halting" in  s:

            self.q.put(("info" ,s))
        else:
                self.q.put(("output",s))

    def flush(self): 
        pass


class InputInterceptor:

    def __init__(self ,q,messages):
        self.q=q
        self.messages =messages

    def readline(self):
            self.messages.put(("need_input" ,""))
            return   self.q.get()





# This confirms main() only runs when this file is executed
def main():
    main_window =tk.Tk()

    WindowSimulator(main_window)
    main_window.mainloop()


if __name__ =="__main__":
    main()



