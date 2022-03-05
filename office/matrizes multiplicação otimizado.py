def multiplicacao(m1,m2):
    
    m3 = []
    
    num_lin = len(m1)
    num_col = len(m2[0])
    
    a = 0
    b = 0
    c = 0
    
    """PARA CADA LINHA"""
    for i in range(num_lin):
        m3.append([])
        
        """PARA CADA ITEM DA LINHA"""
        for j in range(num_col):
            m3[a].append(0)
            for item in m1[0]:
                
                m3[a][b] += m1[a][c] * m2[c][b]
                c += 1
            
            b += 1
            c = 0
        a += 1
        b = 0
        
    return m3