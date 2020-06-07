class DES:

        def setPadding(self, text):
                temp = list(map(ord, text))
                init = str()
                
                result = list()

                for i in range(len(temp)):
                        init += (str(format(temp[i], 'b').zfill(8)))

                for i in range((len(init)//64)+1):

                        if len(init)<(64*i)+64:
                                result.append(init[64*i:len(init)])

                        else:
                                result.append(init[64*i:64*i+64])

                if result[len(result)-1] == '':
                        del result[len(result)-1]

                if len(result[len(result)-1]) < 64:
                        while True:
                                result[len(result)-1] += '0'
                                if len(result[len(result)-1]) % 64 == 0:
                                        break
                return result
                

        def initialPermutation(self, initText):
                initPBox = [58, 50, 42, 34, 26, 18, 10, 2,
                            60, 52, 44, 36, 28, 20, 12, 4,
                            62, 54, 46, 38, 30, 22, 14, 6,
                            64, 56, 48, 40, 32, 24, 16, 8,
                            57, 49, 41, 33, 25, 17, 9, 1,
                            59, 51, 43, 35, 27, 19, 11, 3,
                            61, 53, 45, 37, 29, 21, 13, 5,
                            63, 55, 47, 39, 31, 23, 15, 7]

                result = []
                
                for i in initText:
                        temp = ""
                        for j in range(len(initPBox)):
                                temp += i[initPBox[j]-1]        

                        result.append(temp)
                return result

        def mixer(self, leftSplited, rightSplited, roundKeys, i):            
                rightFunction = self.function(rightSplited, roundKeys[i])

                result = ''
                leftSplited = leftSplited[0]

                for i in range(len(leftSplited)):
                        
                        if rightFunction[i] == leftSplited[i]:
                                result += '0'
                        else:
                                result += '1'
                return result
                                

        def splitPlainText(self, initPermutated):
                left = []
                right = []
                for i in initPermutated:
                        left.append(i[0:32])
                        right.append(i[32:64])

                return left, right

        def combine(self, left, right):
                result = str(left) + str(right)
                return result
                
        def finalPermutation(self, combined):
                finalPBox = [40, 8, 48, 16, 56, 24, 64, 32,
                             39, 7, 47, 15, 55, 23, 63, 31,
                             38, 6, 46, 14, 54, 22, 62, 30,
                             37, 5, 45, 13, 53, 21, 61, 29,
                             36, 4, 44, 12, 52, 20, 60, 28,
                             35, 3, 43, 11, 51, 19, 59, 27,
                             34, 2, 42, 10, 50, 18, 58, 26,
                             33, 1, 41, 9, 49, 17, 57, 25]

                result = []
                
                for i in combined:
                        temp = ""
                        for j in range(len(finalPBox)):
                                temp += i[finalPBox[j]-1]        

                        result.append(temp)
                return result

        def subsitute(self, exclusiveOred):
                sBox = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                        [0, 15, 7, 4, 14, 2, 13, 10, 3, 6, 12, 11, 9, 5, 3, 8],
                        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

                result = ''
                
                for i in range(8):
                        row = 2*int(exclusiveOred[i*6]) + int(exclusiveOred[i*6+5])
                        col = 8*int(exclusiveOred[i*6+1]) + 4*int(exclusiveOred[i*6+2]) + 2*int(exclusiveOred[i*6+3]) + int(exclusiveOred[i*6+4])

                        value = sBox[row][col]

                        value = str(format(value, 'b').zfill(4))
                        result += value
                
                return result

        def straightPermutation(self, subsituted):
                straightPBox = [16, 7, 20, 21, 29, 12, 28, 17,
                                1, 15, 23, 26, 5, 18, 31, 10,
                                2, 8, 24, 14, 32, 27, 3, 9,
                                19, 13, 30, 6, 22, 11, 4, 25]

                subsituted = [subsituted]

                result = []
                
                for i in subsituted:
                        temp = ""
                        for j in range(len(straightPBox)):
                                temp += i[straightPBox[j]-1]        

                        result.append(temp)

                return result[0]

        def function(self, right, roundKey):
                right48Bit = self.expansionPermutation(right)
                right48Bit = right48Bit[0]

                exclusiveOred = ""

                for i in range(len(roundKey)):
                        if right48Bit[i] == roundKey[i]:
                                exclusiveOred += "0"
                        else:
                                exclusiveOred += "1"

                subsituted = self.subsitute(exclusiveOred)
                straightPermutated = self.straightPermutation(subsituted)

                return straightPermutated

        def expansionPermutation(self, rightHalf):
                expansionPBox = [32, 1, 2, 3, 4, 5, 
                                 4, 5, 6, 7, 8, 9,
                                 8, 9, 10, 11, 12, 13,
                                 12, 13, 14, 15, 16, 17,
                                 16, 17, 18, 19, 20, 21,
                                 20, 21, 22, 23, 24, 25,
                                 24, 25, 26, 27, 28, 29,
                                 28, 29, 31, 31, 32, 1]

                result = []
                for i in rightHalf:
                        temp = ""
                        for j in range(len(expansionPBox)):
                                temp += i[expansionPBox[j]-1]        

                        result.append(temp)

                return result

        def keyPermutation(self, seedKey):
                keyPBox = [57, 49, 41, 33, 25, 17, 9, 1,
                           58, 50, 42, 34, 26, 18, 10, 2,
                           59, 51, 43, 35, 27, 19, 11, 3,
                           60, 52, 44, 36, 63, 55, 47, 39,
                           31, 23, 15, 7, 62, 54, 46, 38,
                           30, 22, 14, 6, 61, 53, 45, 37,
                           29, 21, 13, 5, 28, 20, 12, 4]

                result = []
                for i in seedKey:
                        temp = ""
                        for j in range(len(keyPBox)):
                                temp += i[keyPBox[j]-1]        

                        result.append(temp)

                return result

        def shiftLeft(self, key, i):
                shiftAmount = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
                
                amount = shiftAmount[i]
                keyList = []

                for keyIndex in range(len(key)):
                        keyList.append(key[keyIndex])

                for j in range(amount):
                        temp = keyList[0]
                        for k in range(1, 28):
                                keyList[k-1] = keyList[k]

                        keyList[27] = temp

                result = ""

                for key in keyList:
                        result += key
                        
                return result

        def compressionPermutation(self, preRoundKey):
                compressionPBox = [14, 17, 11, 24, 1, 5, 3, 28,
                                   15, 6, 21, 10, 23, 19, 12, 4,
                                   26, 8, 16, 7, 27, 20, 13, 2,
                                   41, 52, 31, 37, 47, 55, 30, 40,
                                   51, 45, 33, 48, 44, 49, 39, 56,
                                   34, 53, 46, 42, 50, 36, 29, 32]

                preRoundKey = [preRoundKey]

                result = []
                for i in preRoundKey:
                        temp = ""
                        for j in range(len(compressionPBox)):
                                temp += i[compressionPBox[j]-1]        

                        result.append(temp)

                return result                

        def keyGenerate(self, seedKey):
                key56Bit = self.keyPermutation(seedKey)
                leftKey, rightKey = self.splitKey(key56Bit)
                
                leftKey = leftKey[0]
                rightKey = rightKey[0]

                result = []

                for i in range(16):        
                        leftKey = self.shiftLeft(leftKey, i)
                        rightKey = self.shiftLeft(rightKey, i)
                        preRoundKey = leftKey + rightKey
                        result.append(self.compressionPermutation(preRoundKey)[0])
                
                return result
        
                        

        def splitKey(self, key56Bit):
                left = []
                right = []
                for i in key56Bit:
                        left.append(i[0:28])
                        right.append(i[28:56])

                return left, right                

while True:
        plainText = input("임의의 문자를 입력 (종료 : 입력 없이 엔터) ")
        
        if plainText == "":
                break
        
        seedKey = input("Seed Key 입력 (1 ~ 64 Bit Text) ")

        if seedKey == "":
                print("Seed Key가 입력되지 않았습니다.")
                continue

        seedKey = seedKey.encode()

        if len(seedKey) > 8:
                print("Seed Key의 범위는 64 Bit까지 지원")
                continue

        print("\n")
        seedKey = seedKey.decode()
        
        des = DES()

        initText = des.setPadding(plainText)
        seedKey = des.setPadding(seedKey)
        
        roundKeys = des.keyGenerate(seedKey)
        encryptedMessage = []

        print(initText)
        print("평문 문자열 :",end = " ")

        for message in initText:
                for i in range(8):
                        temp = message[i*8:i*8+8].strip()
                        print(chr(int(temp,2)), end= "")
        print("\n")
        

        for text in initText:
                text = [text]

                initPermutated = des.initialPermutation(text)
                                        
                leftSplited, rightSplited = des.splitPlainText(initPermutated)

                for i in range(16):
                        rightMixed = des.mixer(leftSplited, rightSplited, roundKeys, i)
                        leftSplited = [rightMixed]
                        
                        if i!= 15:
                                leftSplited, rightSplited = rightSplited, leftSplited

                leftSplited = leftSplited[0]
                rightSplited = rightSplited[0]

                
        
                combined = des.combine(leftSplited, rightSplited)
                combined = [combined]

                encryptedMessage.append(des.finalPermutation(combined)[0])

        print(encryptedMessage)
        print("암호화된 문자열 :",end = " ")

        for message in encryptedMessage:
                for i in range(8):
                        temp = message[i*8:i*8+8]
                        print(chr(int(temp,2)), end= "")
                        
        print("\n")

        roundKeys.reverse()

        decryptedMessage = []

        for text in encryptedMessage:

                text = [text]

                initPermutated = des.initialPermutation(text)
                leftSplited, rightSplited = des.splitPlainText(initPermutated)
                
                for i in range(16):
                        rightMixed = des.mixer(leftSplited, rightSplited, roundKeys, i)
                        leftSplited = [rightMixed]
                        
                        if i!= 15:
                                leftSplited, rightSplited = rightSplited, leftSplited

                leftSplited = leftSplited[0]
                rightSplited = rightSplited[0]
        
                combined = des.combine(leftSplited, rightSplited)

                combined = [combined]
                decryptedMessage.append(des.finalPermutation(combined)[0])

        
        print(decryptedMessage)
        print("복호화된 문자열 :",end = " ")

        for message in decryptedMessage:
                for i in range(8):
                        temp = message[i*8:i*8+8]
                        print(chr(int(temp,2)), end= "")

        if decryptedMessage == initText:
                print("\n\n평문과 복문이 일치함")

        print("\n")


        

        
        

