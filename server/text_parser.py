import pandas as pd
import numpy as np

'''
f = open("/home/sandman/Documents/glove/glove.6B.300d.txt")


words = []
embeddings = []

for line in f:
    line_arr = line.split()

    word = line_arr[0]
    if (len(word) > 1):
        metadata = {"word": word}
        embedding = [float(idx) for idx in line_arr[1:]]

        words.append(metadata)
        embeddings.append(embedding)

f.close()

data_dict = {"id": list(range(0, len(words))),
             "vector": embeddings, "metadata": words}

df = pd.DataFrame(data=data_dict)

# print(df)
df.to_csv('./pinecone_embeddings.csv')
'''


df = pd.read_csv("./pinecone_embeddings.csv")

# print(df)
print(df['vector'][50])
print(df["metadata"][50])
'''
tru = "0.12223 -0.062161 0.10265 -0.40805 0.10654 -0.48842 0.12906 0.072008 -0.16505 -1.2484 -0.27203 0.24494 -0.019948 0.23436 -0.57432 0.31995 -0.18246 0.1503 0.34655 0.2265 0.36638 0.79454 0.19986 0.225 0.11843 -0.15771 -0.16916 -0.55472 0.23015 0.30359 -0.70714 0.42985 -0.31805 -0.55347 -0.96565 0.62324 0.44734 -0.1403 -0.096 -0.62947 0.12182 -0.059004 0.60845 0.15747 -0.022277 -0.092013 0.046482 -0.26055 -0.26406 -0.17651 0.44739 0.21398 0.079406 0.061875 -0.55664 0.076884 -0.22866 0.075791 0.15964 0.17276 0.39957 -0.17731 -0.44611 0.20684 -0.42703 0.0037284 0.509 -0.82593 -0.085914 0.091054 -0.36856 -0.19303 0.2082 -0.027169 0.31786 0.030474 -0.088152 0.47706 0.1341 -0.20072 -0.27623 0.43892 0.94871 0.17903 -0.13401 0.25436 -0.10244 0.063746 0.071544 0.052862 -0.44849 0.33915 -0.29395 -0.20647 0.61184 -0.39364 -0.45656 0.051248 0.20079 0.31602 0.17865 -0.58358 0.082549 -0.61667 0.36087 0.65531 0.14653 -0.071991 0.15614 -0.43585 0.36064 -0.35896 0.21708 -0.38949 0.68852 0.097017 0.4674 -0.82492 -0.012216 0.083045 -0.044133 0.26483 0.22458 0.1767 -0.10118 -0.55313 0.318 0.27509 -0.21402 -0.43556 -0.34446 -0.12704 -0.054073 0.62872 -0.41001 0.19714 -0.5672 -0.31658 0.9053 0.027934 0.2113 0.21724 0.3195 0.14062 -0.7701 0.053052 0.061543 0.050296 -0.14394 0.12125 -0.73577 -0.40958 0.31672 0.28044 -0.058603 0.57888 -0.1712 -0.061543 0.72776 -0.37305 -0.59949 -0.067845 0.39678 -0.068958 0.020298 0.13247 0.40025 -0.29223 0.30528 -0.11507 0.20241 -0.37877 -1.1511 -0.44627 0.60029 0.063876 0.3107 -0.029327 -0.16545 -0.021006 0.052126 -0.6909 -0.40967 0.12529 -0.15659 -0.25864 0.31925 -0.083312 0.069714 0.028983 -0.48995 -0.31852 0.57388 0.11705 0.43639 0.041366 -0.66766 -0.25382 -0.31567 -0.5258 0.44724 0.040228 0.30393 -0.17622 0.36996 0.14062 0.80402 0.063388 0.15757 -0.15083 -0.18056 -0.316 -1.1182 0.55308 -0.45927 0.25279 0.12756 0.084556 -0.187 0.34364 -0.42563 0.12472 0.0070946 0.49408 -0.0069488 0.31937 -0.45428 -0.092554 -0.012733 0.27243 0.047856 -0.25248 0.20009 -0.53538 -0.49092 0.20087 -0.32953 -0.64246 -0.62285 0.49539 -0.30896 0.082288 -0.15695 -0.13768 0.022834 -0.32196 -0.070724 0.34402 0.069751 -0.13499 0.75713 -0.43602 -0.41223 0.29663 0.22165 -0.037991 0.25625 0.2371 0.05644 0.14575 -0.0070891 0.036454 -0.22941 0.0034585 -0.40737 -0.022802 0.48937 -0.7906 0.64764 0.12277 0.26465 0.11988 0.48374 0.33964 -0.396 -0.072488 -0.75909 0.26677 0.58196 -0.54229 0.33786 -0.25471 0.34492 0.48574 0.60619 0.279 0.13243 0.10837 0.25857 -0.67635 -0.13474 0.39164 -0.15988 0.34202 0.76314 -0.49514 -0.22336 0.18838 0.12686 0.19456"
fal = "0.55439 -0.085219 -0.31988 -0.1691 -0.29832 -0.28423 0.11363 0.65683 0.24823 -1.9314 0.022737 0.60779 0.13547 0.50247 -0.39238 0.24324 0.068047 -0.47801 0.38315 -0.13515 0.19173 0.088711 -0.39833 -0.28885 -0.34894 -0.030636 -0.106 -0.17216 0.17947 0.87219 -0.9214 0.34497 -0.11884 -0.19078 -0.54191 0.1007 -0.77182 -0.11747 0.51761 0.10381 -0.53278 0.21559 -0.27057 0.77774 0.21076 -0.51575 -0.49584 -0.17465 -0.37669 0.12461 0.93686 0.082385 0.54021 0.10453 -0.41341 0.26045 -0.17718 0.22294 -0.028334 0.23652 0.037439 -0.18425 0.44453 -0.02977 -0.12991 -0.22142 0.17659 -0.82022 0.04056 0.20961 -0.023596 -0.36297 0.27339 -0.17286 -0.15121 0.31537 0.91249 0.098087 0.42424 0.6546 -0.33139 0.41263 0.17996 0.75602 -0.11874 0.28958 0.056087 0.0021477 -0.26114 0.54033 -0.59412 -0.057224 0.074611 0.18342 0.26055 0.81494 -0.20422 0.11902 0.75717 -0.59814 -0.099803 0.20251 0.40179 0.51187 0.33351 -0.79421 -0.29053 -0.45451 -0.59452 0.10312 0.027901 0.096397 0.013611 -0.55959 0.95584 0.42188 -0.0045522 0.77694 -0.13688 -0.26828 0.47714 0.24661 -0.11335 0.37392 0.027083 -0.36149 0.0012311 -0.63023 0.34428 0.030014 -0.60467 -0.0086586 0.0097451 0.63667 0.023508 -0.39995 0.70875 -0.55463 0.2191 -0.3652 -0.10612 0.17232 0.24732 0.143 0.079085 0.053343 0.12869 -0.7122 0.70338 -0.37917 -0.0044442 0.21811 -0.33694 -0.23005 -0.96895 0.31527 -0.073771 -0.12972 -0.13713 -0.24979 0.18523 -0.3224 0.21994 0.1176 -0.10437 0.15177 -0.40447 -0.26964 -0.43252 -0.46681 0.78099 -0.13944 -0.093231 0.04987 -0.12683 -0.097899 -0.062282 -0.055067 -0.16509 -0.3244 0.43378 -0.12798 -0.038633 0.2106 -0.50717 -0.35338 -0.25448 0.27063 0.36342 -0.098928 0.33326 -0.21942 0.53901 0.0044639 0.23668 0.1466 0.18306 -0.62193 -0.54911 0.48968 -0.16561 -0.063218 -0.68171 -0.09254 0.46306 0.15254 -0.036834 0.11918 0.0080517 -0.25967 -0.15613 0.19103 0.12062 -0.014601 -0.073043 -0.32347 0.36058 0.01913 0.024538 0.56444 -0.094491 0.56649 0.39927 -0.43356 0.32572 0.13548 -0.15926 0.12374 1.2536 0.34831 -0.46947 -0.11751 -0.034591 -0.47831 -0.84715 -0.23707 -0.62729 -0.20924 -0.0044933 0.044305 -0.27297 0.20521 -0.1346 -0.015359 -0.27588 -0.46108 0.45687 -0.031738 0.039933 -0.35385 -0.74576 0.11804 -0.016513 -0.15746 0.33587 -0.30572 0.24166 0.17191 0.18782 0.16233 0.026706 -0.33238 0.35292 0.58085 0.013707 0.32173 0.18638 -0.78982 0.29653 -0.2196 0.40856 -0.34564 0.021388 0.94896 -0.17639 0.2854 -1.4173 0.063337 1.2512 0.18317 0.020716 0.054017 -0.2431 0.26632 -0.24356 0.1932 0.018286 0.37677 -0.088881 -0.43679 0.022612 -0.01636 -0.090973 0.4904 0.025302 -0.55881 0.34433 0.3366 -0.012362 0.37296"
truth = "0.038429 -0.51199 -0.15712 -0.73346 0.27319 0.24353 -0.33097 -0.00070355 -0.23664 -0.73523 -0.18475 0.34058 0.48249 0.50483 -0.5077 0.42109 -0.19487 0.33453 0.13735 0.067023 0.42028 0.72348 0.21168 0.23914 0.14471 0.16251 -0.61541 -1.0224 -0.056761 0.090351 -0.34777 0.3904 0.097491 -0.78579 0.21744 -0.012945 -0.087638 -0.21392 0.36534 -0.1815 0.10635 0.69467 0.32096 0.45486 0.049684 0.1011 -0.36113 -0.27842 -0.52265 -0.09453 0.34434 0.09622 0.3233 -0.018441 -0.335 0.017833 0.55925 0.077004 -0.039915 0.26348 -0.2179 -0.8694 -0.19395 -0.166 0.2157 0.30813 0.22143 -0.53382 0.2618 0.3561 -0.56419 -0.086598 -0.07322 -0.011665 0.63397 0.32568 0.20481 0.77152 -0.14038 0.35829 -0.1666 0.23913 0.78833 0.14227 -0.5108 0.25907 -0.21026 0.157 -0.43297 0.66547 -0.88672 -0.49385 -0.18656 0.40467 0.23276 0.25698 -0.56728 0.11347 0.29555 0.12016 0.12179 0.1369 -0.13963 -0.31386 0.46211 0.33974 0.48587 -0.13704 0.1713 -0.28463 0.38626 0.31325 0.17538 -0.37113 0.10149 0.1253 -0.019431 -0.61775 0.73812 0.38823 -0.11989 0.45068 0.27571 0.065998 -0.17706 -0.073294 0.33629 -0.28345 -0.51388 -0.45113 -0.1178 -0.25093 0.14948 -0.065483 -0.30263 0.40932 0.056803 -0.46579 0.76677 0.28997 0.041598 -0.4492 0.37202 0.015886 -0.12652 -0.50803 0.13125 -0.014654 0.18599 0.15361 -0.68887 -0.74702 -0.013624 0.46601 -0.76083 0.071868 -0.32005 -0.16096 0.55418 -0.26085 -0.41146 -0.15322 0.11388 -0.18586 -0.062185 -0.068679 -0.18956 -0.37112 0.54346 0.20497 0.88776 -0.071579 -0.48136 0.045946 0.68607 -0.222 0.4807 -0.06271 -0.20023 -0.41842 0.016328 -0.55379 -0.4191 0.068953 -0.79246 -0.13702 0.38072 0.16107 0.22096 0.22568 -0.47441 -0.036908 0.35736 -0.19162 0.42478 -0.026377 -0.67941 0.086695 -0.29331 -0.32451 -0.19485 -0.40648 -0.43369 -0.11167 0.49594 -0.21987 -0.047705 0.43108 0.044428 -0.39868 -0.090655 -0.079983 -0.60468 0.17083 -0.41022 -0.077806 0.079979 -0.11097 0.038046 0.56583 -0.69014 0.3747 0.087769 0.16075 0.0061826 0.35767 -0.25537 0.26381 0.12971 -0.22845 0.29536 -0.38817 0.44512 -0.45041 -0.61669 0.013552 -0.2748 -0.55329 -0.51792 0.12243 -0.052322 0.26123 -0.0087445 -0.15716 0.01434 -0.19455 -0.080308 0.17902 0.0051833 0.40746 0.3766 -0.71522 -0.44236 0.10979 -0.3351 -0.47454 -0.13135 0.081781 0.15292 -0.028853 0.028469 0.33847 -0.094318 0.026253 -0.53074 0.29975 0.53837 -0.54912 0.94171 0.14551 0.26736 -0.27824 0.028483 0.73009 -0.073051 -0.34903 0.017752 -0.41773 0.49779 -0.62563 -0.25118 -0.27987 0.33688 0.13388 0.2476 -0.47715 0.13194 -0.1868 0.0968 -0.65184 -0.18342 -0.11901 0.57987 0.17908 0.15809 -1.142 -0.17359 0.67719 0.35408 0.033497"
the = "0.04656 0.21318 -0.0074364 -0.45854 -0.035639 0.23643 -0.28836 0.21521 -0.13486 -1.6413 -0.26091 0.032434 0.056621 -0.043296 -0.021672 0.22476 -0.075129 -0.067018 -0.14247 0.038825 -0.18951 0.29977 0.39305 0.17887 -0.17343 -0.21178 0.23617 -0.063681 -0.42318 -0.11661 0.093754 0.17296 -0.33073 0.49112 -0.68995 -0.092462 0.24742 -0.17991 0.097908 0.083118 0.15299 -0.27276 -0.038934 0.54453 0.53737 0.29105 -0.0073514 0.04788 -0.4076 -0.026759 0.17919 0.010977 -0.10963 -0.26395 0.07399 0.26236 -0.1508 0.34623 0.25758 0.11971 -0.037135 -0.071593 0.43898 -0.040764 0.016425 -0.4464 0.17197 0.046246 0.058639 0.041499 0.53948 0.52495 0.11361 -0.048315 -0.36385 0.18704 0.092761 -0.11129 -0.42085 0.13992 -0.39338 -0.067945 0.12188 0.16707 0.075169 -0.015529 -0.19499 0.19638 0.053194 0.2517 -0.34845 -0.10638 -0.34692 -0.19024 -0.2004 0.12154 -0.29208 0.023353 -0.11618 -0.35768 0.062304 0.35884 0.02906 0.0073005 0.0049482 -0.15048 -0.12313 0.19337 0.12173 0.44503 0.25147 0.10781 -0.17716 0.038691 0.08153 0.14667 0.063666 0.061332 -0.075569 -0.37724 0.01585 -0.30342 0.28374 -0.042013 -0.040715 -0.15269 0.07498 0.15577 0.10433 0.31393 0.19309 0.19429 0.15185 -0.10192 -0.018785 0.20791 0.13366 0.19038 -0.25558 0.304 -0.01896 0.20147 -0.4211 -0.0075156 -0.27977 -0.19314 0.046204 0.19971 -0.30207 0.25735 0.68107 -0.19409 0.23984 0.22493 0.65224 -0.13561 -0.17383 -0.048209 -0.1186 0.0021588 -0.019525 0.11948 0.19346 -0.4082 -0.082966 0.16626 -0.10601 0.35861 0.16922 0.07259 -0.24803 -0.10024 -0.52491 -0.17745 -0.36647 0.2618 -0.012077 0.08319 -0.21528 0.41045 0.29136 0.30869 0.078864 0.32207 -0.041023 -0.1097 -0.092041 -0.12339 -0.16416 0.35382 -0.082774 0.33171 -0.24738 -0.048928 0.15746 0.18988 -0.026642 0.063315 -0.010673 0.34089 1.4106 0.13417 0.28191 -0.2594 0.055267 -0.052425 -0.25789 0.019127 -0.022084 0.32113 0.068818 0.51207 0.16478 -0.20194 0.29232 0.098575 0.013145 -0.10652 0.1351 -0.045332 0.20697 -0.48425 -0.44706 0.0033305 0.0029264 -0.10975 -0.23325 0.22442 -0.10503 0.12339 0.10978 0.048994 -0.25157 0.40319 0.35318 0.18651 -0.023622 -0.12734 0.11475 0.27359 -0.21866 0.015794 0.81754 -0.023792 -0.85469 -0.16203 0.18076 0.028014 -0.1434 0.0013139 -0.091735 -0.089704 0.11105 -0.16703 0.068377 -0.087388 -0.039789 0.014184 0.21187 0.28579 -0.28797 -0.058996 -0.032436 -0.0047009 -0.17052 -0.034741 -0.11489 0.075093 0.099526 0.048183 -0.073775 -0.41817 0.0041268 0.44414 -0.16062 0.14294 -2.2628 -0.027347 0.81311 0.77417 -0.25639 -0.11576 -0.11982 -0.21363 0.028429 0.27261 0.031026 0.096782 0.0067769 0.14082 -0.013064 -0.29686 -0.079913 0.195 0.031549 0.28506 -0.087461 0.0090611 -0.20989 0.053913"

tru = tru.split()
tru = [float(idx) for idx in tru]

truth = truth.split()
truth = [float(idx) for idx in truth]

fal = fal.split()
fal = [float(idx) for idx in fal]

the = the.split()
the = [float(idx) for idx in the]

print(len(the))


def euclidean(a, b):
    sum = 0
    for i in range(0, len(a)):
        sum += (a[i] - b[i])**2

    return np.sqrt(sum)


print("___Dot___")
print(f"Opposites: {np.dot(tru, fal)}")
print(f"Similiar: {np.dot(tru, truth)}")
print(f"Neutral: {np.dot(tru, the)}")
print(f"Same: {np.dot(tru, tru)}\n\n")

print("___Euclidean___")
print(f"Opposites: {euclidean(tru, fal)}")
print(f"Similiar: {euclidean(tru, truth)}")
print(f"Neutral: {euclidean(tru, the)}")
print(f"Same: {euclidean(tru, tru)}\n\n")

print(euclidean([2, 2], [-2, -2]))
print(euclidean([2, 2], [2, 1]))
'''