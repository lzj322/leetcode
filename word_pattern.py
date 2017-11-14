class Solution(object):
    def wordPattern(self, pattern, sstr):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #print pattern
        #print sstr
        plen=len(pattern)
        slist=sstr.split()
        if len(slist)!=plen:
        	return False
       	else:
        	di=dict()
        	tem=list()
        	pos=0
        	for word in slist:
        		if word not in di:
        			if pattern[pos] not in tem:
        				tem.append(pattern[pos])
        				di[word]=pattern[pos]
        			else:
        				return False
        		pos+=1
        	for p in range(plen):
        		if di[slist[p]] != pattern[p]:
        			return False
        	return True

        
pattern="abaa"
sstr='dog cat dog dog'       
s=Solution()
print s.wordPattern(pattern,sstr)

