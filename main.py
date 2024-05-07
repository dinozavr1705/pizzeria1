all_pizzas = {"1":"крученая пицца фреди фазбера","2":"пепперони","3":"пицца 4 сыра","4":"фирменная пицца с особым соусосом(в ноябре отсутствует)_"}
all_pizzas_cost ={all_pizzas["1"]:120,all_pizzas["2"]:200,all_pizzas["3"]:280,all_pizzas["4"]:360}
class User:
    def __init__(self):
        self.shop_list = {}
        self.cost_of_all_pizzas = 0

    def cost(self):
        a = self.shop_list.values()
        for i in a:
            self.cost_of_all_pizzas+=i

    def add_to_shop_list(self,pizza_name,pizza_cost):
        self.shop_list[pizza_name] = pizza_cost

    def bruh(self):
        self.cost_of_all_pizzas = 0
    def bruh1(self,bruh2):
        self.cost_of_all_pizzas = 0 + bruh2
    def bruh3(self):
        pass
    def buy_pizza(self):
        choice = str(input("какую пиццу вы выберите"))
        print(f"эта пицца стоит {all_pizzas_cost[all_pizzas[choice]]}")
        lol = int(input("сколько вы хотите заплатить? "))
        a = all_pizzas_cost[all_pizzas[choice]]
        if a > lol:
            print("вам не хватает")
            self.shop_list[choice] = a
        elif a == lol:
            print("оплата прошла успешно")
            self.cost_of_all_pizzas = 0
        else:
            print(f"ваша сдача составляет {lol - a} рублей")
            self.cost_of_all_pizzas = 0 + lol - a
    def buy_shop_list(self):
        self.cost()
        print("ваша корзина:")
        for i in self.shop_list.keys():
            print(i)
        a = int(input(f"это все будет стоить {self.cost_of_all_pizzas} рублей, будете покупать?(1 - да, 2 -нет "))
        if a == 1:
            b = int(input("сколько вы желаете заплатить? "))
            c = {b>self.cost_of_all_pizzas:f"ваша сдача {b - self.cost_of_all_pizzas}" , b == self.cost_of_all_pizzas:"оплата прошла успешно",b < self.cost_of_all_pizzas:"оплата не прошла"}
            d = {b > self.cost_of_all_pizzas:self.bruh1(b - self.cost_of_all_pizzas),
                 b == self.cost_of_all_pizzas: self.bruh, b < self.cost_of_all_pizzas: self.bruh3}
            x = c[True]
            print(c[True])
            if b>self.cost_of_all_pizzas:
                self.bruh1(b - self.cost_of_all_pizzas)
            elif b == self.cost_of_all_pizzas:
                self.bruh()
            else:
                self.bruh3()
bruh = 0
user = User()
while True:
    user.buy_pizza()


