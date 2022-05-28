class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        senderToWords = {}
        for i,sender in enumerate(senders):
            count = len(messages[i].split(' '))
            if sender in senderToWords :
                senderToWords[sender] += count
            else:
                senderToWords[sender] = count

        maxCount = 0
        for key in senderToWords:
            if senderToWords[key] > maxCount :
                maxCount = senderToWords[key]
        
        maxSender = []
        for key in senderToWords:
            if senderToWords[key] == maxCount :
                maxSender.append(key)
        
        return sorted(maxSender,reverse=True)[0]