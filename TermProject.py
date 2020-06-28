import os

class Account:
        def __init__(self, accName, accNum, accPassword, accBalance):
                self.__accName = accName
                self.__accNum = accNum
                self.__accPassword = accPassword
                self.__accBalance = accBalance

        def deposit(self, amount):
                try:                        
                        file = open("ACC.txt", 'r')

                        print("")
                                        
                        ACCs = file.readlines()
                        file.close()

                        for i in range(1, len(ACCs), 4):

                                if ACCs[i][:-1] == self.__accNum:
                                        self.__accBalance = str(amount + int(self.__accBalance))
                                        
                                        ACCs[i+2] = self.__accBalance + "\n"
                                        file = open("ACC.txt", 'w')

                                        for j in range(len(ACCs)):
                                                file.write(ACCs[j])
                                                
                                        file.close()
                                        
                                        print(amount, "원이 입금되었습니다. 잔액 :", self.__accBalance)
                                        return
                                                         
                except Exception as e:
                        print("오류가 발생했습니다.", e)

        def withdraw(self, amount, password):
                try:                        
                        file = open("ACC.txt", 'r')

                        print("")
                                        
                        ACCs = file.readlines()
                        file.close()

                        for i in range(1, len(ACCs), 4):
                                if ACCs[i][:-1] == self.__accNum and password == self.__accPassword:
                                        if int(self.__accBalance) >= amount:

                                                self.__accBalance = str(int(self.__accBalance)-amount)
                                        
                                                ACCs[i+2] = self.__accBalance + "\n"
                                                file = open("ACC.txt", 'w')

                                                for j in range(len(ACCs)):
                                                        file.write(ACCs[j])

                                                file.close()

                                                print(amount, "원이 출금되었습니다. 잔액 : ",self.__accBalance)
                                                return

                                        else:
                                                print("잔액이 부족합니다.")
                                                return

                        print("비밀번호가 다릅니다.")
                                                         
                except Exception as e:
                        print("오류가 발생했습니다.", e)

        def remittance(self, dest, amount, password):
                try:                        
                        file = open("ACC.txt", 'r')

                        print("")
                                        
                        ACCs = file.readlines()
                        file.close()

                        for i in range(1, len(ACCs), 4):
                                if ACCs[i][:-1] == self.__accNum and password == self.__accPassword:
                                        if int(self.__accBalance) >= amount:
                                                
                                                for j in range(1, len(ACCs), 4):
                                                        if dest == ACCs[j][:-1]:
                                                                self.__accBalance = str(int(self.__accBalance)-amount)

                                                                ACCs[j+2] = str(int(ACCs[j+2]) + amount) + "\n"
                                                                ACCs[i+2] = self.__accBalance + "\n"

                                                                file = open("ACC.txt", 'w')

                                                                for k in range(len(ACCs)):
                                                                        file.write(ACCs[k])

                                                                file.close()

                                                                print(amount, "원이",ACCs[j-1][:-1], "님에게 송금되었습니다. 잔액 : ",self.__accBalance)
                                                                return

                                               
                                                print("잘못된 계좌입니다.")
                                                return

                                        else:
                                                print("잔액이 부족합니다.")
                                                return

                        print("비밀번호가 다릅니다.")
                                                         
                except Exception as e:
                        print("오류가 발생했습니다.", e)

        def inquiry(self, password):


                if self.__accPassword == password:
                        print("")
                        print("예금주\t  잔액")
                        print("================")
                        print(self.__accName, "\t", self.__accBalance)
                        return

                print("비밀번호가 다릅니다.")

