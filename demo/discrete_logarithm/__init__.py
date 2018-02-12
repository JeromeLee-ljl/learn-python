import random

#离散对数加密 然而并不知道对数体现在哪
class User(object):
    def __init__(self, prime_num, generator_num):
        # 素数
        self.prime_num = prime_num
        # 生成元
        self.generator_num = generator_num
        # 私钥
        self._private_key = random.randint(1, self.prime_num)
        print("私钥", self._private_key)

    def pub_key(self):
        key = self.generator_num ** self._private_key % self.prime_num
        print("公钥", key)
        return key

    def calc_key(self, pub_key):
        self.key = pub_key ** self._private_key % self.prime_num
        print("加密码", self.key)

    def en(self, txt):
        result = txt * self.key
        print(txt, "encode-->", result)
        return result

    def de(self, result):
        txt = result // self.key
        print(result, "decode-->", txt)
        return txt


if __name__ == '__main__':
    prime_num = 2579
    generator_num = 2

    a = User(prime_num, generator_num)
    b = User(prime_num, generator_num)

    a_pub_key = a.pub_key()
    b_pub_key = b.pub_key()
    # 交换密钥
    a.calc_key(b_pub_key)
    b.calc_key(a_pub_key)

    txt = 123
    result = a.en(txt)
    de_txt = b.de(result)
