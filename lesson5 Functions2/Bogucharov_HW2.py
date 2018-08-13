def mysqrt(num, eps=0.001, estimation=1):
    new_estimation = (num / estimation + estimation) / 2
    if abs(new_estimation - estimation) <= eps:
        print(round(new_estimation, 2))
        return
    mysqrt(num, eps, new_estimation)


mysqrt(4)
mysqrt(5, 0.01)
mysqrt(4 / 10000)
