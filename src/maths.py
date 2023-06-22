import numpy as np
def minmax(x):
    return [np.min(x), np.max(x)]


def minmax_of_all(old, new_list):
    if old == None:
        return minmax(new_list)
    
    new = minmax(new_list)    
    if new[0] > old[0]:
        new[0] = old[0]
    if new[1] < old[1]:
        new[1] = old[1]
    print(np.array(new)-np.array(old))
    return new
    
def main():
    x = None
    for i in range(5):
        a = np.random.rand(5)
        print(a)
        # print(f'Local Extremes - {minmax(a)}')
        x = minmax_of_all(x, a)
        # print(f'Global Extremes - {minmax_of_all(x, a)}')
    return

if __name__ == '__main__':
    main()