def max2(a,b):
    if a == b:
        return '{}와 {}는 같다.'.format(a, b)
    else:
        return '{}이(가) 크다.'.format(max(a,b))

print(max2(2,3))

# def maxN(*args_list):
#     args_list = list(args_list)
#     args_list.sort(reverse=True)
#     return args_list[0]

    # length = len(args_list)
    #
    # for i in range(length - 1):
    #     indexMin = i
    #     for j in range(i + 1, length):
    #         # 기본 선택 정렬에서 반대로 왼쪽이 가장 큰 수가 오도록 정렬
    #         if args_list[indexMin] < args_list[j]:
    #             indexMin = j
    #     args_list[i], args_list[indexMin] = args_list[indexMin], args_list[i]
    #
    # return args_list[0]



#print(maxN(3,1,4,9,7,8,5))