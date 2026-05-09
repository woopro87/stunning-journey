class VendingMachine:
    VALID_COINS = {100, 500, 1000}

    def __init__(self):
        self.balance = 0
        self.drinks = {
            "1": {"name": "콜라", "price": 700, "stock": 5},
            "2": {"name": "사이다", "price": 600, "stock": 5},
            "3": {"name": "물", "price": 500, "stock": 5},
        }

    def insert_coin(self, amount):
        if amount not in self.VALID_COINS:
            raise ValueError("지원하지 않는 동전입니다. (100, 500, 1000원만 가능)")
        self.balance += amount

    def purchase(self, drink_code):
        drink = self.drinks.get(drink_code)
        if not drink:
            raise ValueError("존재하지 않는 음료 번호입니다.")
        if drink["stock"] <= 0:
            raise ValueError("재고가 부족합니다.")
        if self.balance < drink["price"]:
            raise ValueError("잔액이 부족합니다.")

        self.balance -= drink["price"]
        drink["stock"] -= 1
        return drink["name"]

    def refund(self):
        refund_amount = self.balance
        self.balance = 0
        return refund_amount


def run_cli():
    machine = VendingMachine()

    while True:
        print("\n===== 동전 음료 자판기 =====")
        print(f"현재 잔액: {machine.balance}원")
        print("음료 목록:")
        for code, drink in machine.drinks.items():
            print(
                f"  {code}. {drink['name']} - {drink['price']}원 (재고: {drink['stock']})"
            )
        print("메뉴: 1) 동전 투입 2) 음료 구매 3) 거스름돈 반환 4) 종료")

        choice = input("선택: ").strip()

        if choice == "1":
            try:
                amount = int(input("투입할 동전 금액 입력 (100/500/1000): ").strip())
                machine.insert_coin(amount)
                print(f"{amount}원이 투입되었습니다.")
            except ValueError as error:
                print(error)
        elif choice == "2":
            drink_code = input("구매할 음료 번호 입력: ").strip()
            try:
                drink_name = machine.purchase(drink_code)
                print(f"{drink_name}가 나왔습니다.")
            except ValueError as error:
                print(error)
        elif choice == "3":
            refund_amount = machine.refund()
            print(f"거스름돈 {refund_amount}원을 반환합니다.")
        elif choice == "4":
            refund_amount = machine.refund()
            if refund_amount:
                print(f"종료 전 거스름돈 {refund_amount}원을 반환합니다.")
            print("자판기를 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    run_cli()
