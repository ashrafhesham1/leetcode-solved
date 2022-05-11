class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [[1,'I'],[4,'IV'],[5,'V'],[9,'IX'],[10,'X'],[40,'XL'],
                  [50,'L'],[90,'XC'],[100,'C'],[400,'CD'],[500,'D'],
                  [900,'CM'],[1000,'M']]
        
        roman = ''
        for val, rom in reversed(romans):
            if num // val :
                count = num // val
                roman += (rom*count)
                num = num % val
        return roman











    '''   
    romans = {
            1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'
        }
        i=0
        roman = ''
        while num > 0 :

            num, cur = divmod(num,10)
            cur *= 10 ** i

            cur_roman = ''
            while cur > 0 :
                if cur in romans :
                    cur_roman =  cur_roman + romans[cur]
                    break
                else:
                    keys = list(romans.keys())
                    for j in range(len(keys)-1):
                        if keys[j+1] > cur :
                            cur_roman = cur_roman + romans[keys[j]]
                            cur -= keys[j]
                            break
                        elif j+1 == len(keys)-1 :
                            cur_roman = cur_roman + romans[keys[j+1]]
                            cur -= keys[j+1]
                            break

            roman = cur_roman + roman
            i+=1
        return roman
        '''