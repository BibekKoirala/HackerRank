
def Two_Chars(st):
    tmax = current = 0
    char = []
    for i in st:
        if i not in char:
            char.append(i)
    for it in char:
        for jt in char:
            if it != jt:
                if char.index(it) < char.index(jt):
                    for kt in st:
                        if current % 2 == 0 and kt == jt:
                            current = 0
                            break
                        elif current % 2 == 1 and kt == it:
                            current = 0
                            break
                        elif current % 2 == 0 and kt == it:
                            current += 1
                        elif current % 2 == 1 and kt == jt:
                            current += 1
                else:
                    for kt in st:
                        if current % 2 == 0 and kt == it:
                            current = 0
                            break
                        elif current % 2 == 1 and kt == jt:
                            current = 0
                            break
                        elif current % 2 == 0 and kt == jt:
                            current += 1
                        elif current % 2 == 1 and kt == it:
                            current += 1
            print(char)
            tmax = max(tmax, current)
            current = 0

    return tmax



print(Two_Chars('aszhapcjicuxzduyrlnecoywttqutrsrqwzgxmqfszbyrbbspyzeoomxiadsthfyczkyumtwbvlinvqaqpjfodmcxsnilskboiuonuritqnxlqwgkamwzaawenjyyubzajbtckammqpwhzktckiknttgacmjhhwhsgpbhaxzblcjkrdfyyuugcpkzwwypmxpzetzbgkyvqfpvndfbejfaeyuvjubqzfwnypznegkntmszexvmfqftnapxpwclwkghdmxbywwaviryotchkgjagssbmnczfcrxbzwbmwmnpxvojrroowgtwnuwrgwewesivgsyrcqsteewwywmawvadviftxeavovtngafhcqizoqdgjqaovudchtaolzvikqeytcuyerubyhesubspmibqbbwwzzrzltqdptjabavijmvugralehmzylclwenuvshfvcurfrdhwyzdaltyxkwqzkthlzikixsftffawqsjowmmozeefwcudulvntaqudhaxxzqeummadpdprgloffmebqpigpulizldambrkkmzpshrstwyuxbsmtcdgczodammqfsiouayibnncwjcavcjkidzofrsuvfbercyqdsxapyqbpohsywysquuipvmcrxoopvulmqbnetlcsbpgqemwqfizmitewulrbmeoasqfizozmqcfkrfbkafgvmewysktwlqitjtznbownpplaskmpwpxukrhzphxjfjqmqvtgduskxpeqgjznekwbmlgcwklpnpjrpceqkizkgwraipupdkzglgg'))