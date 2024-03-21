N, M = map(int, input().split())
arr = list(map(int, input().split()))
m_arr = [0]
p_arr = [0]
for i in range(N):
    if arr[i] > 0:
        p_arr.append(arr[i])
    else:
        m_arr.append(arr[i])
m_arr.sort(reverse=True)
p_arr.sort()
ans = 0

def poparr(array, max_val):
    hap = 0
    while array:
        end_point = array.pop()

        for _ in range(M-1):
            if not array:
                break
            array.pop()

        if end_point == max_val:
            hap += abs(end_point)
        else:
            hap += abs(end_point) * 2

    return hap

if abs(m_arr[-1]) > abs(p_arr[-1]):
    m_arr.pop(0)
    p_arr.pop(0)
    m_hap = poparr(m_arr, m_arr[-1])
    p_hap = poparr(p_arr, 0)
    ans = m_hap + p_hap
else:
    m_arr.pop(0)
    p_arr.pop(0)
    p_hap = poparr(p_arr, p_arr[-1])
    m_hap = poparr(m_arr, 0)
    ans = p_hap + m_hap

print(ans)