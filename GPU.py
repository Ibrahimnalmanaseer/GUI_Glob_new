


def GPU_spec(app,message):
    

    avg_call_time = int(app.avg_call_time_var.get())/3600 if app.avg_call_time_var.get() else 0
    expected_calls = int(app.expected_calls_var.get()) if app.expected_calls_var.get() else 0


    total_hours = round(avg_call_time * expected_calls) if avg_call_time and expected_calls else 0

    with_dr = app.with_dr_var.get()
    if with_dr :
        
      total_hours*=2

    number_of_GPU= (int(total_hours)+1399) //1400

    message +=f'''
    ----------------------------------------
              Analytics Server GPU
    ----------------------------------------
    GPU Specifications:
    RTX 4090
    RAM 16 GB
    CPU core i91300k
    SSD 500
    ----------------------------------------
    Total_hours = {total_hours }
    ========================================
    Total GPU needed = {number_of_GPU}
    ========================================
  '''
    
    if with_dr :
        
      message+=f'''
    ========================================
    DR GPU needed = {number_of_GPU}
    ========================================

'''
    
    return message
    
  

   
        
 
        

       


   


    
    
    


        






