class noeud : 
    
    def __init__(self,fixe):
        self.gauche = None
        self.droite = None
        self.fixe = fixe
        self.decision = []
        self.z = None
    
    def separer(self) : 
        
        if len(self.fixed) != len(self.decision) : 
            
            left  = self.fixed_vars
            right = self.fixed_vars

            left.append(1)
            right.append(0)

            self.left = noeud(left)
            self.right = noeud(right)    
    
    def evaluer(self) :
        poids_max = poids_max
        decision = []
        z = 0

        for i in range(len(objets)): 
             
            if self.fixe[i] == 1 : 
                if objets[i].poids > poids_max : 
                    return
                poids_max -= objets[i].poids
                z +=  objets[i].utilite
            decision.append(self.fixe[i])
            

        for k in objets[len(self.fixed_vars):] : 
            if k.poids <= poids_max : 
                decision.append(1)
                poids_max -= k.poids
                z +=  k.utilite
            
            else :
                decision.append(0)
        self.decision = decision
        self.z = z

    

class objet:
    
    def __init__(self,poids,utilite):
        self.utilite = utilite
        self.poids = poids

objets = []

def ajout_objects() : 
    
    for i in range(6):
        x = int(input("Poids : ")) 
        y = int(input("Utilité : ")) 
        objets.append(objet(x,y))

def solution_initiale(objets,poids_max) : 
    decision = []
    k = poids_max

    for i in objets : 
        if i.poids <= k : 
            decision.append(1)
            k -= i.poids
        else :
            decision.append(0)
    print("les objets sélectionnés : ",decision), 
    print("le poids des objets: ",poids_max-k)


def ajout_poids_max() :
        poids_max = int(input("Donnez le Poids Maximum du sac-a-dos : ")) 
        return poids_max

def tri (objets):
    objets.sort(key = lambda a : (a.utilite/a.poids) , reverse = True)

if __name__ == '__main__':
    
    ajout_objects()
    tri(objets)
    poids_max = ajout_poids_max()
    
    solution_initiale(objets,poids_max)