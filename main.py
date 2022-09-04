from Cartoon import Cartoon
from CartoonList import CartoonList

if __name__ == "__main__":
    cartoonList = CartoonList()

    cartoon1 = Cartoon("Battle", 2022, 153, "Savchuk")
    cartoon2 = Cartoon("Victory", 2022, 53, "Savchuk")

    # print(cartoon1.__str__())

    cartoonList.add(cartoon1)
    cartoonList.add(cartoon2)

    print(cartoonList.cartoonList)




