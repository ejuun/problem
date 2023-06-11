from math import lcm,gcd

a, b = map(int, input().split())
c, d = map(int, input().split())
ans2 = lcm(b, d)

multi_a = (ans2 // b) * a
multi_c = (ans2 // d) * c
ans1 = multi_a + multi_c

ans_gcd = gcd(ans1, ans2)
ans1 = ans1 // ans_gcd
ans2 = ans2 // ans_gcd
print(ans1, ans2)