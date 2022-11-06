class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


# 由列表生成链表(list >> LinkedList)
# 头节点法
def head_list_to_linkedlist(ll):
    head1 = ListNode(ll[0])
    for val in ll[1:]:
        node = ListNode(val)
        node.next = head1
        head1 = node  # 头节点法得到的linked list与list的顺序相反
        # ListNode(val).next = head1
        # head1 = ListNode(val)
    return head1


'''
这里不可使用以下部分来创建，由于没有保存到node,下面两行中的ListNode(val)相当于分别创建了两个毫无关联的新节点。
ListNode(val).next = head1  #生成了节点ListNode(val)
head1.next = ListNode(val)  #生成了另一个节点ListNode(val)，与前一个语句生
'''


# 头节点法补充（简化版）
#对List Node的类定义进行修改

# 尾节点法
def tail_list_to_linkedlist(ll):
    head1 = ListNode(ll[0])
    tail1 = head1
    for val in ll[1:]:
        node = ListNode(val)
        tail1.next = node
        tail1 = node  # 由于只有尾节点移动，所以尾节点法得到的linked list与list顺序相同
    return head1


# 由链表生成列表(LinkedList >> list)
def linkedlist_to_list(head1):
    ll = []
    while head1:
        ll.append(head1.item)
        head1 = head1.next
    return ll


list1 = [1, 2, 3]
head = head_list_to_linkedlist(list1)
print(head.item)

ll = linkedlist_to_list(head)
print(ll)
