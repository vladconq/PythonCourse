def mysqrt(num, eps=0.0000001, estimation=1):
    new_estimation = (num / estimation + estimation) / 2
    if abs(new_estimation - estimation) <= eps:
        if eps != 0.0000001:
            print(round(new_estimation, len(str(eps)) - 2))
        else:
            index = None
            str_new_est = str(new_estimation)
            for i in range(len(str_new_est)):
                if str_new_est[i].isdigit() and str_new_est[i] != '0':
                    index = i
                    break
            print(round(new_estimation, index))
        return
    mysqrt(num, eps, new_estimation)


mysqrt(4)
mysqrt(5, 0.01)
mysqrt(4 / 10000)
mysqrt(4 / 1000000)
mysqrt(100)
