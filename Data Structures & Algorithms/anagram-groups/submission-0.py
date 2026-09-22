from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)
    
        for mot in strs:
            cle = "".join(sorted(mot))  # même clé pour toutes les anagrammes
            groupes[cle].append(mot)
        
        return list(groupes.values())