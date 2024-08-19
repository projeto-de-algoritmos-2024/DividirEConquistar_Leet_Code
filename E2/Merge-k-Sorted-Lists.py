#from typing import List, Optional

#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mesclarDuasListas(lista1: Optional[ListNode], lista2: Optional[ListNode]) -> Optional[ListNode]:
            no_ficticio = ListNode(0)
            atual = no_ficticio

            while lista1 and lista2:
                if lista1.val < lista2.val:
                    atual.next = lista1
                    lista1 = lista1.next
                else:
                    atual.next = lista2
                    lista2 = lista2.next
                atual = atual.next

            atual.next = lista1 if lista1 else lista2
            return no_ficticio.next
        
        return None

