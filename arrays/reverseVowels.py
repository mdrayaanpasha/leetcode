class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_dict={}
        list_str=list(s)
        vowels=['a','e','i','o','u']
        counter=0
        for index,elem in enumerate(list_str): 
            if elem.lower() in vowels:
                new_dict[counter]=index
                counter+=1

        dict_length=len(new_dict)

       
        for i in range(dict_length // 2):
            list_str[new_dict[i]], list_str[new_dict[dict_length - 1 - i]] = (
                list_str[new_dict[dict_length - 1 - i]],
                list_str[new_dict[i]],
            )

        return "".join(list_str)

            


