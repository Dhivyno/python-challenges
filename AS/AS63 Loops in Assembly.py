      LDA R1
      ANI #%00001111 
      ADD R0, R1  
      LDA R1
      ANI #%11110000
      RAR            
      ADD R0, R1    
      HLT             
