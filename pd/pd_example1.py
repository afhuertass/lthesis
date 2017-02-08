
import pandas as pd
import numpy as np 
#primer ejemplo programacion dinamica

def fmaxs( datos ,n = 2):
    brigadas = range( 0 , 6 )
    for brig in brigadas:
        print brig 
    



dataFrame = pd.read_excel('./data/pd1.xlsx', sheetname="datos" , parse_cols="A,B,C,D" , convert_float = True )


n_rows , n_cols = dataFrame.shape

# el numero de columnas -1 es el numero de etapas

# lista de etapas  ( n = 3 , 2 , 1 )
etapas = range( n_cols -1 , 0 , -1 )

print etapas 

f_max_prev = None # variables f estrella y x estrella del libro
x_max_prev = None #

Fs = dict() # 
for etapa in etapas:

    if  etapa == n_cols -1 :
        
        f_max_prev = dataFrame.iloc[:  , -1 ]
        x_max_prev = dataFrame.iloc[: , 0 ]

        data = (f_max_prev , x_max_prev)
        Fs[etapa] = data 
        print f_max_prev
    else:
        print("### step ### ")
        f_aux = None

        f_max_new = []
        x_max_new = [] 
        for brigada in range( 0 , n_rows):
            lx = [] 
            for xs in range ( 0 , n_rows   ):
          
                #print("xs:" + str(xs))
                factor = None
                if (brigada - xs ) < 0 :
                    factor = np.nan
                else:
                    factor = f_max_prev[ brigada - xs ]
                    
                fn  = dataFrame[etapa][xs] + factor
                if np.isnan(fn) :
                    fn = 0.0 
                lx.append( fn )
            print lx
            val_max = max(lx)
            ind_max = lx.index(val_max)
            
            print("val max:" + str(val_max))
            print("ind max :" + str(ind_max))
            #factor = f_max_prev.shift(  (xs) )
            f_max_new.append( val_max )
            x_max_new.append( ind_max )


        f_max_prev = f_max_new[:]
        x_max_prev = x_max_new[:]

        data = ( f_max_prev , x_max_prev)
        Fs[etapa] = data 
            #fn = fn.fillna(value = 0.0 )
            #fn = fn.transpose()
            
            #print fn
        
#print f_max_prev
#print f_max_prev.shift( periods = 1)

