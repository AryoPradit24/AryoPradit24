def sum(n: int) -> int:
    mod = 1000_003
    return (4*(1-(-1)**(n+1)*pow(3,2*n,mod))/(1+3))%mod
