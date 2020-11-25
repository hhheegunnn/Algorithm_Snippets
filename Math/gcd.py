# 최대 공약수 gcd 유클리드 호제법

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print("GCD(192,162) = ",gcd(162,192))

# GCD(192,162) =  6

# 꼭 a가 b 보다 안커도 됨 