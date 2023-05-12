
import time
import tkinter
import tkinter.messagebox
import customtkinter
import numpy as np

    

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    alloc=[]
    max=[]
    total_res=[]
    req=[]
    avail=[]
    pid=0
    seq=[]
    remaining_need=[]
    num_of_proc=0
    done=[]
    trying=[]
    not_work=[]  
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="please enter number of processes", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #to get the # of process
        def get_num():
          
          App.num_of_proc=int(self.entry.get())
          print(App.num_of_proc)
          self.entry.delete(0,tkinter.END)

        # create an entry box and button  
        self.entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="# of processes")
        self.entry.grid(row=2, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.button_1 = customtkinter.CTkButton(master=self.sidebar_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),width=20,height=20,command=get_num,text="submit")
        self.button_1.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

       
        
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Matrices Entry")
        self.tabview.add("Request Entry")
        
        self.tabview.tab("Matrices Entry").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Request Entry").grid_columnconfigure(0, weight=1)

       

        
        self.label_res = customtkinter.CTkLabel(self.tabview.tab("Matrices Entry"), text="total resources")
        self.label_res.grid(row=0, column=0, padx=20, pady=20)
        self.toral_res = customtkinter.CTkButton(self.tabview.tab("Matrices Entry"),
                                                  text="Add",command=self.button_click_event_T)
        self.toral_res.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.label_alloc = customtkinter.CTkLabel(self.tabview.tab("Matrices Entry"), text="allocation")
        self.label_alloc.grid(row=1, column=0, padx=20, pady=20)
        self.allocation =  customtkinter.CTkButton(self.tabview.tab("Matrices Entry"),
                                                        text="Add",command=self.button_click_event_A)
        self.allocation.grid(row=1, column=1, padx=0, pady=(20, 10))
        self.label_max_need = customtkinter.CTkLabel(self.tabview.tab("Matrices Entry"), text="max need")
        self.label_max_need.grid(row=2, column=0, padx=20, pady=20)
        self.max_need = customtkinter.CTkButton(self.tabview.tab("Matrices Entry"),
                                                        text="Add",command=self.button_click_event_M)
        self.max_need.grid(row=2, column=1, padx=20, pady=(20, 10))
        self.label_pid = customtkinter.CTkLabel(self.tabview.tab("Request Entry"), text="Process ID")
        self.label_pid.grid(row=3, column=0, padx=20, pady=(20,10))
        self.pid =  customtkinter.CTkButton(self.tabview.tab("Request Entry"),
                                                        text="Add",command=self.button_click_event_id)
        self.pid.grid(row=3, column=1, padx=20, pady=(20, 10))
        self.label_req = customtkinter.CTkLabel(self.tabview.tab("Request Entry"), text="Request")
        self.label_req.grid(row=4, column=0, padx=20, pady=(20,10))
        self.req = customtkinter.CTkButton(self.tabview.tab("Request Entry"),
                                                        text="Add",command=self.button_click_event_r)
        self.req.grid(row=4, column=1, padx=20, pady=(20, 10))
        self.req_sub = customtkinter.CTkButton(self.tabview.tab("Request Entry"),
                                                        text="submit",command=self.button_click_event_req)
        self.req_sub.grid(row=5, column=1, padx=20, pady=(20, 10))

     


        # create tabview
        self.tabview2 = customtkinter.CTkTabview(master=self, width=230)
        self.tabview2.grid(row=1, column=1, padx=(20, 20), pady=(0, 0), sticky="nsew")
        self.tabview2.add("Total_Res Matrix")
        self.tabview2.add("Allocation Matrix")
        self.tabview2.add("Max need Matrix")
        self.tabview2.add("Available Matrix")
        self.tabview2.add("Remaining Matrix")
        self.tabview2.tab("Total_Res Matrix").grid_columnconfigure(0, weight=1)
      
        self.tabview2.tab("Allocation Matrix").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview2.tab("Max need Matrix").grid_columnconfigure(0, weight=1)
        self.tabview2.tab("Available Matrix").grid_columnconfigure(0, weight=1)
        self.tabview2.tab("Remaining Matrix").grid_columnconfigure(0, weight=1) 
       
      

      

        # create scrollable frame for the steps
        self.steps_frame = customtkinter.CTkScrollableFrame(self, label_text="steps",width=250)
        self.steps_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.steps_frame.grid_columnconfigure(0, weight=1)
         # create results frame

        self.results_frame = customtkinter.CTkFrame(self)
        self.results_frame.grid(row=1, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
      
       
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
       
   

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

  



    def button_click_event_T(self):
   
     D= customtkinter.CTkInputDialog(text="m * n =\n note: m = #rows , n = #columns", title="set m*n")
     m_n= D.get_input()
     App.show_msg("enter the matrix elements (row by row & separated by space) as follows: \n assume matrix is 3*3: 0 0 0 1 1 1 3 3 3 \n(1st row is 000,2nd is 111,3rd is 333)" )
     Matrix= customtkinter.CTkInputDialog(text="enter the matrix elements", title="Matrix elements")
     Matrix=Matrix.get_input()
     R,C=App.set_m_n(m_n)
     
     App.total_res= App.matrix_reshape(Matrix,Rows=R,Columns=C,name="totalResources")
     App.show_msg("total resource matrix is added successfully")
     self.list_T = tkinter.Listbox(self.tabview2.tab("Total_Res Matrix"),font=("Times",14))
     self.list_T.grid(row=0, column=0, padx=20, pady=20)
     for i in  App.total_res:
      print('\t'.join(map(str, i)))
      self.list_T.insert(tkinter.END,'  \t  '.join(map(str, i)))

      
     app.update() 

     
   

    def button_click_event_A(self):
   
     D= customtkinter.CTkInputDialog(text="m * n =\n note: m = #rows , n = #columns", title="set m*n")
     m_n= D.get_input()
     App.show_msg("enter the matrix elements (row by row & separated by space) as follows: \n assume matrix is 3*3: 0 0 0 1 1 1 3 3 3 \n(1st row is 000,2nd is 111,3rd is 333)" )
     Matrix= customtkinter.CTkInputDialog(text="enter the matrix elements", title="Matrix elements")
     Matrix=Matrix.get_input()
     R,C=App.set_m_n(m_n)
     App.alloc=App.matrix_reshape(Matrix,Rows=R,Columns=C,name="allocation")
     App.show_msg("allocation matrix is added successfully")
     
     self.list_A= tkinter.Listbox(self.tabview2.tab("Allocation Matrix"),font=("Times",14))

     self.list_A.grid(row=0, column=0, padx=20, pady=20)
     for i in  App.alloc:
      print('\t'.join(map(str, i)))
      self.list_A.insert(tkinter.END,'  \t  '.join(map(str, i)))
    
     app.update()
   

    def button_click_event_M(self):
   
     D= customtkinter.CTkInputDialog(text="m * n =\n note: m = #rows , n = #columns", title="set m*n")
     m_n= D.get_input()
     App.show_msg("enter the matrix elements (row by row & separated by space) as follows: \n assume matrix is 3*3: 0 0 0 1 1 1 3 3 3 \n(1st row is 000,2nd is 111,3rd is 333)" )
     Matrix= customtkinter.CTkInputDialog(text="enter the matrix elements", title="Matrix elements")
     Matrix=Matrix.get_input()
     R,C=App.set_m_n(m_n)
     App.max=App.matrix_reshape(Matrix,Rows=R,Columns=C,name="max need")  
     App.show_msg("max need matrix is added successfully")
     self.list_M= tkinter.Listbox(self.tabview2.tab("Max need Matrix"),font=("Times",14))

     self.list_M.grid(row=0, column=0, padx=20, pady=20)
     for i in  App.max:
      print('\t'.join(map(str, i)))
      self.list_M.insert(tkinter.END,'  \t  '.join(map(str, i)))
     app.update()
 

    def button_click_event_id(self):
   
     D= customtkinter.CTkInputDialog(text="process id", title="set process id")
     id= int(D.get_input())
     App.pid=id
     App.show_msg("ID is added successfully")
    
 

    def button_click_event_r(self):
   
     D= customtkinter.CTkInputDialog(text="m * n =\n note: m = #rows , n = #columns", title="set m*n")
     m_n= D.get_input()
     App.show_msg("enter the matrix elements (row by row & separated by space) as follows: \n assume matrix is 3*3: 0 0 0 1 1 1 3 3 3 \n(1st row is 000,2nd is 111,3rd is 333)" )
     Matrix= customtkinter.CTkInputDialog(text="enter the matrix elements", title="Matrix elements")
     Matrix=Matrix.get_input()
     R,C=App.set_m_n(m_n)
     App.req_mat(Matrix)
     App.show_msg("Request is added successfully")
    

    def show_mat(self):

        if (App.avail.__len__!=0 and App.remaining_need.__len__!=0):
         self.list_AV = tkinter.Listbox(self.tabview2.tab("Available Matrix"),font=("Times",14))
         self.list_AV.grid(row=0, column=0, padx=20, pady=20)
          
         for i in  App.avail:
          print('\t'.join(map(str, i)))
          self.list_AV.insert(tkinter.END,'  \t  '.join(map(str, i)))
         
         app.update()
         self.list_REM = tkinter.Listbox(self.tabview2.tab("Remaining Matrix"),font=("Times",14))
         self.list_REM.grid(row=0, column=0, padx=20, pady=(20,10))
         for i in  App.remaining_need:
          print('\t'.join(map(str, i)))
          self.list_REM.insert(tkinter.END,'  \t  '.join(map(str, i)))

   
         
        app.update()

      
    def button_click_event_req(self):
  
     App.bank()  
     App.show_mat(self)
     safe,seq= App.banker_alg(alloc=App.alloc,avail=App.avail,rem=App.remaining_need,self=self)
     if safe:
      print(seq)
     else:
      print("deadlock")

   
    def set_m_n(m_n):
     m_n=list(m_n.split("*"))
     Rows = m_n[0]
     Columns = m_n[1]
     Rows=int(Rows)
     Columns=int(Columns)
     return Rows,Columns

    def matrix_reshape(ele,Rows,Columns,name):
 

     elements = list(map(int, ele.split()))   

     matrix = np.array(elements).reshape(Rows, Columns) 
 # Printing the matrix given by the user 
 
     print("matrix:\n",matrix)
     return matrix

  
    def req_mat(k):
     elements = list(map(int, k.split()))  
     App.req.append(elements)


    def show_msg(text):
      tkinter.messagebox.showinfo("check",text)

    def error_msg(text):
     tkinter.messagebox.showerror('Error', text)


    def bank():
     
     App.avail=App.total_res-np.sum(App.alloc,axis=0)
     if np.any(App.req[0] > App.max[App.pid] - App.alloc[App.pid]):
        print("Error: the process has exceeded its maximum claim.")
        App.error_msg("Error: the process has exceeded its maximum claim.")
     
    
     if np.any(App.req > App.avail):
        print("Error: the requested resources are not available.")
        App.error_msg("Error: the requested resources are not available.")

     App.alloc[App.pid]+=App.req[0]
     App.remaining_need=App.max-App.alloc
     App.avail-=App.req  



    def banker_alg (alloc,avail,rem,self):
      finish= np.zeros(5,bool)
      j=0
      while True:
       found=False
       for i in range(App.num_of_proc):
   
         if not finish[i] and  np.all(rem[i] <= avail[0]):
          print("trying p",i)
          App.printing_steps("trying p"+str(i),j,self)
          
          j+=1
          time.sleep(3)
         
          avail+=App.alloc[i]
          
          
          finish[i]=True
          App.seq.append(i)
          App.printing_seq(self,i)
          found=True
          print("p",i,"is done")
          App.printing_steps( "p"+str(i)+" is done",j,self)
          App.show_mat(self)
          
          
          j+=1
          time.sleep(3)

         elif not finish[i] and not np.all(rem[i] <= avail[0]) :
          print("p",i,"cannot work, trying another process...")
          App.printing_steps("p"+str(i)+"cannot work, trying another process",j,self)
        
          j+=1
          time.sleep(3)

   

       if not found:
         if np.all(finish):
        # If all processes have finished, the system is in a safe state
          App.print_safe("it is safe!",self)
          return True, App.seq
         
          
     
         else:
        # If there is no process that can be executed, the system is in an unsafe state
          App.print_safe("DeadLock!!,it is not safe",self)
          return False, None
         
      

    
    def printing_steps(text,i,self):
      switch = customtkinter.CTkLabel(master=self.steps_frame, text=text)
      switch.grid(row=i, column=0, pady=(0, 20))
      app.update()    
      
    j=0
    def printing_seq(self,i):
       
       switch = customtkinter.CTkLabel(master=self.results_frame, text=f"p {i} ")
       switch.grid(row=0, column=App.j, pady=(0, 20))
       app.update() 
       App.j+=1

    def print_safe(text,self):
      switch = customtkinter.CTkLabel(master=self.results_frame, text=text)
      switch.grid(row=3, column=0, pady=(0, 20))



    
        

if __name__ == "__main__":
    app = App()
    app.mainloop()



 