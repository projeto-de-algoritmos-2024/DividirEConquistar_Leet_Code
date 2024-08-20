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
        
        def mesclar(lists: List[Optional[ListNode]], esquerda: int, direita: int) -> Optional[ListNode]:
            if esquerda == direita:
                return lists[esquerda]
            if esquerda < direita:
                meio = (esquerda + direita) // 2
                lista1 = mesclar(lists, esquerda, meio)
                lista2 = mesclar(lists, meio + 1, direita)
                return mesclarDuasListas(lista1, lista2)
            return None
        
        if not lists:
            return None
        return mesclar(lists, 0, len(lists) - 1)
        
        return None

