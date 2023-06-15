def solution(survey, choices):
    personal = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0,}
    answer = ''
    for i in range(len(survey)):
        if survey[i][0] == 'R':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['T'] += choices[i] - 4
        elif survey[i][0] == 'T':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['R'] += choices[i] - 4
        
        elif survey[i][0] == 'C':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['F'] += choices[i] - 4
        elif survey[i][0] == 'F':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['C'] += choices[i] - 4
        
        elif survey[i][0] == 'J':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['M'] += choices[i] - 4
        elif survey[i][0] == 'M':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['J'] += choices[i] - 4
        
        elif survey[i][0] == 'A':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['N'] += choices[i] - 4
        elif survey[i][0] == 'N':
            if choices[i] <= 4:
                personal[survey[i][0]] += 4 - choices[i]
            else:
                personal['A'] += choices[i] - 4
        
    if personal['R'] < personal['T']:
        answer += 'T'
    else:
        answer += 'R'

    if personal['C'] < personal['F']:
        answer += 'F'
    else:
        answer += 'C'

    if personal['J'] < personal['M']:
        answer += 'M'
    else:
        answer += 'J'

    if personal['A'] < personal['N']:
        answer += 'N'
    else:
        answer += 'A'
            
    return answer