def adminMenu():
        while True:
                print("")
                select = int(input("1.계좌생성 2.계좌삭제 3.계좌현황 4.돌아가기 : "))

                if select == 1:
                        print("")
                        try:
                                if os.path.isfile("ACC.txt") == False:
                                        file = open("ACC.txt", 'w')
                                        file.close()
                                        
                                
                                file = open("ACC.txt", 'r')
                                
                                accName = input("예금주 : ")
                                accNum = input("계좌번호 : ")
                                accPassword = input("비밀번호 : ")
                                accBalance = input("잔고 :")
                                
                                ACCs = file.readlines()
                                file.close()

                                if len(ACCs) == 0:
                                        file = open("ACC.txt", 'a')

                                        file.write(accName+"\n")
                                        file.write(accNum+"\n")
                                        file.write(accPassword+"\n")
                                        file.write(accBalance+"\n")

                                        file.close()

                                else:
                                        for i in range(1, len(ACCs), 4):
                                                if ACCs[i][:-1] == accNum:
                                                        print("계좌가 이미 존재합니다.")
                                                        break

                                                elif i+4 > len(ACCs):

                                                        file = open("ACC.txt", 'a')

                                                        file.write(accName+"\n")
                                                        file.write(accNum+"\n")
                                                        file.write(accPassword+"\n")
                                                        file.write(accBalance+"\n")

                                                        file.close()
                                
                        except Exception as e:
                                print("오류가 발생했습니다.", e)
                        


                elif select == 2:
                        print("")
                        try:            
                                
                                file = open("ACC.txt", 'r')
                                
                                accNum = input("삭제할 계좌번호 : ")
                                
                                ACCs = file.readlines()
                                file.close()

                                for i in range(1, len(ACCs), 4):

                                        if ACCs[i][:-1] == accNum:
                                                for j in range(4):
                                                        del ACCs[i-1]


                                                file = open("ACC.txt", 'w')
                                                for j in range(len(ACCs)):
                                                        file.write(ACCs[j])

                                                file.close()
                                                print("계좌가 삭제되었습니다.")
                                                break

                                        elif i+4 > len(ACCs):
                                                print("계좌번호가 없습니다.")
                                                
                                       
                                
                        except Exception as e:
                                print("오류가 발생했습니다.", e)

                elif select == 3:
                        print("")
                        print("예금주\t계좌번호")
                        print("================")
                        try:            
                                
                                file = open("ACC.txt", 'r')
                                
                                ACCs = file.readlines()

                                for i in range(len(ACCs)):
                                        if i % 4 == 2 or i % 4 == 3:
                                                continue
                                        
                                        print(ACCs[i][:-1], end = '\t')

                                        if i % 4 == 1:
                                                print("")

                                file.close()
                                
                        except Exception as e:
                                print("오류가 발생했습니다.", e)

                elif select == 4:
                        break

                else:
                        print("올바른 입력이 아닙니다.")
                        continue

def clientMenu():
        try:            
                                
                file = open("ACC.txt", 'r')

                print("")
                                
                accNum = input("계좌번호 : ")
                                
                ACCs = file.readlines()
                file.close()

                for i in range(1, len(ACCs), 4):

                        if ACCs[i][:-1] == accNum:
                                ACC = Account(ACCs[i-1][:-1], ACCs[i][:-1], ACCs[i+1][:-1], ACCs[i+2][:-1])
                                break

                        elif i+4 > len(ACCs):
                                print("계좌번호가 없습니다.")
                                return
                                                 
        except Exception as e:
                print("오류가 발생했습니다.", e)
        
        while True:
                print("")
                select = int(input("1.입금 2.출금 3.송금 4.잔액조회 5.로그아웃 : "))

                if select == 1:
                        print("")
                        amount = int(input("입금액 : "))
                        
                        ACC.deposit(amount)

                elif select == 2:
                        print("")
                        amount = int(input("출금액 : "))
                        password = input("비밀번호 : ")
                        
                        ACC.withdraw(amount, password)


                elif select == 3:
                        print("")

                        dest = input("송금 계좌 : ")
                        amount = int(input("송금액 : "))
                        password = input("비밀번호 : ")
                        
                        ACC.remittance(dest, amount, password)

                elif select == 4:
                        print("")
                        password = input("비밀번호 : ")
                        
                        ACC.inquiry(password)

                elif select == 5:
                        break

                else:
                        print("올바른 입력이 아닙니다.")
                        continue

if __name__ == "__main__":
        while True:
                print("")
                select = int(input("1.관리자메뉴 2.고객로그인 3.종료 : "))

                if select == 1:
                        adminMenu()

                elif select == 2:
                        clientMenu()

                elif select == 3:
                        break
