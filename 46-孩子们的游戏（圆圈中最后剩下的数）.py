'''
题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:
首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....
直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
如果没有小朋友，请返回-1
示例1
输入5,3
返回值3
'''
class Solution:
    # 约瑟夫环。时间复杂度O(n)，空间复杂度O(1)
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0:
            return -1
        if n == 1:
            return 0
        index = 0
        for i in range(2, n + 1):
            index = (index + m) % i
            # print(index)
        return index


if __name__ == '__main__':
    u = Solution()
    print(u.LastRemaining_Solution(5, 0))
    print(u.LastRemaining_Solution(5, 1))
    print(u.LastRemaining_Solution(5, 3))
    print(u.LastRemaining_Solution(0, 1))