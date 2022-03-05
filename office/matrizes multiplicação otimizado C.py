def multiplicacao(m1,m2):
    
    m3 = []
    
    num_lin = len(m1)
    num_col = len(m2[0])
    
    """PARA CADA LINHA"""
    for i in range(num_lin):
        m3.append([])
        
        """PARA CADA ITEM DA LINHA"""
        for j in range(num_col):
            m3[i].append(0)
            for c in range(len(m1[0])):
                
                m3[i][j] += m1[i][c] * m2[c][j]
        
    return m3