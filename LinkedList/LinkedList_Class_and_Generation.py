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
head1.next = ListNode(val)  #生成了另一个节点ListNode(val)，与前一个语句生成的ListNode(val)并无关系
'''


# 头节点法补充（简化版）
# 对List Node的类定义进行修改
class ListNode:
    def __init__(self, item1, next1=None):
        self.item = item1
        self.next = next1


def head_opt_list_to_linkedlist(ll):
    head1 = None
    for val in reversed(ll):
        head1 = ListNode(val, head1)
    return head1


# 尾节点法
def tail_list_to_linkedlist(ll):
    head1 = ListNode(ll[0])
    tail1 = head1
    for val in ll[1:]:
        node = ListNode(val)
        tail1.next = node
        tail1 = node  # 由于只有尾节点移动，所以尾节点法得到的linked list与list顺序相同
    return head1


# 尾节点法简化版
def tail_opt_list_to_linkedlist(ll):
    head1 = ListNode(ll[0])
    tail1 = head1
    for val in ll[1:]:
        tail1.next = ListNode(val)  #区分与头节点法简化的区别，这里可以直接使用，新建的节点ListNode(val)即赋值给tail.next
        tail1 = tail1.next
    return head1


# 由链表生成列表(LinkedList >> list)
def linkedlist_to_list(head1):
    ll = []
    while head1:
        ll.append(head1.item)  # 得到的list与linked list顺序相同
        head1 = head1.next
    return ll


list1 = [1, 2, 3]
head = tail_opt_list_to_linkedlist(list1)
print(head.next.next.item)

ll = linkedlist_to_list(head)
print(ll)
