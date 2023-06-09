def bin_string(n):
    return [ bin(x)[2:].rjust(n,'0') for x in range(2**n) ]

class Knapsack:
    def BFKS01(self, cap, p, w):
        assert len(p) == len(w),"p and w don't have same size."
        
        n = len(p)
        binary_list = bin_string(n)
        #binary_list = list(product([0, 1], repeat=n)
        
        soln = []
        for s in binary_list:
            profit = sum([int(s[i])*p[i] for i in range(n)])
            weight = sum([int(s[i])*w[i] for i in range(n)])
            if(weight <= cap):
                soln.append((weight,profit,s))
            
        maxp = max(soln , key = lambda tup: tup[1])
        print(maxp)
        return maxp[1]
        
    def BFKSfrac(self, cap, p, w):
        assert len(p) == len(w), "p and w do not have the same number"
        n = len(p)
        binary_list = bin_string(n)
        
        maxP = 0
        for s in binary_list:
            z = []
            for i, x in enumerate(s):
                if x == '0':
                    z.append(i)

            profit = sum(int(s[i])*p[i] for i in range(n))
            weight = sum(int(s[i])*w[i] for i in range(n))
            fraction = 0

            if weight < cap:
                for i in z:
                    remaining = cap - weight
                    if remaining < w[i]:
                        remain = remaining
                    else:
                        remain = w[i]
                    
                    frac = (p[i] / w[i]) * remain
            
                    if frac > fraction:
                        fraction = frac 
                    else:
                        fraction = 0
                
            profit += fraction

            if weight <= cap and profit >= maxP:
                maxP = profit
                
        return maxP

    def greedyKS(self, cap, p, w):
        assert len(w) == len(p)
        n = len(p)
        ratios = [(p[i] / w[i], i) for i in range(n)]
        ratios.sort(reverse=True)

        maxp = 0
        for ratio, i in ratios:
            if cap == 0:
                return maxp
            amount = min(w[i], cap)
            maxp += amount * ratio
            cap -= amount

        return maxp
    
    def dynamic01(self, p, w, cap, len):
        result = [0]*(len+1)
        k = [[0]*(cap+1) for i in range(len+1)]
        p.insert(0,0) 
        w.insert(0,0)

        for i in range(len + 1):
            for j in range(cap + 1):
                if(i == 0 or j == 0):
                    k[i][j] = 0
                elif (w[i] <= j):
                    k[i][j] = max(p[i] + k[i-1][j-w[i]], k[i-1][j])
                else:
                    k[i][j]= k[i-1][j]
                
        i = len
        j = cap
        while(i > 0 and j > 0):
            if (k[i][j] == k[i-1][j]):
                i -= 1
            else:
                result[i] = 1
                j -= w[i]
                i -= 1
                
        result.pop(0)
        return(k[len][cap])
