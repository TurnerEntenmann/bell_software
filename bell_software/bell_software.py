import re, subprocess
import customtkinter as ctk
from tkinter import StringVar

cr=10
px=10
py=10
entry_width=100

def main():
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.geometry("600x500")
    root.title("Bell's Inequality")
    root.resizable(False,False)
    
    # vars for counts
    global a_counts_var, b_counts_var, coin_var
    
    # what the run button does
    def run_command():
        run_time = float(time_var.get())
        coin_time = float(coin_var.get())
        # run counter.py and get count numbers back
        text = subprocess.check_output(["python", "counter.py", str(run_time), str(coin_time)])
        vals = re.findall(r'\d+', text.decode('utf-8'))

        # update vars
        a_counts_var.set(vals[0])
        a_cps_var.set(str(float(vals[0]) / run_time))
        b_counts_var.set(vals[1])
        b_cps_var.set(str(float(vals[1]) / run_time))
        coin_var.set(vals[2])
        coin_ps_var.set(str(float(vals[2]) / run_time))
    
    # frame for everything
    page_frame = ctk.CTkFrame(root, corner_radius=cr)
    page_frame.grid(row=0,column=0, padx=px, pady=py)
    # frame for the inputs
    input_frame = ctk.CTkFrame(page_frame, corner_radius=cr)
    input_frame.grid(row=0, column=0, padx=px, pady=py)
    # inputs
    time_lab = ctk.CTkLabel(input_frame, text="run time (s):")
    time_lab.grid(row=0, column=0, padx=px, pady=py)
    time_var=StringVar()
    time_var.set("10")
    time_ent = ctk.CTkEntry(input_frame, textvariable=time_var, placeholder_text="merp")
    time_ent.grid(row=0, column=1, padx=px, pady=py)
    
    coin_lab = ctk.CTkLabel(input_frame, text="coincidence window (ps):")
    coin_lab.grid(row=1, column=0, padx=px, pady=py)
    coin_var=StringVar()
    coin_var.set("3")
    coin_ent = ctk.CTkEntry(input_frame, textvariable=coin_var, placeholder_text="merp")
    coin_ent.grid(row=1, column=1, padx=px, pady=py)
    
    
    # run button
    run_frame = ctk.CTkFrame(input_frame, corner_radius=cr, width=entry_width)
    run_frame.grid(row=2, column=0, padx=px, pady=py)        
        
    run_button = ctk.CTkButton(run_frame, text="run", command=run_command)
    run_button.grid(row=0, column=0)
    
    # a / b frame
    ab_frame = ctk.CTkFrame(input_frame, corner_radius=cr, width=entry_width)
    ab_frame.grid(row=3, column=0, padx=px, pady=py)
    
    a_lab = ctk.CTkLabel(ab_frame, text="A")
    a_lab.grid(row=0, column=1, padx=px, pady=py)
    b_lab = ctk.CTkLabel(ab_frame, text="B")
    b_lab.grid(row=0, column=2, padx=px, pady=py)
    
    counts_lab = ctk.CTkLabel(ab_frame, text="Counts")
    counts_lab.grid(row=1, column=0, padx=px, pady=py)
    cps_lab = ctk.CTkLabel(ab_frame, text="Counts / sec")
    cps_lab.grid(row=2, column=0, padx=px, pady=py)
    
    # counts and counts / sec
    a_counts_var = StringVar()
    a_counts_var.set("0")
    a_counts_lab = ctk.CTkEntry(ab_frame, textvariable=a_counts_var, state="readonly", width=entry_width)
    a_counts_lab.grid(row=1, column=1, padx=px, pady=py)
    
    b_counts_var = StringVar()
    b_counts_var.set("0")
    b_counts_lab = ctk.CTkEntry(ab_frame, textvariable=b_counts_var, state="readonly", width=entry_width)
    b_counts_lab.grid(row=1, column=2, padx=px, pady=py)
    
    a_cps_var = StringVar()
    a_cps_var.set("0")
    a_cps_lab = ctk.CTkEntry(ab_frame, textvariable=a_cps_var, state="readonly", width=entry_width)
    a_cps_lab.grid(row=2, column=1, padx=px, pady=py)
    
    b_cps_var = StringVar()
    b_cps_var.set("0")
    b_cps_lab = ctk.CTkEntry(ab_frame, textvariable=b_cps_var, state="readonly", width=entry_width)
    b_cps_lab.grid(row=2, column=2, padx=px, pady=py)
    

    # coincidences
    coin_frame = ctk.CTkFrame(input_frame, corner_radius=cr)
    coin_frame.grid(row=4, column=0, padx=px, pady=py, sticky="w")
    
    coin_lab = ctk.CTkLabel(coin_frame, text="Coincidences")
    coin_lab.grid(row=0, column=0, padx=px, pady=py)
    coin_ps_lab = ctk.CTkLabel(coin_frame, text="Coincidences / sec")
    coin_ps_lab.grid(row=1, column=0, padx=px, pady=py)
    
    coin_var = StringVar()
    coin_var.set("0")
    coin_var_lab = ctk.CTkEntry(coin_frame, textvariable=coin_var, state="readonly", width=entry_width)
    coin_var_lab.grid(row=0, column=1, padx=px, pady=py)
    
    coin_ps_var = StringVar()
    coin_ps_var.set("0")
    coin_ps_var_lab = ctk.CTkEntry(coin_frame, textvariable=coin_ps_var, state="readonly", width=entry_width)
    coin_ps_var_lab.grid(row=1, column=1, padx=px, pady=py)

    # main page
    root.mainloop()





main()







# counter.py needs runtime (s) and coincidence window (ps) as args

print("running counter.py\n--------------")
os.system("python counter.py")
print("--------------\ndone running counter.py")